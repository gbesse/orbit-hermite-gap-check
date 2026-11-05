import unittest,math
from orbit_hermite_gap_check.core import run
class DomainTests(unittest.TestCase):
 def test_cubic_exact(self):
  x=run({'states':[{'t':0,'position':[0,0,0],'velocity':[0,0,0]},{'t':2,'position':[8,0,0],'velocity':[12,0,0]}],'queries':[1],'max_gap':3})['queries'][0];self.assertEqual(x['position'],[1,0,0]);self.assertEqual(x['linear_disagreement'],3)
 def test_no_extrapolation(self):
  x=run({'states':[{'t':0,'position':[0,0,0],'velocity':[1,0,0]},{'t':2,'position':[2,0,0],'velocity':[1,0,0]}],'queries':[-1,1,2],'max_gap':1});self.assertEqual([r['status']for r in x['queries']],['outside','gap','observed'])
 def test_duplicate_time(self):
  with self.assertRaises(ValueError):run({'states':[{'t':0,'position':[0]*3,'velocity':[0]*3}]*2,'queries':[],'max_gap':1})
