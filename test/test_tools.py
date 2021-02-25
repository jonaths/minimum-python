import os
import sys
import pandas as pd
import unittest
import numpy as np

# para incluir app en el path
testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

# importar aquí librerías locales
# from tools.tools import find_index_among_zeroes

# para poder acceder a los directorios de app
os.chdir(appdir)


class TestTools(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
