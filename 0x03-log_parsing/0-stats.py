#!/usr/bin/python3
"""
This module parses logs from the stdout
"""
import sys


def parseline(line):
    """
    This function parses a line from
    the stdout
    """
    try:
        parsed = {}
        temp = line.split(' ')
        parsed['fileSize'] = int(temp[8])
        parsed['code'] = temp[7]
        return parsed
    except Exception as e:
        return None


def print_stats(fileSize, map_):
    """
    prints info on error
    """
    print('File Size: {}'.format(fileSize))
    [print('{}: {}'.format(i[0], i[1])) for i in map_.items()]


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
                else:
                    map_[code_key] = 1
                map_ = dict(sorted(map_.items()))
                if aggregate == 10:
                    print('File Size: {}'.format(fileSize))
                    [print('{}: {}'.format(i[0], i[1])) for i in map_.items()]
                    map_ = {}
                    fileSize = 0
                    aggregate = 0
        print_stats(fileSize, map_)
    except KeyboardInterrupt as e:
        print_stats(fileSize, map_)
