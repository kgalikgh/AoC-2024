#!/usr/bin/python3

import sys

class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    directions = [Vec2(0,-1), Vec2(1,0), Vec2(0,1), Vec2(-1,0)]

    player_pos = Vec2(0,0)
    room_map = []
    with open(input_filepath, mode='r') as input:
        for i, line in enumerate(input):
            room_map.append(list(line[:-1]))
            j = line.find('^')
            if j != -1:
                player_pos.x = j
                player_pos.y = i

    dir_index = 0
    counter = 0
    out_of_bounds = False
    while not out_of_bounds:
        dir = directions[dir_index]
        while not out_of_bounds and room_map[player_pos.y][player_pos.x] != '#':
            if room_map[player_pos.y][player_pos.x] != 'X':
                counter += 1
                room_map[player_pos.y][player_pos.x] = 'X'
            player_pos.x += dir.x
            player_pos.y += dir.y
            if player_pos.y >= len(room_map) or player_pos.y < 0 or player_pos.x >= len(room_map[0]) or player_pos.x < 0 :
                out_of_bounds = True
        player_pos.x -= dir.x
        player_pos.y -= dir.y

        dir_index = (dir_index + 1) % 4
    print(counter)


if __name__ == "__main__":
    main()
