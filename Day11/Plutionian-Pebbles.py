#!/usr/bin/python3

import sys
from collections import deque 

# 0 -> 1
# .{2x} -> .{x} .{x}
# .{2x+1} -> . * 2024

max_iter = 25 

def processNumber(num) -> int:
    queue = deque()
    queue.append((num, max_iter))
    counter = 1
    while len(queue) > 0:
        num, iters = queue.popleft()
        #print(f'queue size {len(queue)}')
        #print(f'{num} -> {iters} iters')
        for i in range(iters):
            #print(f'Iter {i}. considering num = {num}')
            if int(num) == 0:
                num = '1'
            elif len(num) % 2 != 0:
                num = str(int(num) * 2024)
            else:
                pivot = len(num) // 2
                left = num[:pivot]
                right = num[pivot:]
                num = left
                queue.append((str(int(right)), iters - i - 1))
                #print(f"Added {(str(int(right)), iters - i - 1)} to queue")
                counter += 1
            #print(f'Iter {i}. New num = {num}')
    return counter

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        numbers = list(input.read().split())

    counter = sum([processNumber(num) for num in numbers])

        #print(numbers)
    print(counter)

if __name__ == "__main__":
    main()
