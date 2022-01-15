import os
import sys
import unittest

# To include app in the path
testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

# Import local libraries here, considering if they are in common or inside a
# module in the modules directory
from modules.hello_world.tools.tools import say_hello

# Enables access of the app directories
os.chdir(appdir)


class TestTools(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertTrue(True)

    def test_say_hello(self):
        r = say_hello('message')
        self.assertIsInstance(r, str)


if __name__ == '__main__':
    unittest.main()
