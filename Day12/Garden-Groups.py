#!/usr/bin/python3

import sys
from collections import deque

def exploreRegion(field, visited, queue, start_i, start_j):
    n = len(field)
    m = len(field[0])
    #init region search
    region_name = field[start_i][start_j]
    region_area = 0
    region_perimeter = 0
    region_queue = [(start_i,start_j)]
    #print(f'region name {region_name} starting point {(start_i,start_j)}')

    while len(region_queue) > 0:
        k, l = region_queue.pop()
        if visited[k][l]:
            continue

        visited[k][l] = True
        #print(visited)
        region_area += 1
        common_sides = 0

        #print(f'considering coords ({k},{l}) with val {field[k][l]}, visited {visited[k][l]}')
        for i, j in [(k-1,l), (k+1,l), (k,l-1), (k,l+1)]:
            if i >= 0 and i < n and j >= 0 and j < m:
                #print(f'considering coords ({i},{j}) with val {field[i][j]}, visited {visited[i][j]}')
                
                if field[i][j] == region_name and not visited[i][j]:
                    region_queue.append((i,j))
                elif field[i][j] == region_name and visited[i][j]:
                    #print(f'Added side {i} {j}')
                    common_sides += 1
                elif field[i][j] != region_name and not visited[i][j]:
                    queue.append((i,j))
        region_perimeter += 4 - 2 * common_sides
        #print(f'{region_name} area {region_area}')

    result = region_area * region_perimeter
    return result


def main():
    input_filepath = 'input.txt'
    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    with open(input_filepath, mode='r') as input:
        field = [list(x.strip()) for x in input]     

    sum = 0
    n = len(field)
    m = len(field[0])
    visited = [[False for _ in range(m)] for _ in range(n)] 
    #print(visited)
    queue = deque()
    queue.append((0,0))
    #print(queue)
    while len(queue) > 0:
        i, j = queue.popleft()
        if visited[i][j]:
            continue
        sum += exploreRegion(field, visited, queue, i, j)
        #print(queue)

    print(sum)

if __name__ == "__main__":
    main()
