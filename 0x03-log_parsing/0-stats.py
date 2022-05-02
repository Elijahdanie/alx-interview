#!/usr/bin/python3
"""
This module parses logs from the stdout
"""
import sys
from typing import OrderedDict


def parseline(line):
    """
    This function parses a line from
    the stdout
    """
    try:
        parsed = {}
        temp = line.split(' ')
        if len(temp) == 9:
            parsed['fileSize'] = int(temp[8])
            parsed['code'] = temp[7]
        else:
            parsed['fileSize'] = int(temp[6])
            parsed['code'] = temp[5]
        return parsed
    except Exception as e:
        return None


def print_stats(fileSize, map_):
    """
    prints info on error
    """
    map_sorted = OrderedDict(sorted(map_.items()))
    print('File size: {}'.format(fileSize))
    [print('{}: {}'.format(i[0], i[1])) for i in map_sorted.items()]


if __name__ == '__main__':
    """
    Entry point for the code
    """
    aggregate = 0
    fileSize = 0
    map_ = {}
    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parseline(line)
            if parsed is not None:
                aggregate += 1
                fileSize += parsed['fileSize']
                code_key = parsed['code']
                if code_key in map_.keys():
                    map_[code_key] += 1
                elif code_key.isdigit():
                    map_[code_key] = 1
                srt = OrderedDict(sorted(map_.items()))
                if aggregate == 10:
                    print('File size: {}'.format(fileSize))
                    [print('{}: {}'.format(i[0], i[1])) for i in srt.items()]
                    aggregate = 0
        print_stats(fileSize, map_)
    except KeyboardInterrupt:
        print_stats(fileSize, map_)
