#!/usr/bin/python3

import sys

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self) -> int:
        return self.x * 100 + self.y

def findCost(bytes):
    starting_pos = Vec2(0,0)
    stack = [starting_pos]
    cost_dict = {starting_pos : 0}
    visited = {starting_pos : True }
    while len(stack) > 0:
        elem = stack.pop()
        for dir in 




def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        bytes = [Vec2(line[0],line[1]) for line in input]
        if len(bytes) > 1024:
            bytes = bytes[:1023]

    




if __name__ == "__main__":
    main()
