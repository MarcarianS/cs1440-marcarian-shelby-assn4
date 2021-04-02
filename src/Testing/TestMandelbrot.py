import unittest
from Mandelbrot import

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    # def test_colorOfThePixel(self):
    #     self.assertEqual(Mandelbrot.Mandelbrot()._Mandelbrot__makePicture(complex(0, 0), palette), '#002277')
    #     self.assertEqual(colorOfThePixel(complex(-0.751, 1.1075), palette), '#ffe7ae')
    #     self.assertEqual(colorOfThePixel(complex(-0.2, 1.1075), palette), '#fff797')
    #     self.assertEqual(colorOfThePixel(complex(-0.75, 0.1075), palette), '#95ff51')
    #     self.assertEqual(colorOfThePixel(complex(-0.748, 0.1075), palette), '#00f970')
    #     self.assertEqual(colorOfThePixel(complex(-0.7562500000000001, 0.078125), palette), '#51ff36')
    #     self.assertEqual(colorOfThePixel(complex(-0.7562500000000001, -0.234375), palette), '#fcff8d')
    #     self.assertEqual(colorOfThePixel(complex(0.3374999999999999, -0.625), palette), '#fffb94')
    #     self.assertEqual(colorOfThePixel(complex(-0.6781250000000001, -0.46875), palette), '#9dff54')
    #     self.assertEqual(colorOfThePixel(complex(0.4937499999999999, -0.234375), palette), '#ffeaa8')
    #     self.assertEqual(colorOfThePixel(complex(0.3374999999999999, 0.546875), palette), '#ccff6c')

    def test_pixelsWrittenSoFar(self):
        self.assertEqual(Mandelbrot.Mandelbrot().pixelsWrittenSoFar(7, 7), 49)
        self.assertEqual(Mandelbrot.Mandelbrot().pixelsWrittenSoFar(257, 321), 82497)
        self.assertEqual(Mandelbrot.Mandelbrot().pixelsWrittenSoFar(256, 256), 65536)
        self.assertEqual(Mandelbrot.Mandelbrot().pixelsWrittenSoFar(100, 100), 10000)
        self.assertEqual(Mandelbrot.Mandelbrot().pixelsWrittenSoFar(640, 480), 307200)


if __name__ == '__main__':
    unittest.main()
