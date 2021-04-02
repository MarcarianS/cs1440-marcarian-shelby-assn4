import unittest

from Testing import TestMandelbrot, TestPalette, TestFractalInformation, TestJulia


suite = unittest.TestSuite()
tests = (TestMandelbrot.TestMandelbrot, TestJulia.TestJulia, TestFractalInformation.TestFractalInformation,
         TestPalette.TestPalette)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
