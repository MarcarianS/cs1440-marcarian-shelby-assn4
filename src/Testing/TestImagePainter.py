import unittest

from ImagePainter import ImagePainter


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestImagePainter(unittest.TestCase):
    def setUp(self):
        self.image = ImagePainter(512, '#ffffff')
    def test_calculateColor(self):
        # Tests mandelbrot values
        self.assertEqual(self.image.calculateColor(complex(0.0, 0.0), complex(0.0, 0.0)), '#002277')
        self.assertEqual(self.image.calculateColor(complex(-0.2, 1.1075), complex(0.0, 0.0)), '#fff797')
        self.assertEqual(self.image.calculateColor(complex(-0.751, 1.1075), complex(0.0, 0.0)), '#ffe7ae')
        self.assertEqual(self.image.calculateColor(complex(-0.75, 0.1075), complex(0.0, 0.0)), '#95ff51')
        self.assertEqual(self.image.calculateColor(complex(-0.748, 0.1075), complex(0.0, 0.0)), '#00f970')
        self.assertEqual(self.image.calculateColor(complex(-0.7562500000000001, 0.078125), complex(0.0, 0.0)), '#51ff36')
        self.assertEqual(self.image.calculateColor(complex(-0.7562500000000001, -0.234375), complex(0.0, 0.0)), '#fcff8d')
        self.assertEqual(self.image.calculateColor(complex(0.3374999999999999, -0.625), complex(0.0, 0.0)), '#fffb94')
        self.assertEqual(self.image.calculateColor(complex(-0.6781250000000001, -0.46875), complex(0.0, 0.0)), '#9dff54')
        self.assertEqual(self.image.calculateColor(complex(0.4937499999999999, -0.234375), complex(0.0, 0.0)), '#ffeaa8')
        self.assertEqual(self.image.calculateColor(complex(0.3374999999999999, 0.546875), complex(0.0, 0.0)), '#ccff6c')

        # Tests julia values
        self.assertEqual(self.image.calculateColor(complex(0.0, 0.0), complex(-1.0, 0.0)), '#009cb3')
        self.assertEqual(self.image.calculateColor(complex(-0.751, 1.1075), complex(-1.0, 0.0)), '#ffe4b5')
        self.assertEqual(self.image.calculateColor(complex(-0.2, 1.1075), complex(-1.0, 0.0)), '#ffe4b5')
        self.assertEqual(self.image.calculateColor(complex(-0.75, 0.1075), complex(-1.0, 0.0)), '#009cb3')
        self.assertEqual(self.image.calculateColor(complex(-0.748, 0.1075), complex(-1.0, 0.0)), '#009cb3')
        self.assertEqual(self.image.calculateColor(complex(-0.7562500000000001, 0.078125), complex(-1.0, 0.0)), '#009cb3')
        self.assertEqual(self.image.calculateColor(complex(-0.7562500000000001, -0.234375), complex(-1.0, 0.0)), '#ffeda4')
        self.assertEqual(self.image.calculateColor(complex(0.3374999999999999, -0.625), complex(-1.0, 0.0)), '#ffe7ae')
        self.assertEqual(self.image.calculateColor(complex(-0.6781250000000001, -0.46875), complex(-1.0, 0.0)), '#ffe7ae')
        self.assertEqual(self.image.calculateColor(complex(0.4937499999999999, -0.234375), complex(-1.0, 0.0)), '#fff797')
        self.assertEqual(self.image.calculateColor(complex(0.3374999999999999, 0.546875), complex(-1.0, 0.0)), '#ffe9ab')

if __name__ == '__main__':
    unittest.main()


