# Contributing papers and corrections

Thank you for helping make this collection useful. A good contribution explains why a paper changes our understanding, not just where to insert its title.

## Inclusion

For a method, identify the program that the model generates, edits, selects or executes and explain how it advances the task. Include important historical work, benchmarks, surveys and alternative routes with the appropriate `kind`. Do not include every AI paper implemented in Python. Keep ordinary software-engineering work only when it establishes a foundation relevant to the broader scope.

Use original papers, proceedings, publisher pages and author repositories. Keep one record for a preprint and its published version; do not count a paper, project page and code repository as three studies.

## Add or correct a record

1. Search `data/papers.json` by arXiv ID, DOI and normalized title before adding anything.
2. Copy an existing record and assign a stable, unique alphanumeric `id`. Keep full authors and verified title. Unknown DOI, venue or code URL stays empty.
3. Select one domain/subcategory from `data/taxonomy.json`. Use `related_domains` for cross-domain connections. See [taxonomy](docs/taxonomy.md).
4. Write short `summary` and `summary_zh` annotations. Say what code does and why the paper belongs; avoid copying the abstract or adding unsupported performance claims.
5. Set `reading_depth` honestly. `abstract` means metadata/abstract screened; `sections` means specified original sections were read. Fill `read_sections`, `checked_on`, version and protocol notes accordingly. Neither label means reproduction.
6. Sort by first public date, normally arXiv v1. Keep available precision (`YYYY-MM` is fine). `year` can be the publication year; explain the relation in metadata. A conference template does not prove acceptance.
7. If proposing `milestone: true`, explain the specific turning point in both languages. Recency, citation count and a high score are not sufficient by themselves.
8. Run the commands below, inspect the generated diff, and open a pull request.

```sh
python scripts/build.py
python scripts/validate.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

The build and checks use Python 3.10+ and the standard library. Edit the JSON source rather than changing one generated table while leaving the other exports stale.

## What to include in a submission

- Original paper link, stable identifier and title.
- Suggested category and a sentence describing the role of code.
- Executor, feedback and important external tools, when checked in the paper.
- Reading depth, exact sections/version and any experimental qualification.
- Whether this is a new paper, a corrected record, or a proposed reclassification.

You can use the [paper suggestion form](https://github.com/DuHeng0128/Code-to-Everything/issues/new?template=paper.yml) without editing JSON. A suggestion does not imply automatic acceptance.

## Corrections are first-class contributions

Especially useful corrections include a missing foundational paper, a misleading role-of-code label, duplicate versions, incorrect author/venue metadata, and results quoted without their model or search budget. A paper can be important while a particular claim remains uncertain.

## 中文维护要点

优先保留原始来源、准确作者、稳定ID与首次公开时间；不要把“用了代码”一概当成code agent，也不要给论文推测录用会议。每次新增只改统一JSON数据，再生成中英文目录与文献文件。提出里程碑时说明它改变了哪一步工作方式。阅读仅到摘要就保留A标签；补读方法、消融和局限后再改为K。
