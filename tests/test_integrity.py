import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import load
from validate import record_errors,editorial_errors
from discover import parse_feed,merge_candidates,canonical_id

class IntegrityTests(unittest.TestCase):
    def test_detailed_analysis_requires_a_source_and_both_languages(self):
        papers,taxonomy,_=load()
        for field in ['analysis_source','analysis_location_zh','experiment']:
            modified=copy.deepcopy(papers)
            next(p for p in modified if p.get('mechanism'))[field]=''
            with self.subTest(field=field):
                self.assertTrue(any('incomplete sourced analysis' in e for e in record_errors(modified,taxonomy)))

    def test_reading_comparison_cannot_reference_a_missing_paper(self):
        papers,taxonomy,_=load();modified=copy.deepcopy(papers)
        modified[0]['compare_with']=['UnknownPaper']
        self.assertTrue(any('comparison reference' in e for e in record_errors(modified,taxonomy)))

    def test_reading_note_must_be_complete_in_both_languages(self):
        papers,taxonomy,_=load();modified=copy.deepcopy(papers)
        next(p for p in modified if p.get('io'))['feedback_zh']=''
        self.assertTrue(any('incomplete bilingual reading note' in e for e in record_errors(modified,taxonomy)))

    def test_focus_paper_must_resolve_and_belong_to_the_domain(self):
        papers,taxonomy,_=load();modified=copy.deepcopy(taxonomy)
        modified[0]['focus_papers']=['UnknownPaper','Eureka']
        errors=editorial_errors(papers,modified)
        self.assertTrue(any('unknown focus paper' in e for e in errors))
        self.assertTrue(any('primary domain' in e for e in errors))

    def test_duplicate_identifier_is_rejected(self):
        papers,taxonomy,_=load();modified=copy.deepcopy(papers);modified[1]['arxiv_id']=modified[0]['arxiv_id']='2402.01030'
        self.assertTrue(any('duplicate arxiv_id' in e for e in record_errors(modified,taxonomy)))

    def test_milestone_needs_a_reason(self):
        papers,taxonomy,_=load();modified=copy.deepcopy(papers);modified[0]['milestone']=True;modified[0]['milestone_reason']=''
        self.assertTrue(any('unexplained milestone' in e for e in record_errors(modified,taxonomy)))

    def test_versions_and_overlapping_searches_do_not_duplicate(self):
        self.assertEqual(canonical_id('http://arxiv.org/abs/2609.19906v2'),'2609.19906')
        item=dict(arxiv_id='2609.19906',published='2026-09-17',title='Example')
        result=merge_candidates([('robotics',[item]),('tools',[item])],set())
        self.assertEqual(len(result),1);self.assertEqual(result[0]['matched_queries'],['robotics','tools'])
        self.assertEqual(merge_candidates([('robotics',[item])],{'2609.19906'}),[])

    def test_error_feed_cannot_look_like_an_empty_success(self):
        with self.assertRaises(ValueError):parse_feed(b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/api/errors</id></entry></feed>')

    def test_atom_namespaces_and_authors(self):
        raw=b'''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:os="http://a9.com/-/spec/opensearch/1.1/"><os:totalResults>1</os:totalResults><entry><id>http://arxiv.org/abs/2609.19906v1</id><title>A\n program</title><author><name>A. Author</name></author><published>2026-09-17</published></entry></feed>'''
        entries,total=parse_feed(raw);self.assertEqual(total,1);self.assertEqual(entries[0]['title'],'A program');self.assertEqual(entries[0]['authors'],['A. Author'])

if __name__=='__main__':unittest.main()
