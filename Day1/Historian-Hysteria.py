#!/usr/bin/python3

import heapq
import sys

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    input = open(input_filepath, mode='r')

    heap_left = []
    heap_right = []

    for line in input.readlines():
        left, right = line.split()
        heap_left.append(int(left))
        heap_right.append(int(right))

    heapq.heapify(heap_left)
    heapq.heapify(heap_right)

    sum = 0
    while(len(heap_left) > 0):
        left_tip = heapq.heappop(heap_left)
        right_tip = heapq.heappop(heap_right)
        sum += abs(left_tip - right_tip)

    print(sum)

if __name__ == '__main__':
    main()
