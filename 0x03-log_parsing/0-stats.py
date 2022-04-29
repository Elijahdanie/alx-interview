#!/usr/bin/python3
''' parses input from stdin and prints stats '''
import sys
from collections import OrderedDict
from re import search as grep


def print_log(size, map_):
    ''' print to stdout '''
    print("File size: {}".format(size))
    for k, v in map_.items():
        if k and v:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    line_count = total_size = 0
    CODES = [200, 301, 400, 401, 403, 404, 405, 500, None]
    map_ = OrderedDict((k, 0) for k in CODES)
    try:
        for line in sys.stdin:
            status, size = grep(" \d{3} ", line), grep("\d{1,4}$", line)
            status = int(status.group()) if status else None
            map_[status] += 1
            total_size += int(size.group()) if size else 0
            line_count += 1
            if line_count % 10 == 0:
                print_log(total_size, map_)
        print_log(total_size, map_)
    except KeyboardInterrupt:
        print_log(total_size, map_)
