#!/usr/bin/python3
"""
This module parses logs from the stdout
"""
import fileinput


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


if __name__ == '__main__':
    """
    Entry point for the code
    """
    aggregate = 0
    fileSize = 0
    code_map = {}
    for line in fileinput.input():
        line = line.strip()
        parsed = parseline(line)
        if parsed is not None:
            aggregate += 1
            fileSize += parsed['fileSize']
            code_key = parsed['code']
            if code_key in code_map.keys():
                code_map[code_key] += 1
            else:
                code_map[code_key] = 1
            code_map = dict(sorted(code_map.items()))
            if aggregate == 10:
                print('File Size: {}'.format(fileSize))
                [print('{}: {}'.format(i[0], i[1])) for i in code_map.items()]
                code_map = {}
                fileSize = 0
                aggregate = 0
