#!/usr/bin/python3

import sys

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    test_string = 'XMAS'

    with open(input_filepath, mode='r') as input:
        matrix = [line[:-1] for line in input.readlines()]
        n = len(matrix)
        m = len(matrix[0])
        counter = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 'X':
                    continue
                # down-right diagonal
                if i <= n - 4 and j <= m - 4:
                    counter += int(test_string == ''.join([matrix[i + k][j + k] for k in range(0, 4)]))

                # right
                if j <= m - 4:
                    counter += int(test_string == ''.join([matrix[i][j + k] for k in range(0, 4)]))

                # down
                if i <= n - 4:
                    counter += int(test_string == ''.join([matrix[i + k][j] for k in range(0, 4)]))

                # up-left diagonal
                if i >= 3 and j >= 3:
                    counter += int(test_string == ''.join([matrix[i - k][j - k] for k in range(0, 4)]))

                # up 
                if i >= 3:
                    counter += int(test_string == ''.join([matrix[i - k][j] for k in range(0, 4)]))

                # left 
                if j >= 3:
                    counter += int(test_string == ''.join([matrix[i][j - k] for k in range(0, 4)]))

                # up-right diagonal
                if i >= 3 and j <= n - 4:
                    counter += int(test_string == ''.join([matrix[i - k][j + k] for k in range(0, 4)]))

                # down-left diagonal
                if i <= n - 4 and j >= 3:
                    counter += int(test_string == ''.join([matrix[i + k][j - k] for k in range(0, 4)]))
        print(counter)

if __name__ == "__main__":
    main()
