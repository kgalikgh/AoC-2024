#!/usr/bin/python3

import re
import sys

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    prog = re.compile(r'(?:(do)\(\))|(?:(don\'t)\(\))|(?:mul\(([0-9]{1,3}),([0-9]{1,3})\))')

    with open(input_filepath, mode='r') as input:
        all_ops = []
        text = input.read()

        all_ops += re.findall(prog, text)

        result = 0
        enabled = True 
        for op in all_ops:
            if op[0] == 'do':
                enabled = True
            elif op[1] == "don't":
                enabled = False
            else:
                if enabled:
                    result += int(op[2]) * int(op[3])

        print(result)


if __name__ == "__main__":
    main()
