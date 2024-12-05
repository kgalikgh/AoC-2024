#!/usr/bin/python3

import sys

def getCorrectedMiddle(rules: dict[int, list[int]], numbers: list[int]) -> int:
    was_corrected = False

    for i, num in enumerate(numbers):
        for j, aux_num in enumerate(numbers[:i]):
            if num in rules and aux_num in rules[num]:
                was_corrected = True
                t = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = t

    print(numbers)
    return numbers[len(numbers) // 2] if was_corrected else 0 


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
            sum_of_middles += getCorrectedMiddle(rules_dict, numbers)
        print(sum_of_middles)
                    
if __name__ == "__main__":
    main()
