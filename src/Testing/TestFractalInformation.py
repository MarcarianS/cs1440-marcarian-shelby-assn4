import unittest
import FractalInformation


class TestFractalInformation(unittest.TestCase):
    def setUp(self):
        self.info = FractalInformation.FractalInformation()

    def test_getFractal(self):
        self.assertEqual(self.info.getFractal('fulljulia'), 'fulljulia')
        self.assertEqual(self.info.getFractal('lakes'), 'lakes')
        self.assertEqual(self.info.getFractal('elephants'), 'elephants')
        self.assertIsNone(self.info.getFractal('absent'))
        self.assertIsNone(self.info.getFractal(''))
        self.assertIsNone(self.info.getFractal('Does not exist'))

if __name__ == '__main__':
    unittest.main()
