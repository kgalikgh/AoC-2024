#!/usr/bin/python3

import sys

def defragment(fragment_list):
    left = 0
    right = len(fragment_list) - 1
    print(fragment_list)
    while fragment_list[left][1] != '.':
        left += 1

    while (fragment_list[right][1] == '.' or fragment_list[right][0] > fragment_list[left][0]) and right > left:
        right -= 1 

    if right <= left:
        right = len(fragment_list) - 1
        left += 1

    if fragment_list[right][0] == fragment_list[left][0]:
        fragment_list[left][1] = fragment_list[right][1]
        fragment_list[right][1] = '.'
    else:
        diff = fragment_list[left][0] - fragment_list[right][0]
        saved_frag = fragment_list[right].copy()
        fragment_list[right][1] = '.'
        fragment_list.insert(left, saved_frag)
        fragment_list[left + 1][0] = diff
        left += 1

    return fragment_list


def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    text = ''
    with open(input_filepath, mode='r') as input:
        text = input.read().strip()
    

    id = 0
    fragment_list = []
    isFree = False
    pos = 0
    for char in text:
        occurences = int(char)
        if isFree: 
            if occurences > 0:
                fragment_list.append([occurences,'.'])
            isFree = False
        else:
            if occurences > 0:
                fragment_list.append([occurences,id])
            id += 1
            isFree = True
        pos += occurences

    defragmented = defragment(fragment_list)
    return 
    sum = 0
    iter = 0
    for fragment in defragmented:
        if fragment[1] != '.':
            for _ in range(fragment[0]):
                sum += fragment[1] * iter
                iter += 1

    print(sum)

if __name__ == "__main__":
    main()
