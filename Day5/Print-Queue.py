#!/usr/bin/python3

import sys

def isCorrectReport(rules: dict[int, list[int]], numbers: list[int]) -> bool:
    ocurrence_list = [0] * 100

    for num in numbers:
        ocurrence_list[num] += 1
        if num in rules:
            if any([ocurrence_list[x] > 0 for x in rules[num]]):
                return False

    return True 


def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:

        rules_dict = {}
        # Read rules
        for rule in input:
            if not rule.strip():
                break
            key, val = map(int, rule.strip().split('|'))
            if key not in rules_dict:
                rules_dict[key] = [val]
            else:
                rules_dict[key].append(val)

        sum_of_middles = 0
        # Process data
        for line in input:
            numbers = list(map(int, line.strip().split(',')))
            if isCorrectReport(rules_dict, numbers):
                sum_of_middles += numbers[len(numbers) // 2]
        print(sum_of_middles)
                    
if __name__ == "__main__":
    main()
