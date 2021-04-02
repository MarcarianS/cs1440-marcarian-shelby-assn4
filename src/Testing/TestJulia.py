import unittest
from Julia import Julia


class TestJulia(unittest.TestCase):
    def test_getIteration(self):
        self.assertEqual(Julia().getIteration(complex(0, 0), complex(-1.0, 0.0), 96), 77)
        self.assertEqual(Julia().getIteration(complex(-0.751, 1.1075), complex(-1.0, 0.0), 96), 0)
        self.assertEqual(Julia().getIteration(complex(-0.2, 1.1075), complex(-1.0, 0.0), 96), 0)
        self.assertEqual(Julia().getIteration(complex(-0.75, 0.1075), complex(-1.0, 0.0), 96), 77)
        self.assertEqual(Julia().getIteration(complex(-0.748, 0.1075), complex(-1.0, 0.0), 96), 77)


if __name__ == '__main__':
    unittest.main()
