#!/usr/bin/python3

import sys

def defragment(disk_map):
    left = 0
    right = len(disk_map) - 1
    while left < right:
        while disk_map[left] != '.':
            left += 1
        while disk_map[right] == '.':
            right -= 1 
        if left >= right:
            break

        t = disk_map[left]
        disk_map[left] = disk_map[right]
        disk_map[right] = t

    return disk_map


def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    text = ''
    with open(input_filepath, mode='r') as input:
        text = input.read().strip()
    
    disk_map = [] 
    id = 0
    isFree = False
    for char in text:
        occurences = int(char)
        if isFree: 
            disk_map.extend(occurences * ['.']) 
            isFree = False
        else:
            disk_map.extend(occurences * [id])
            id += 1
            isFree = True

    defragmented = defragment(disk_map)
    sum = 0
    for i, char in enumerate(defragmented):
        if char == '.':
            break
        sum += i * char 
    print(sum)

if __name__ == "__main__":
    main()
