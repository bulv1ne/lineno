#!/usr/bin/env python
import argparse
import unittest

from lineno.cli import line_numbers


class TestLineNumbers(unittest.TestCase):

    def test_single(self):
        self.assertEqual(line_numbers('1'), [(1, 1)])

    def test_comma(self):
        self.assertEqual(line_numbers('1,2'), [(1, 1), (2, 2)])

    def test_range(self):
        self.assertEqual(line_numbers('1-2'), [(1, 2)])

    def test_invalid_line_number(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            line_numbers('abc')
