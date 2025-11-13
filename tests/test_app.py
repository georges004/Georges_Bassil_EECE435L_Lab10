import os
import sys
import unittest

# Add project root to PYTHONPATH
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"),
            "Hello, World from Georges Bassil!"
        )


if __name__ == "__main__":
    unittest.main()
