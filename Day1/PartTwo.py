#!/usr/bin/python3

import sys

type countDict = dict[int,int]

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    input = open(input_filepath, mode='r')
    
    left_arr = []
    counting_dict: countDict = {}
    
    for line in input.readlines():
        left, right = line.split()
        left_arr.append(int(left))
        key = int(right)
        if key not in counting_dict.keys():
            counting_dict[key] = 0
        counting_dict[key] += 1

    result = 0
    for item in left_arr:
        if item in counting_dict.keys():
            result += counting_dict[item] * item
    
    print(result)

if __name__ == '__main__':
    main()
