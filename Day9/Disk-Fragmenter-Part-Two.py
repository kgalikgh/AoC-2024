#!/usr/bin/python3

import sys

class Fragment:
    def __init__(self, val, times):
        self.val = val
        self.times = times

    def __str__(self):
        return ''.join([self.val] * self.times) 

def defragment(fragment_list: list[Fragment]):
    right = len(fragment_list) - 1

    while right > 0:
        left = 0

        while right > 0 and fragment_list[right].val == '.':
            right -= 1

        while left < right and (fragment_list[left].val != '.' or fragment_list[left].times < fragment_list[right].times):
            left += 1

        if left >= right:
            right -= 1
            continue 

        if fragment_list[left].times == fragment_list[right].times:
            t = fragment_list[left].val
            fragment_list[left].val = fragment_list[right].val
            fragment_list[right].val = t
        else:
            diff = fragment_list[left].times - fragment_list[right].times
            fragment_list.insert(left, Fragment(fragment_list[right].val, fragment_list[right].times))
            left += 1
            fragment_list[right+1].val = '.'
            fragment_list[left].times = diff

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
    for char in text:
        occurences = int(char)
        if isFree: 
            if occurences > 0:
                fragment_list.append(Fragment('.', occurences))
            isFree = False
        else:
            if occurences > 0:
                fragment_list.append(Fragment(str(id), occurences))
            id += 1
            isFree = True

    defragment(fragment_list)

    iter = 0
    sum = 0
    for frag in fragment_list:
        for _ in range(frag.times):
            if frag.val != '.':
                sum += iter * int(frag.val)
            iter += 1

    print(sum)

if __name__ == "__main__":
    main()
