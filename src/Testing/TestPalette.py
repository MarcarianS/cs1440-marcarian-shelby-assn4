import unittest
from Palette import Palette


class TestPalette(unittest.TestCase):
    def setUp(self):
        self.palette = Palette()
    def test_getSize(self):
        self.assertEqual(self.palette.getSize(), 96)

    def test_getColor(self):
        self.assertEqual(self.palette.getColor(0), '#ffe4b5')
        self.assertEqual(self.palette.getColor(95), '#002277')
        self.assertEqual(self.palette.getColor(77), '#009cb3')


if __name__ == '__main__':
    unittest.main()
