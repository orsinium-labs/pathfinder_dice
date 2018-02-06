import unittest
from pathfinder_dice import Dice, roll


class TestAlgos(unittest.TestCase):

    def test_common(self):
        with self.subTest():
            self.assertEqual(roll('1d1'), 1)
        with self.subTest():
            for i in range(20):
                self.assertIn(roll('1d2'), range(1, 3))
        with self.subTest():
            for i in range(20):
                self.assertIn(roll('2d2'), range(2, 5))


if __name__ == '__main__':
	unittest.main()
