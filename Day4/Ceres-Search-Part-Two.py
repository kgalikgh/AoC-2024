#!/usr/bin/python3

import sys

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        matrix = [line[:-1] for line in input.readlines()]
        n = len(matrix)
        m = len(matrix[0])
        counter = 0
        pattern_to_cycle = 'MSSM'
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if matrix[i][j] != 'A':
                    continue
                ends = ''.join([matrix[i-1][j-1], matrix[i-1][j+1], matrix[i+1][j+1], matrix[i+1][j-1]])
                counter += int(ends in [pattern_to_cycle[i:] + pattern_to_cycle[:i] for i in range(len(pattern_to_cycle))])

        print(counter)

if __name__ == "__main__":
    main()
