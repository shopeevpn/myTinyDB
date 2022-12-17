"""unittests"""

import unittest
from my_tinydb import TestGenerator
#TODO:: find out how to fix can't find module error on import


class TestGenerator(unittest.TestCase):
    def test_error(self):
        self.assertRaises(TypeError, generator.generate_password, 2)

if __name__ == "__main__":
    unittest.main()
