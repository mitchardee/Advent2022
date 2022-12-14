
def buildCave(x0, y0, x1, y1, cave):
    if(x0!=x1 and y0!=y1):
        raise ValueError('wall is not vertical or horizontal')

    if x0 != x1:
        lower, higher = min([x0, x1]), max([x0, x1])
        for i in range(lower, higher + 1):
            cave[y0][i] = '#'

    else:
        lower, higher = min([y0, y1]), max([y0, y1])
        for i in range(lower, higher + 1):
            cave[i][x0] = '#'
    
def dropSand(cave, abyssY):
    [y, x] = [0, 500]
    while True:
        if y >= abyssY:
            return False

        if cave[y+1][x] == '.':
            y += 1
        elif cave[y+1][x-1] == '.':
            x -= 1
            y += 1
        elif cave[y+1][x+1] == '.':
            x += 1
            y += 1
        else:
            cave[y][x] = 'o'
            return True

def part1(input):
    xCoords, yCoords = [], []
    for wall in input:
        for corner in wall:
            [x, y] = corner.split(',')
            xCoords.append(int(x))
            yCoords.append(int(y))

    xMin, xMax = min(xCoords), max(xCoords)
    yMin, yMax = min(yCoords), max(yCoords)

    abyssY = yMax + 2

    cave = [['.' for _ in range(xMax+3)] for _ in range(yMax + 3)] # random-ish amounts of wiggle-room

    for wall in input:
        for i in range(len(wall) - 1):
            [x0, y0] = wall[i].split(',')
            [x1, y1] = wall[i+1].split(',')
            buildCave(int(x0), int(y0), int(x1), int(y1), cave)


    i = 0

    while True:
        if not dropSand(cave, abyssY):
            for line in cave:
                print(''.join(line[xMin-1:]))
            print(i)
            return
        i += 1

def dropSand2(cave):
    [y, x] = [0, 500]
    while True:
        # print([y,x])
        if cave[y+1][x] == '.':
            y += 1
        elif cave[y+1][x-1] == '.':
            x -= 1
            y += 1
        elif cave[y+1][x+1] == '.':
            x += 1
            y += 1
        else:
            cave[y][x] = 'o'
            if [y,x] == [0, 500]:
                return False
            return True
        
def part2(input):
    xCoords, yCoords = [], []
    for wall in input:
        for corner in wall:
            [x, y] = corner.split(',')
            xCoords.append(int(x))
            yCoords.append(int(y))

    yMax = max(yCoords)

    cave = [['.' for _ in range(500+yMax+4)] for _ in range(yMax + 2)] # Maximum size of sand dune is yHeight on either side of sand opening
    cave.append(['#' for _ in range(500+yMax+4)])

    for wall in input:
        for i in range(len(wall) - 1):
            [x0, y0] = wall[i].split(',')
            [x1, y1] = wall[i+1].split(',')
            buildCave(int(x0), int(y0), int(x1), int(y1), cave)


    i = 0

    while True:
        if not dropSand2(cave):
            for line in cave:
                print(''.join(line[cave[-2].index('o')-1:(-1)*((cave[-2][::-1].index('o'))-1)]))
            print(i+1)
            return
        i += 1


if __name__ == '__main__':
    input = []
    with open('./input.txt') as f:
        input = [line.strip().split(' -> ') for line in f]

    part1(input)
    part2(input)