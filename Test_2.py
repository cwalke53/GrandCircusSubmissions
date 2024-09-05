import unittest
import Poker


class MyTestCase(unittest.TestCase):
    def test_check_3ofa_kind1(self):
        self.assertEqual(Poker.check_3ofa_kind("S4", "S4", "S4"), 4)

    def test_check_3ofa_kind2(self):
        self.assertEqual(Poker.check_3ofa_kind("S5", "S9", "S4"), 0)

    def test_check_3ofa_kind3(self):
        self.assertEqual(Poker.check_3ofa_kind("SA", "SA", "SA"), 14)

    def test_check_3ofa_kind4(self):
        self.assertEqual(Poker.check_3ofa_kind("SA", "S2", "S3"), 14)


if __name__ == '__main__':
    unittest.main()
