import unittest
import suma
from nose2.tools import params


class TestSum2(unittest.TestCase):

    @params(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    def test_sum2(self, a):
        self.assertEqual(suma.suma(a, a), (a+a), "Deberia ser 6!")
        self.assertTrue(True)
        self.assertFalse(False)

    @params((1, 2), (2, 3))
    def test_sum3(self, a, b):
        self.assertEqual(suma.suma(a, b), (a + b), "Deberia ser 6!")

    # @params(True, False)
    # def test_true(self, value):
    #     self.assertTrue(value)


if __name__ == "__main__":
    unittest.main()