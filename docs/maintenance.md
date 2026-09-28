# Maintaining a living collection

[Home](../README.md) · [Contribution rules](../CONTRIBUTING.md)

## One source of truth

| File | Maintainer edits it? | Purpose |
|---|---|---|
| `data/papers.json` | Yes | Records, annotations, categories, source checks and milestone reasons |
| `data/taxonomy.json` | Yes | Domain definitions, bilingual overviews and keys selecting expanded analyses |
| `data/repository.json` | Yes | Curation date and coverage boundary |
| `data/search_queries.json` | Yes | Explicit discovery queries |
| `scripts/build.py` | When changing presentation | Generates reader-facing indexes and exports |
| `README.md`, `README.zh-CN.md` | Generated | English and Chinese paper indexes |
| `references.bib`, `references.ris`, `data/papers.csv` | Generated | Reusable bibliographic exports |
| `docs/paper-notes*.md` | Generated | Inputs/outputs, mechanisms, feedback, experiments, comparisons and source locations |
| Other `docs/*.md` | Yes | Cross-method comparisons and curation history |

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
- **Monthly:** follow references and author projects for papers missed by keywords; expand source-based analysis in weakly covered domains.
- **Before a survey release:** recheck milestone choices, release-state notes, venue claims, bibliography consistency and experimental qualifications.

The search only finds recent arXiv submissions. It does not cover every conference, journal, technical report or repository. Backward/forward citation tracking, original project pages and expert suggestions remain necessary. Title keywords are a discovery aid, not an inclusion rule.

## Checks and export scope

The validator checks metadata, unique IDs/DOIs/arXiv IDs/normalized titles, dates, category membership, source URLs and local documentation links. It also checks bilingual note completeness, comparison references and the membership of representative papers. Unit tests cover these relationships and candidate parsing/deduplication, including API error feeds.

RIS and BibTeX contain the same accepted records as the paper index. Initial exports were parsed independently with rispy and bibtexparser.

## 中文操作说明

论文机制、实验结果与来源位置写在 `data/papers.json`，领域概览及扩展分析列表写在 `data/taxonomy.json`。运行生成命令后，中英文 README、分析页和文献导出一并更新。每周工作流提供候选，维护者根据原始来源决定是否收录。
