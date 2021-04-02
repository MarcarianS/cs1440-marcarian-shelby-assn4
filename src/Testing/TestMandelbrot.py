import unittest
from Mandelbrot import Mandelbrot

# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):

    def test_pixelsWrittenSoFar(self):
        self.assertEqual(Mandelbrot().pixelsWrittenSoFar(7, 7), 49)
        self.assertEqual(Mandelbrot().pixelsWrittenSoFar(257, 321), 82497)
        self.assertEqual(Mandelbrot().pixelsWrittenSoFar(256, 256), 65536)
        self.assertEqual(Mandelbrot().pixelsWrittenSoFar(100, 100), 10000)
        self.assertEqual(Mandelbrot().pixelsWrittenSoFar(640, 480), 307200)

    def test_getIteration(self):
        self.assertEqual(Mandelbrot().getIteration(complex(0.0, 0.0), complex(0.0, 0.0), 96), 95)
        self.assertEqual(Mandelbrot().getIteration(complex(-0.2, 1.1075), complex(0.0, 0.0), 96), 9)
        self.assertEqual(Mandelbrot().getIteration(complex(-0.751, 1.1075), complex(0.0, 0.0), 96), 2)
        self.assertEqual(Mandelbrot().getIteration(complex(-0.75, 0.1075), complex(0.0, 0.0), 96), 30)

if __name__ == '__main__':
    unittest.main()
