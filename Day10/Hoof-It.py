#!/usr/bin/python3

import sys

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

def scoreTrailhead(topo_map, starting_point: Vec2):
    visited = [[False] * len(topo_map[0]) for _ in topo_map]
    stack = [starting_point]
    visited[starting_point.y][starting_point.x] = True
    counter = 0
    while len(stack) > 0:
        pos = stack.pop()
        visited[pos.y][pos.x] = True
        val = int(topo_map[pos.y][pos.x])
        if val == 9:
            counter += 1
        for dir in [Vec2(1,0), Vec2(0,1), Vec2(-1,0), Vec2(0,-1)]:
            if int(topo_map[pos.y + dir.y][pos.x + dir.x]) - val == 1 and not visited[pos.y + dir.y][pos.x + dir.x]:
                stack.append(Vec2(pos.x + dir.x, pos.y + dir.y))
    return counter

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    topo_map = []
    starting_points = []
    with open(input_filepath, mode='r') as input:
        m = 0
        for i, row in enumerate(input):
            row = row.strip()
            if m == 0:
                m = len(row) + 2
            topo_map.append(['-1'] + list(row) + ['-1'])
            for j in range(len(row)):
                if row[j] == '0':
                    starting_points.append(Vec2(j + 1, i + 1))
        topo_map.insert(0, ['-1'] * m)
        topo_map.append(['-1'] * m)

    trailhead_sum = sum([scoreTrailhead(topo_map, point) for point in starting_points]) 
    print(trailhead_sum)

if __name__ == "__main__":
    main()
