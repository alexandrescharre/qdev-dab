import unittest
from dab.account import *

class checkWithdrawalUnitTests(unittest.TestCase):
  def test_authorized(self):
    self.assertEqual(checkWithdrawal(600,450), True)
    self.assertEqual(checkWithdrawal(300, 450), False)
    self.assertEqual(checkWithdrawal(999, 501), False)
    self.assertRaises(ValueError, checkWithdrawal, -1)

if __name__ == '__main__':
  unittest.main()
