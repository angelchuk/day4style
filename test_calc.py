import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
	self.assertNotEqual(self.calc.add(1, 4), 8)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
	self.assertNotEqual(self.calc.sub(9, 42), -32)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
	self.assertEqual(self.calc.mul(8, 3), 23)
