# Curation log

## 2026-09-28 — Initial repository collection

The collection starts from a research dossier whose broad search and selected full-text reading were performed on 2026-09-12/13. Its candidate list contained 204 records and 154 selected references, including two public commentaries and an event-specific technical report.

The public index carries over **151** of those records. The event-specific Navier–Stokes report and its two commentaries are not promoted into a repository category or a milestone. The mathematics section is organized around program-aided reasoning, formal proof and mathematical research systems.

**Sixteen original-source additions** bring the index to **167 records**. Twelve repair historical/topic gaps: NS-VQA, SketchAdapt, ShapeAssembly, DeepCAD, GPT-f, HyperTree Proof Search, Draft/Sketch/Prove, ProgPrompt, Instruct2Act, BlenderAlchemy, SciCode and LL3M. Four recent robot-program papers are Auto-HSI, Learning and Transferring Closed-Loop Robot Software, M³P-R1 and RIVET. Their original arXiv records, authors and abstracts were checked on 2026-09-28; full protocols were not audited, so they remain A.

The 45 K records retain their actual source-check dates and reading locations from the dossier. Bibliographic updates do not silently promote a paper's reading depth. This update did not repeat a comprehensive search across all domains for September 14–28; recent searches were targeted and are not exhaustive.

## Search and source trail

The targeted search used title lookups and combinations including `ProgPrompt Instruct2Act robot task plans code`, `ShapeAssembly SketchAdapt neural symbolic VQA`, `Draft Sketch Prove GPT-f SciCode`, `BlenderAlchemy iterative refinement`, and recent robot/code-generation queries. Search results were used to find original arXiv records, author pages and the existing reference repository. No search-engine result count is reported as a paper count.

Original records for new entries are linked in the [index](../README.md#paper-index); stable keys also resolve in [JSON](../data/papers.json), [BibTeX](../references.bib) and [RIS](../references.ris). Earlier formal publication metadata may still rely on authors' arXiv journal references/comments; their provenance is retained rather than silently upgraded to independent confirmation.

## Editorial choices

The primary hierarchy is domain → concrete task. Cross-domain links use facets. The 21 milestone selections explain specific changes in the role of programs, rather than following a recent-first ranking. Background and complementary systems remain visible, so the collection does not portray all advances in perception, VLA control or neural world models as code-agent results.

The reference repository [MLLM-Token-Compression](https://github.com/yaolinli/MLLM-Token-Compression) informed the annotated-table and contribution-rule approach. Its paper text and tables were not copied. No survey author list, DOI, acceptance or publication status has been invented for this project.

## Initial verification boundary

Local checks cover metadata, category membership, duplicate identities, generated-file consistency, local links, candidate parsing and bibliography parsing. One live arXiv query completed successfully and produced five unseen candidates; those hits were not automatically added. The full eight-query scheduled workflow has not been run on GitHub. Live external code availability was not exhaustively tested. The project was prepared against remote base commit `e1a04942966d272567b2c7e78775c9c9b067974d`; remote publication and Windows working-tree application are separate from content preparation.
