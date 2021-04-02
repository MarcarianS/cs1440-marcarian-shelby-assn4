import unittest

from Testing import TestMandelbrot,  TestImagePainter, TestPalette, TestFractalInformation


suite = unittest.TestSuite()
tests = (TestMandelbrot.TestMandelbrot, TestImagePainter.TestImagePainter, TestFractalInformation.TestFractalInformation,
         TestPalette.TestPalette)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
