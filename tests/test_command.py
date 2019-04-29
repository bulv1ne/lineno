#!/usr/bin/env python
import os
import sys
import unittest
from subprocess import check_output

if sys.version_info[0] == 3:
    from io import StringIO  # noqa: F401
else:
    from cStringIO import StringIO  # noqa: F401


TEST_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_FILE = os.path.join(TEST_DIR, "test_file.txt")


class TestLineno(unittest.TestCase):
    def test_execute_package(self):
        out = check_output(["python", "-m", "lineno", "-l", "2", TEST_FILE]).decode()
        self.assertEqual(out, "Second\n")
