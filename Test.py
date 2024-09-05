import unittest
import Poker


class MyTestCase(unittest.TestCase):
    # Each method should have one blank line before it

#test_Poker1
    def test_Poker1(self):
        self.assertEqual(Poker.check_straight("S4", "S5", "S7"), 0)

    def test_Poker2(self):
        self.assertEqual(Poker.check_straight("S4", "S5", "S6"), 6)

    def test_Poker3(self):
        self.assertEqual(Poker.check_straight("S10", "SJ", "SA"), 0)

    def test_Poker4(self):
        self.assertEqual(Poker.check_straight("S4", "S2", "S3"), 4)

#test_check_3ofa_kind1

    def test_check_3ofa_kind1(self):
        self.assertEqual(Poker.check_3ofa_kind("S4", "S4", "S4"), 4)

    def test_check_3ofa_kind2(self):
        self.assertEqual(Poker.check_3ofa_kind("S5", "S9", "S4"), 0)

    def test_check_3ofa_kind3(self):
        self.assertEqual(Poker.check_3ofa_kind("SA", "SA", "SA"), 14)

    def test_check_3ofa_kind4(self):
        self.assertEqual(Poker.check_3ofa_kind("SA", "S2", "S3"), 0)
    #test_check_royal_flush

    def test_check_royal_flush1(self):
        self.assertEqual(Poker.check_royal_flush("S8", "S4", "S2"), 0)

    def test_check_royal_flush2(self):
        self.assertEqual(Poker.check_royal_flush("SA", "S4", "S2"), 14)

    def test_check_royal_flush3(self):
        self.assertEqual(Poker.check_royal_flush("S9", "S2", "S3"), 0)

    def test_check_royal_flush4(self):
        self.assertEqual(Poker.check_royal_flush("SA", "S4", "S2"), 14)



if __name__ == '__main__':
    unittest.main()

