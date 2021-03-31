import unittest
from julia_fractal import getColorFromPalette, GRAD, WHITE, f, \
    getFractalName


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):
    def test_colorOfThePixel(self):
        self.assertEqual(getColorFromPalette(complex(0, 0), GRAD), '#009cb3')
        self.assertEqual(getColorFromPalette(complex(-0.751, 1.1075), GRAD), '#ffe4b5')
        self.assertEqual(getColorFromPalette(complex(-0.2, 1.1075), GRAD), '#ffe4b5')
        self.assertEqual(getColorFromPalette(complex(-0.75, 0.1075), GRAD), '#009cb3')
        self.assertEqual(getColorFromPalette(complex(-0.748, 0.1075), GRAD), '#009cb3')
        self.assertEqual(getColorFromPalette(complex(-0.7562500000000001, 0.078125), GRAD), '#009cb3')
        self.assertEqual(getColorFromPalette(complex(-0.7562500000000001, -0.234375), GRAD), '#ffeda4')
        self.assertEqual(getColorFromPalette(complex(0.3374999999999999, -0.625), GRAD), '#ffe7ae')
        self.assertEqual(getColorFromPalette(complex(-0.6781250000000001, -0.46875), GRAD), '#ffe7ae')
        self.assertEqual(getColorFromPalette(complex(0.4937499999999999, -0.234375), GRAD), '#fff797')
        self.assertEqual(getColorFromPalette(complex(0.3374999999999999, 0.546875), GRAD), '#ffe9ab')

    def test_dictionaryGetter(self):
        self.assertIsNone(getFractalName('absent'))
        self.assertIsNotNone(getFractalName('fulljulia'))
        self.assertIsNone(getFractalName(''))
        self.assertIsNotNone(getFractalName('lakes'))
        self.assertIsNone(getFractalName('Still Not In Here'))
        self.assertIsNotNone(getFractalName('hourglass'))


if __name__ == '__main__':
    unittest.main()
