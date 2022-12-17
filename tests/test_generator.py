"""unittests"""

import unittest

from .my_tinydb import generator

#from my_tinydb.generator import generate_password
#from .my_tinydb import generator

class TestGenerator(unittest.TestCase):
    def test_error(self):
        self.assertRaises(TypeError, generator.generate_password, 2)

if __name__ == "__main__":
    unittest.main()
