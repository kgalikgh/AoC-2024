#!/usr/bin/python3

import sys

def searchEquation(numbers, exp_result):
    def searchEquationIter(acc, iter):
        if iter == len(numbers):
            return acc == exp_result 

        curr_num = acc * numbers[iter]
        if curr_num <= exp_result:
            if searchEquationIter(curr_num, iter + 1):
                return True

        curr_num = acc + numbers[iter]
        if curr_num <= exp_result:
            if searchEquationIter(curr_num, iter + 1):
                return True

        return False 

    return searchEquationIter(numbers[0], 1)

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        sum_of_searches = 0
        for line in input:
            tokens = line.split()
            exp_result = int(tokens[0][:-1])
            nums = list(map(int, tokens[1:]))
            if searchEquation(nums, exp_result):
                sum_of_searches += exp_result

        print(sum_of_searches)
            
if __name__ == "__main__":
    main()
