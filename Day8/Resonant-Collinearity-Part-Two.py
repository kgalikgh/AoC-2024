#!/usr/bin/python3

import sys

antinodes_list = []
def findAntinodes(begin, move_vec, n, m):
    curr = begin
    while curr[0] >= 0 and curr[0] < n and curr[1] >= 0 and curr[1] < m:
        if curr not in antinodes_list:
            antinodes_list.append(curr)
        curr = (curr[0] + move_vec[0], curr[1] + move_vec[1])


def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    antennas_dict = {}
    n = m = 0
    with open(input_filepath, mode='r') as input:
        lines = input.readlines()
        n = len(lines)
        m = len(lines[0][:-1])
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                if char != '.':
                    if char not in antennas_dict:
                        antennas_dict[char] = [(i,j)]
                    else:
                        antennas_dict[char].append((i,j))

    #print(antennas_dict)

    for key in antennas_dict:
        combinations = []
        for x in antennas_dict[key]:
            for y in antennas_dict[key]:
                if x != y and not any((y,x) == pair for pair in combinations):
                    combinations.append((x,y))
        for (p1,p2) in combinations:
            vec = (p1[0] - p2[0], p1[1] - p2[1])
            inv_vec = (-vec[0], -vec[1])
            findAntinodes(p1, vec, n, m)
            findAntinodes(p2, inv_vec, n, m)
    print(len(antinodes_list))

if __name__ == "__main__":
    main()
