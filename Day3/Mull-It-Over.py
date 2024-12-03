#!/usr/bin/python3

import re
import sys

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    prog = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')

    with open(input_filepath, mode='r') as input:
        all_ops = []
        for line in input:
            all_ops += re.findall(prog, line)

        result = sum([int(op[0]) * int(op[1]) for op in all_ops]) 
        print(result)

if __name__ == "__main__":
    main()
