# Curation log

## 2026-09-28: Method analysis and index consolidation

Replaced the reading-route introduction and duplicate representative tables with one chronological index per subarea. Milestone contributions now appear within their paper entries. Removed public reading-depth badges and acknowledgments; source-reading provenance remains in the underlying records.

Revised all 42 bilingual method comparisons and added detailed, section-linked mechanisms and experimental notes for 21 papers: ViperGPT, PyVision, MatPlotAgent, WavJourney, SlideCoder, Paper2Poster, CAD-Recode, Real2Code, BlenderAlchemy, CodeAct, Eureka, Voyager, WorldCoder, GIF-MCTS, DeepSeek-Prover-V2, LLM-SR, ScienceAgentBench, DreamCoder, LeanDojo, PAL and FunSearch. The new notes cite the inspected methods, results or examples. The collection remains at 167 papers; this revision prioritizes analysis over additions.

The cross-method page now separates representations, component ablations, reuse settings and evaluation targets. It records the WorldCoder version difference in the GIF-MCTS comparison, the separate data-scale effect in CAD-Recode, and contrasting execution/task-success effects in ScienceAgentBench.

## 2026-09-28: Initial editorial revision

Added bilingual overviews and comparison guidance for all ten areas, plus expanded notes for 42 representative papers. The notes cover input/output, mechanism, feedback and companion papers. The README now introduces program roles before the domain index, and the overview graphic illustrates eight application areas with concrete program outputs.

Paper annotations remain in `data/papers.json`; domain overviews and representative-paper selections are in `data/taxonomy.json`. README files, expanded notes and bibliography exports are generated together. This revision keeps all 167 records, citation keys, first-public dates and reading-depth labels. The extended notes summarize the existing source-reading records and abstract checks; editorial comparisons are labeled as reading takeaways.

Original pages were revisited for ViperGPT, CodeAct, CAD-Recode, WorldCoder, GIF-MCTS, SlideCoder, WavJourney, WavCraft, Code as Policies, Eureka, Voyager, LeanDojo, MatPlotAgent, Paper2Poster, DreamCoder, ReAct, Reflexion and BlenderAlchemy. The reading guide's GIF-MCTS link was corrected to arXiv:2405.15383. The previous URL pointed to the world-model survey.

## 2026-09-28: Initial repository collection

The collection starts from a research dossier whose broad search and selected full-text reading were performed on 2026-09-12/13. Its candidate list contained 204 records and 154 selected references, including two public commentaries and an event-specific technical report.

The public index carries over **151** of those records, excluding the event-specific Navier–Stokes report and its two commentaries. The mathematics section is organized around program-aided reasoning, formal proof and mathematical research systems.

**Sixteen original-source additions** bring the index to **167 records**. Twelve repair historical/topic gaps: NS-VQA, SketchAdapt, ShapeAssembly, DeepCAD, GPT-f, HyperTree Proof Search, Draft/Sketch/Prove, ProgPrompt, Instruct2Act, BlenderAlchemy, SciCode and LL3M. Four recent robot-program papers are Auto-HSI, Learning and Transferring Closed-Loop Robot Software, M³P-R1 and RIVET. Their original arXiv records, authors and abstracts were checked on 2026-09-28; full protocols were not audited, with method and experiment analysis deferred.

The initial section-level records retained their source-check dates and reading locations from the dossier; subsequent checks update individual records. Broad review covers literature through September 13; September 14–28 additions came from targeted searches.

## Search and source trail

The targeted search used title lookups and combinations including `ProgPrompt Instruct2Act robot task plans code`, `ShapeAssembly SketchAdapt neural symbolic VQA`, `Draft Sketch Prove GPT-f SciCode`, `BlenderAlchemy iterative refinement`, and recent robot/code-generation queries. Search results led to original arXiv records, author pages and the reference repository.

Original records for new entries are linked in the [index](../README.md#paper-index); stable keys also resolve in [JSON](../data/papers.json), [BibTeX](../references.bib) and [RIS](../references.ris). Earlier formal publication metadata may still rely on authors' arXiv journal references/comments; their provenance is retained rather than silently upgraded to independent confirmation.

## Editorial choices

The primary hierarchy is domain → concrete task. Cross-domain links use facets. The 21 milestone selections explain specific changes in the role of programs, rather than following a recent-first ranking. Background and complementary systems remain visible, so the collection does not portray all advances in perception, VLA control or neural world models as code-agent results.

The feature columns in [MLLM-Token-Compression](https://github.com/yaolinli/MLLM-Token-Compression) informed the presentation. This collection uses domain-specific method comparisons and source provenance in its structured records.

## Initial verification boundary

Initial checks covered metadata, category membership, duplicate identities, generated-file consistency, local links, candidate parsing and bibliography parsing. One live arXiv query produced five unseen candidates for review. The full eight-query scheduled workflow and an exhaustive live code-link check remain untested. The initial project was prepared against remote base commit `e1a04942966d272567b2c7e78775c9c9b067974d`.
