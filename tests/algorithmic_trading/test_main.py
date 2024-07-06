import unittest
from src.algorithmic_trading.main import *


class ShouldReturnHehe(unittest.TestCase):

    def test_shouldReturnHehe(self):
        result = start()
        self.assertEquals(result, "Hehee")


if __name__ == '__main__':
    unittest.main()
