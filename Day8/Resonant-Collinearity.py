#!/usr/bin/python3

import sys

antinodes_list = []
def testAntinode(antinode, n, m):
    if antinode[0] >= 0 and antinode[0] < n and antinode[1] >= 0 and antinode[1] < m and antinode not in antinodes_list:
        antinodes_list.append(antinode)


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
            diff = (p1[0] - p2[0], p1[1] - p2[1])
            antinode1 = (p1[0] + diff[0], p1[1] + diff[1])
            testAntinode(antinode1, n, m)
            antinode2 = (p2[0] - diff[0], p2[1] - diff[1])
            testAntinode(antinode2, n, m)
    print(len(antinodes_list))

if __name__ == "__main__":
    main()
