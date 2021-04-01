import unittest

from Testing import TestMandelbrot,  TestImagePainter


suite = unittest.TestSuite()
# tests = (TestMandelbrot.TestMandelbrot, TestJulia.TestJulia)
tests = (TestMandelbrot.TestMandelbrot, TestImagePainter.TestImagePainter)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
