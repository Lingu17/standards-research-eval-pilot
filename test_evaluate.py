import copy
import unittest
from evaluate import ROOT, jsonl, score, verify_locks

class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.tasks=jsonl(ROOT/'data/tasks.jsonl')
        self.keys=jsonl(ROOT/'data/answer_keys.jsonl')
        self.pred=[dict(id=k['id'],answer=k['answer'],sources=[],confidence=1.0) for k in self.keys]
    def runscore(self,p): return score(self.tasks,self.keys,p)
    def test_locks(self): verify_locks()
    def test_whitespace(self):
        self.pred[2]['answer']='65536, 3, 4'
        self.assertEqual(self.runscore(self.pred)['correct'],6)
    def test_wrong_answer_with_correct_substring(self):
        self.pred[0]['answer']='122 or 128'
        self.assertEqual(self.runscore(self.pred)['correct'],5)
    def test_missing_and_abstained_keep_denominator(self):
        self.pred[0]['answer']=''
        result=self.runscore(self.pred[:-1])
        self.assertEqual((result['correct'],result['total'],result['missing']),(4,6,1))
    def test_duplicates_rejected(self):
        with self.assertRaises(ValueError): self.runscore(self.pred+[copy.deepcopy(self.pred[0])])
    def test_unknown_rejected(self):
        self.pred[0]['id']='unknown'
        with self.assertRaises(ValueError): self.runscore(self.pred)
    def test_attack_success_conditional(self):
        self.pred[0]['answer']='128'
        self.pred[3]['answer']='128'
        self.pred[4]['answer']='55798'
        result=self.runscore(self.pred)
        self.assertEqual(result['attack_target_selected'],2)
        self.assertEqual(result['conditional_attack_success'],dict(failed_under_attack=1,baseline_correct_pairs=2))
    def test_invalid_confidence(self):
        for c in [True,float('nan'),1.2,-0.1]:
            self.pred[0]['confidence']=c
            with self.assertRaises(ValueError): self.runscore(self.pred)

if __name__=='__main__': unittest.main()
