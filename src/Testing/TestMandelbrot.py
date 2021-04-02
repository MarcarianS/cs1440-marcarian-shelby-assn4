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


if __name__ == '__main__':
    unittest.main()
