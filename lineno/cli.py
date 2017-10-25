#!/usr/bin/env python

import shutil
import sys
from argparse import ArgumentParser, ArgumentTypeError, FileType
from itertools import chain

if sys.version_info[0] == 3:
    from io import StringIO
else:
    from cStringIO import StringIO


def line_numbers(arg):
    lnos = []
    for lno in map(lambda v: v.split('-'), arg.split(',')):
        try:
            if len(lno) == 1:
                lnos.append((int(lno[0]), int(lno[0])))
            else:
                lnos.append((int(lno[0]), int(lno[1])))
        except Exception:
            raise ArgumentTypeError(
                'Could not parse %s as a line number' % lno
            )
    return lnos


class Range:
    __slots__ = ('out', 'range_begin', 'range_end', 'buffer',)

    def __init__(self, out, range_):
        self.out = out
        self.range_begin, self.range_end = range_
        self.buffer = StringIO()

    def write(self, line, print_immediately):
        if print_immediately:
            self.flush()
            self.out.write(line)
        else:
            self.buffer.write(line)

    def flush(self):
        if not self.buffer.closed:
            self.buffer.seek(0)
            shutil.copyfileobj(self.buffer, self.out)
            self.buffer.close()

    def __contains__(self, other):
        return self.range_begin <= other <= self.range_end


def main(args=None, stdout=sys.stdout):
    parser = ArgumentParser(
        description='Outputs the lines from specified file'
    )
    parser.add_argument(
        '-l', '--line-number', type=line_numbers, required=True,
        action='append', metavar='line_number', dest='line_numbers'
    )
    parser.add_argument('infile', type=FileType('r'), help='File to read from')

    args = parser.parse_args(args)
    ranges = [
        Range(stdout, lnos)
        for lnos in chain.from_iterable(args.line_numbers)
    ]
    with args.infile as infile:
        for current_lineno, line in enumerate(infile, start=1):
            for ri, r in enumerate(ranges[:]):
                if current_lineno in r:
                    r.write(line, ri == 0)
                if ri == 0 and r.range_end <= current_lineno:
                    r.flush()
                    ranges.pop(0)
            if not ranges:
                break
    # In case the file ended but we haven't output everything
    for r in ranges:
        r.flush()


if __name__ == '__main__':
    main()
