#!/usr/bin/python3

import re
import sys

def calcTokens(a, b, prize) -> int:
    print(f'{a} {b} {prize}')


    counter = 0
    cost = 0
    while prize[0] % b[0] != 0 or prize[1] % b[1] != 0 or prize[0] // b[0] != prize[1] // b[1] or prize[0] // b[0] > 100:
        prize[0] -= a[0]
        prize[1] -= a[1]
        # edge case, couldn't find the answer 
        counter += 1
        if counter > 100 or prize[0] < 0 or prize[1] < 0:
            return 0

        cost += 3

    return cost + prize[0] // b[0]

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    button_pattern = r"^.*X\+(\d+),.*Y\+(\d+).*$"
    prize_pattern = r"^.*X=(\d+),.*Y=(\d+).*$"

    with open(input_filepath, mode='r') as input:
        lines = input.readlines() 
        res = 0
        for i in range(0, len(lines), 4):
            a = re.match(button_pattern, lines[i])
            b = re.match(button_pattern, lines[i+1])
            prize = re.match(prize_pattern, lines[i+2])
            if a is None or b is None or prize is None:
                raise KeyError("regex fucked")
            a = list(map(int, a.groups()))
            b = list(map(int, b.groups()))
            prize = list(map(int, prize.groups()))
            res += calcTokens(a, b, prize)
            # print(calcTokens(a, b, prize))
        print(res)

if __name__ == "__main__":
    main()
