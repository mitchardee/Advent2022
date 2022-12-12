
def updatedDists(pair, heights, dists):
    (i_0, j_0) = pair
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    updated = []

    for dir in dirs:
        (i,j) = (i_0 + dir[0], j_0 + dir[1])
        if i in range(len(dists)) and j in range(len(dists[0])) and dists[i][j] == -1:
            if heights[i][j] <= heights[i_0][j_0] + 1:
                dists[i][j] = dists[i_0][j_0] + 1
                updated.append((i,j))

    return updated
        


def part1(input):
    dists = [[-1 for _ in range(len(input[0]))] for _ in range(len(input))]
    heights = [[ord(input[i][j]) for j in range(len(input[0]))] for i in range(len(input))]
    
    
    queue, end = [], None
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'S':
                queue.append((i, j))
                dists[i][j] = 0
                heights[i][j] = ord('a')
            if c == 'E':
                end = (i, j)
                heights[i][j] = ord('z')

    while True:
        for _ in range(len(queue)):
            queue += updatedDists(queue.pop(0), heights, dists)
        
        if end in queue:
            print(dists)
            print('distance to E:\t', dists[end[0]][end[1]])
            return



def part2(input):
    dists = [[-1 for _ in range(len(input[0]))] for _ in range(len(input))]
    heights = [[ord(input[i][j]) for j in range(len(input[0]))] for i in range(len(input))]
    
    
    queue, end = [], None
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'S' or c == 'a':
                queue.append((i, j))
                dists[i][j] = 0
                heights[i][j] = ord('a')
            if c == 'E':
                end = (i, j)
                heights[i][j] = ord('z')

    while True:
        for _ in range(len(queue)):
            queue += updatedDists(queue.pop(0), heights, dists)
        
        if end in queue:
            print(dists)
            print('distance to E:\t', dists[end[0]][end[1]])
            return


if __name__ == '__main__':
    input_lines = []
    with open('./input.txt') as f:
        input_lines = [line.strip() for line in f]

    part1(input_lines)
    part2(input_lines)