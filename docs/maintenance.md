# Maintaining a living collection

[Home](../README.md) · [Contribution rules](../CONTRIBUTING.md)

## One source of truth

| File | Maintainer edits it? | Purpose |
|---|---|---|
| `data/papers.json` | Yes | Records, annotations, categories, source checks and milestone reasons |
| `data/taxonomy.json` | Yes | Domain and subcategory definitions in both languages |
| `data/repository.json` | Yes | Curation date and coverage boundary |
| `data/search_queries.json` | Yes | Explicit discovery queries |
| `scripts/build.py` | When changing presentation | Generates reader-facing indexes and exports |
| `README.md`, `README.zh-CN.md` | Generated | English and Chinese paper indexes |
| `references.bib`, `references.ris`, `data/papers.csv` | Generated | Reusable bibliographic exports |
| `docs/*.md` | Yes | Reading paths, evidence comparisons and curation history |

After editing accepted records, run `python scripts/build.py`, then `python scripts/validate.py`. Commit the source and generated changes together. `python scripts/build.py --check` checks that they agree without rewriting files.

## Weekly discovery

The GitHub workflow **Discover literature candidates** is configured for Monday **01:23 UTC / 09:23 Asia/Shanghai** and supports manual dispatch. Once the workflow is on the default branch and Actions is enabled, it queries the public arXiv API over an overlapping 21-day window. No model API key is required.

The output is an Actions artifact and job summary containing unreviewed titles, authors, source links and matched query groups. It does not commit files, open issues, send messages or accept papers. Download the artifact, examine original sources, then add worthwhile records through the normal contribution process.

```sh
python scripts/discover.py --days 21
```

Use `--max-queries 1 --max-pages 1` for a small connectivity check. The default is eight query groups and at most two 100-result pages per query. Queries are separated by at least three seconds; temporary request failures are retried. Failed queries make the run visibly fail while preserving partial results. Pagination limits are recorded as `truncated: true`; a truncated query is not complete coverage.

GitHub schedules can be delayed, and scheduled workflows in inactive public repositories may be disabled. Check the Actions page periodically. Failed API access is not evidence that no new papers exist. Workflow details follow the [GitHub documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax); search syntax and rate considerations follow the [arXiv API manual](https://info.arxiv.org/help/api/user-manual.html).

## A practical review rhythm

- **Weekly:** review the candidate artifact and community submissions; correct metadata and add clear advances.
- **Monthly:** follow references and author projects for important papers missed by keywords; revisit weakly covered domains and read selected A entries more deeply.
- **Before a survey release:** recheck milestone choices, release-state notes, venue claims, bibliography consistency and experimental qualifications.

The search only finds recent arXiv submissions. It does not cover every conference, journal, technical report or repository. Backward/forward citation tracking, original project pages and expert suggestions remain necessary. Title keywords are a discovery aid, not an inclusion rule.

## Checks and export scope

The validator checks mandatory metadata, unique IDs/DOIs/arXiv IDs/normalized titles, dates, category membership, safe source URLs and local documentation links. Unit tests cover duplicate rejection and candidate parsing/deduplication, including API error feeds. These checks do not certify scientific claims or the live availability of every external link.

RIS and BibTeX contain the same accepted records as the paper index. Initial exports were parsed independently with rispy and bibtexparser. No Zotero desktop import or research-system reproduction was performed. Later edits should retain this distinction.

## 中文操作说明

日常维护只需改`data/papers.json`，然后运行生成与检查命令。不要分别手改中英文README、CSV、RIS和BibTeX。每周工作流只负责找候选，是否收录、如何分类、是否标里程碑由维护者判断。这样可以持续更新，同时避免把关键词命中、模型摘要或尚未核实的宣传语直接变成正式文献判断。
