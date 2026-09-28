# Working on this collection

- Read CONTRIBUTING.md and docs/taxonomy.md before classifying papers.
- Edit data/papers.json for records; data/taxonomy.json for the hierarchy; data/repository.json for curation dates.
- README.md, README.zh-CN.md, data/papers.csv, references.bib and references.ris are generated. Run `python scripts/build.py` after edits; do not patch generated output alone.
- Keep original-source URLs, stable keys, first-public dates and reading-depth labels. Do not infer conference acceptance from a template or fabricate missing authors, code links, budgets or results.
- Code must contribute to the task, or the entry must be explicitly labeled as background/comparison/benchmark/survey. Review automatically discovered candidates before inclusion.
- Explain milestone status in both languages. Do not equate multi-task coverage with transfer, executable code with scientific correctness, or a proof check with faithful formalization.
- Run `python scripts/validate.py`, `python scripts/build.py --check`, and `python -m unittest discover -s tests` before completion.
- Do not publish the working survey title as a paper citation before a manuscript exists. Preserve user changes and do not push without authorization.
