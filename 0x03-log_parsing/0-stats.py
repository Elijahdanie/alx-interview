#!/usr/bin/env python3

import fileinput

aggregate: int = 0
fileSize: int = 0
code_map = {}

def parseline(line):
    try:
        parsed = {}
        temp = line.split(' ')
        parsed['fileSize'] = int(temp[8])
        parsed['code'] = temp[7]
        return parsed
    except:
        return None

for line in fileinput.input():
    line = line.strip()
    parsed = parseline(line)
    if parsed != None:
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
