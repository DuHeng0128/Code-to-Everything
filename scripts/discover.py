#!/usr/bin/env python3
"""Fetch arXiv candidates. This script NEVER edits the accepted collection."""
import argparse,json,re,sys,time,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from datetime import datetime,timedelta,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NS={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}

def canonical_id(url):
    match=re.search(r'(\d{4}\.\d{4,5})(?:v\d+)?$',url.strip())
    return match.group(1) if match else ''

def parse_feed(raw):
    tree=ET.fromstring(raw);entries=[]
    for e in tree.findall('a:entry',NS):
        aid=canonical_id(e.findtext('a:id','',NS))
        if not aid:raise ValueError('arXiv returned an error entry or unsupported identifier')
        entries.append(dict(arxiv_id=aid,title=' '.join(e.findtext('a:title','',NS).split()),authors=[n.text or '' for n in e.findall('a:author/a:name',NS)],published=e.findtext('a:published','',NS),updated=e.findtext('a:updated','',NS),url='https://arxiv.org/abs/'+aid,status='candidate; not accepted'))
    total=tree.findtext('o:totalResults',None,NS)
    if total is None:raise ValueError('Missing totalResults: refusing to interpret an invalid feed as zero results')
    return entries,int(total)

def merge_candidates(groups,existing):
    merged={}
    for area,items in groups:
        for item in items:
            key=item['arxiv_id']
            if key in existing:continue
            if key not in merged:merged[key]=dict(item,matched_queries=[])
            if area not in merged[key]['matched_queries']:merged[key]['matched_queries'].append(area)
    return sorted(merged.values(),key=lambda p:(p['published'],p['arxiv_id']),reverse=True)

def fetch(query,start,max_results):
    params=urllib.parse.urlencode(dict(search_query=query,start=start,max_results=max_results,sortBy='submittedDate',sortOrder='descending'))
    request=urllib.request.Request('https://export.arxiv.org/api/query?'+params,headers={'User-Agent':'CodeToEverything-LiteratureDiscovery/1.0 (+https://github.com/DuHeng0128/Code-to-Everything)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request,timeout=30) as response:return response.read()
        except Exception:
            if attempt==2:raise
            time.sleep(6*(attempt+1))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--days',type=int,default=21);parser.add_argument('--output',type=Path,default=ROOT/'candidate_reports');parser.add_argument('--max-pages',type=int,default=2);parser.add_argument('--max-queries',type=int,default=8);args=parser.parse_args()
    if not 1<=args.days<=365 or not 1<=args.max_pages<=10 or not 1<=args.max_queries<=8:parser.error('days 1–365; max-pages 1–10; max-queries 1–8')
    now=datetime.now(timezone.utc);begin=now-timedelta(days=args.days)
    queries=json.loads((ROOT/'data/search_queries.json').read_text(encoding='utf-8'))[:args.max_queries]
    existing={p['arxiv_id'] for p in json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8')) if p['arxiv_id']}
    groups=[];log=[];errors=[];last_request=0.0
    for q in queries:
        items=[];query=f'({q["query"]}) AND submittedDate:[{begin:%Y%m%d}0000 TO {now:%Y%m%d}2359]';truncated=False
        try:
            for page in range(args.max_pages):
                time.sleep(max(0,3.1-(time.monotonic()-last_request)))
                raw=fetch(query,page*100,100);last_request=time.monotonic();batch,total=parse_feed(raw);items.extend(batch)
                truncated=total>(page+1)*100
                if not truncated:break
            groups.append((q['area'],items));log.append(dict(area=q['area'],query=query,returned=len(items),total=total,truncated=truncated))
            print(q['area'],len(items),'items',flush=True)
        except Exception as e:
            errors.append(dict(area=q['area'],error=str(e)));log.append(dict(area=q['area'],query=query,error=str(e)));print(q['area'],'FAILED',file=sys.stderr,flush=True)
    candidates=merge_candidates(groups,existing);args.output.mkdir(parents=True,exist_ok=True)
    result=dict(fetched_at=now.isoformat(),window_start=begin.isoformat(),status='partial_failure' if errors else 'ok',queries=log,candidates=candidates,errors=errors)
    (args.output/'candidates.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# arXiv candidate report','',f'Fetched {now:%Y-%m-%d}, last {args.days} days. {len(candidates)} unseen IDs.','', '**Not accepted literature.** Read the source, check relevance and metadata, and assess the role of code before adding anything.','',f'Search status: {result["status"]}. Query truncation and errors are recorded in candidates.json.','', '| Date | Paper | Queries |','|---|---|---|']
    for p in candidates:
        title=p['title'].replace('|','&#124;').replace('[','(').replace(']',')').replace('<','&lt;')
        lines.append(f'| {p["published"][:10]} | [{title}]({p["url"]}) | {", ".join(p["matched_queries"])} |')
    if errors:lines+=['','## Failed queries']+[f'- {e["area"]}: {e["error"]}' for e in errors]
    (args.output/'candidates.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
