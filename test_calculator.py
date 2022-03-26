import sys

import calculator

import unittest

class calculator_test(unittest.TestCase):

    @unittest.skip #skips the condition
    def test_add(self):
        a = 10
        b = 20
        c = calculator.add(a,b)
        self.assertEqual(a+b,c)

    def test_sub(self):
        a = 10
        b = 20
        c = calculator.sub(a,b)
        self.assertEqual(a-b,c)
    @unittest.skipUnless(sys.platform.startswith("linux"),"requries not linux os ") #skip when condition is false
    def test_mul(self):
        a = 10
        b = 20
        c = calculator.mul(a,b)
        self.assertEqual(a*b,c)
    @unittest.skipIf(sys.platform.startswith("win"),"requres not windows Os") #skip when condition is true
    def test_div(self):
        a = 10
        b = 20
        c = calculator.div(a,b)
        self.assertEqual(a/b,c)

if __name__  == "__main__":
    unittest.main()