#!/usr/bin/env python
import os
import sys
import unittest

from lineno import cli

if sys.version_info[0] == 3:
    from io import StringIO
else:
    from cStringIO import StringIO


TEST_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_FILE = os.path.join(TEST_DIR, "test_file.txt")


class TestLineno(unittest.TestCase):
    def test_single_line(self):
        out = StringIO()
        cli.main(["-l", "2", TEST_FILE], stdout=out)
        self.assertEqual(out.getvalue(), "Second\n")

    def test_file_first_arg(self):
        out = StringIO()
        cli.main([TEST_FILE, "-l", "2"], stdout=out)
        self.assertEqual(out.getvalue(), "Second\n")

    def test_multi_line_args(self):
        out = StringIO()
        cli.main(["-l", "2", "-l", "2", TEST_FILE], stdout=out)
        self.assertEqual(out.getvalue(), "Second\nSecond\n")

    def test_multi_line(self):
        out = StringIO()
        cli.main(["-l", "2-4", TEST_FILE], stdout=out)
        expected = "".join(["Second\n", "Third\n", "Fourth\n"])
        self.assertEqual(out.getvalue(), expected)

    def test_multi_args(self):
        out = StringIO()
        cli.main(["-l", "2,3-4,6-8", TEST_FILE], stdout=out)
        expected = "".join(
            ["Second\n", "Third\n", "Fourth\n", "Sixth\n", "Seventh\n", "Eighth\n"]
        )
        self.assertEqual(out.getvalue(), expected)

        out = StringIO()
        cli.main(["-l", "2,2,1", TEST_FILE], stdout=out)
        expected = "".join(["Second\n", "Second\n", "First\n"])
        self.assertEqual(out.getvalue(), expected)

    def test_last_line(self):
        out = StringIO()
        cli.main(["-l", "11,1", TEST_FILE], stdout=out)
        expected = "".join(["Last\n", "First\n"])
        self.assertEqual(out.getvalue(), expected)
