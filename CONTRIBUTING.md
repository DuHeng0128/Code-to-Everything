# Contributing papers and corrections

Contributions include papers, method analysis, experimental comparisons and metadata corrections.

## Inclusion

For a method, identify the program that the model generates, edits, selects or executes and explain how it advances the task. Include important historical work, benchmarks, surveys and alternative routes with the appropriate `kind`. Do not include every AI paper implemented in Python. Keep ordinary software-engineering work only when it establishes a foundation relevant to the broader scope.

Use original papers, proceedings, publisher pages and author repositories. Keep one record for a preprint and its published version; do not count a paper, project page and code repository as three studies.

## Add or correct a record

1. Search `data/papers.json` by arXiv ID, DOI and normalized title before adding anything.
2. Copy an existing record and assign a stable, unique alphanumeric `id`. Keep full authors and verified title. Unknown DOI, venue or code URL stays empty.
3. Select one domain/subcategory from `data/taxonomy.json`. Use `related_domains` for cross-domain connections. See [taxonomy](docs/taxonomy.md).
4. Write short `summary` and `summary_zh` annotations that identify the mechanism and distinctive design. For an expanded analysis, fill bilingual `io`, `feedback` and `takeaway` fields, plus `compare_with` keys. Detailed mechanisms and experiments use `mechanism`, `experiment` and their `_zh` counterparts, with an `analysis_source` URL and bilingual `analysis_location` identifying sections or tables. Add the paper to its domain's `focus_papers` for inclusion in the analysis page.
5. Preserve internal source provenance in `reading_depth`, `read_sections`, `checked_on` and version fields. `abstract` records abstract/metadata screening; `sections` records the specified source sections. Public pages display method analysis and source citations without reading-depth badges.
6. Sort by first public date, normally arXiv v1. Keep available precision (`YYYY-MM` is fine). `year` can be the publication year; explain the relation in metadata. A conference template does not prove acceptance.
7. If proposing `milestone: true`, explain the specific turning point in both languages. Recency, citation count and a high score are not sufficient by themselves.
8. Run the commands below, inspect the generated diff, and open a pull request.

```sh
python scripts/build.py
python scripts/validate.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

The build and checks use Python 3.10+ and the standard library. README files, `docs/paper-notes*.md` and bibliographic exports are generated from the JSON source. Domain introductions and analysis selections live in `data/taxonomy.json`.

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

原始来源、作者、稳定 ID 与首次公开时间保存在 JSON 中。方法分析注明程序表示、核心机制和实验条件，详细结论附具体版本与章节或表格。里程碑说明对应的研究进展。内部来源核查记录随补读更新，公开页面不显示阅读深度标记。
