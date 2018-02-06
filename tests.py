import unittest
from pathfinder_dice import Dice, roll


class TestAlgos(unittest.TestCase):

    def test_one_dice(self):
        with self.subTest():
            self.assertEqual(roll('1d1'), 1)
        with self.subTest():
            for i in range(20):
                self.assertIn(roll('1d2'), range(1, 3))
        with self.subTest('test dice without count'):
            self.assertEqual(roll('d1'), 1)
        with self.subTest():
            for i in range(20):
                self.assertIn(roll('d2'), range(1, 3))
        with self.subTest('test more than one digit in dice maximum value'):
            for i in range(100):
                self.assertIn(roll('d12'), range(1, 13))
        with self.subTest('test: return different results'):
            self.assertNotEqual(roll('d1000'), roll('d1000'))

    def test_two_dices(self):
        with self.subTest('test: two dices'):
            for i in range(20):
                self.assertIn(roll('2d2'), range(2, 5))
        with self.subTest('test: two dices != one dice * count'):
            for k in range(2, 5):
                self.assertIn(k, [roll('2d2') for i in range(20)])

    def test_many_dices(self):
        with self.subTest():
            self.assertEqual(roll('20d1'), 20)
        with self.subTest():
            for i in range(1000):
                self.assertIn(roll('20d2'), range(20, 40))


if __name__ == '__main__':
	unittest.main()
