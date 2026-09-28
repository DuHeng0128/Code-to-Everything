#!/usr/bin/env python3
"""Validate metadata and local documentation without making network requests."""
import json,re,sys,unicodedata
from pathlib import Path
from urllib.parse import urlsplit,unquote
from datetime import date
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]

def normalized_title(s):
    return re.sub(r'\W','',unicodedata.normalize('NFKC',s).casefold())

def record_errors(papers,taxonomy):
    errors=[];homes={(t['id'],s['id']) for t in taxonomy for s in t['subcategories']};domains={t['id'] for t in taxonomy}
    required={'id','title','authors','year','first_public_date','date_basis','url','arxiv_id','doi','domain','subcategory','kind','program_role','summary','summary_zh','reading_depth','checked_on','added_on','milestone','milestone_reason','milestone_reason_zh'}
    for p in papers:
        key=p.get('id','<missing>');missing=required-p.keys()
        if missing:errors.append(f'{key}: missing {sorted(missing)}');continue
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*',key):errors.append(f'{key}: unsafe citation key')
        for f in ['title','summary','summary_zh','program_role','date_basis']:
            if not isinstance(p[f],str) or not p[f].strip():errors.append(f'{key}: empty {f}')
        if not isinstance(p['authors'],list) or not p['authors'] or any(not isinstance(a,str) or not a.strip() for a in p['authors']):errors.append(f'{key}: invalid authors')
        if not isinstance(p['year'],int) or not 1900<=p['year']<=date.today().year:errors.append(f'{key}: invalid year')
        if (p['domain'],p['subcategory']) not in homes:errors.append(f'{key}: unknown taxonomy home')
        if set(p.get('related_domains',[]))-domains:errors.append(f'{key}: unknown related domain')
        if p['kind'] not in {'method','benchmark','background','comparison','survey'}:errors.append(f'{key}: invalid kind')
        if p['reading_depth'] not in {'abstract','sections'}:errors.append(f'{key}: invalid reading depth')
        for f in ['first_public_date','checked_on','added_on']:
            v=p[f]
            try:
                if not re.fullmatch(r'\d{4}(-\d{2}){0,2}',v):raise ValueError()
                date.fromisoformat(v+'-01'*(2-v.count('-')))
            except (ValueError,TypeError):errors.append(f'{key}: invalid {f}')
        if p['arxiv_id'] and not re.fullmatch(r'\d{4}\.\d{4,5}',p['arxiv_id']):errors.append(f'{key}: invalid/versioned arXiv ID')
        if p['doi'] and not p['doi'].startswith('10.'):errors.append(f'{key}: invalid DOI')
        for f in ['url','code_url','project_url']:
            if p.get(f):
                u=urlsplit(p[f])
                if u.scheme not in {'https','http'} or not u.netloc or re.search(r'[\s<>]',p[f]):errors.append(f'{key}: invalid {f}')
        if p['milestone'] and not (p['milestone_reason'] and p['milestone_reason_zh']):errors.append(f'{key}: unexplained milestone')
    for field,transform in [('id',str.casefold),('doi',str.casefold),('arxiv_id',str),('title',normalized_title)]:
        values=[transform(p[field]) for p in papers if p.get(field)]
        errors += [f'duplicate {field}: {v}' for v,c in Counter(values).items() if c>1]
    return errors

def local_link_errors(root):
    errors=[]
    for file in root.rglob('*.md'):
        if '.git' in file.parts:continue
        text=file.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if target.startswith(('http:','https:','mailto:','#')):continue
            target=unquote(target.split('#')[0])
            if target and not (file.parent/target).exists():errors.append(f'{file.relative_to(root)}: missing link {target}')
    return errors

def main():
    p=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'));t=json.loads((ROOT/'data/taxonomy.json').read_text(encoding='utf-8'))
    errors=record_errors(p,t)+local_link_errors(ROOT)
    if errors:print('\n'.join(errors),file=sys.stderr);raise SystemExit(1)
    print(f'Validated {len(p)} unique records, taxonomy, citation keys and local file links.')
if __name__=='__main__':main()
