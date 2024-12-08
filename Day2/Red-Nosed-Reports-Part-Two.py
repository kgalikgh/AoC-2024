#!/usr/bin/python3

import sys

def diffsAreSmall(numbers: list[int]) -> bool:
    for i in range(0, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def isOrdered(numbers: list[int], order_function) -> bool:
    for i in range(0, len(numbers) - 1):
        if not order_function(numbers[i], numbers[i+1]):
            return False
    return True

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        safe_counter = 0
        less_safe_counter = 0
        
        for line in input:
            numbers = [int(x) for x in line.split()]

            if len(numbers) == 1:
                safe_counter+=1
                continue

            for i in range(len(numbers)):
                modified_numbers = numbers[:i] + numbers[i+1:]
                if diffsAreSmall(modified_numbers) and (isOrdered(modified_numbers, lambda x,y: x < y) or isOrdered(modified_numbers, lambda x,y: x > y)):
                    less_safe_counter += 1
                    break
        print(less_safe_counter)

if __name__ == "__main__":
    main()
