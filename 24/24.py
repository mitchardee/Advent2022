import copy

def progress(blizzards, input):
    for bliz in blizzards:
        match bliz[2]:
            case 0:
                if bliz[0]==1:
                    bliz[0] = len(input)-2
                else:
                    bliz[0] -= 1  
            case 1:
                if bliz[0]==len(input)-2:
                    bliz[0] = 1
                else:
                    bliz[0] += 1
            case 2:
                if bliz[1] == len(input[0])-2:
                    bliz[1] = 1  
                else: bliz[1] += 1
            case 3:
                if bliz[1]==1:
                    bliz[1] = len(input[0])-2  
                else:
                     bliz[1] -= 1


def printBoard(blizzards, input):
    dirs = ['^','v','>','<']

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            pr = '.'
            if c == '#':
                pr = '#'
            d = list(filter(lambda x: x[0] == i and x[1] == j, blizzards))
            if len(d)>1:
                pr = repr(len(d))
            if len(d)==1:
                pr = dirs[d[0][2]]
            print(pr, end='')
        print('')

def blizEqual(bliz1, bliz2):
    if len(bliz1) != len(bliz2):
        return False
    for b in bliz1:
        if b not in bliz2:
            return False
    return True

def findPeriod(blizzards, input):

    cop = copy.deepcopy(blizzards)
    for i in range(len(input)*len(input[0])):
        progress(cop, input)
        if blizEqual(cop, blizzards):
            return i

def printCube(cube):
    for i, page in enumerate(cube):
        print('\n',i)
        for line in page:
            print(line)

def makeBigCube(input):
    blizzards = []
    dirs = ['^','v','>','<']
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c in dirs:
                blizzards.append([i,j,dirs.index(c)])

    bigCube = [[[-1 if input[i][j] == '#' else 0 for j in range(len(input[0]))] for i in range(len(input))] for _ in range(findPeriod(blizzards, input)+1)]

    for bliz in blizzards:
            bigCube[0][bliz[0]][bliz[1]] = -1
    for i in range(1, len(bigCube)+1):
        progress(blizzards, input)

        for bliz in blizzards:
            bigCube[i%len(bigCube)][bliz[0]][bliz[1]] = -1
    return bigCube


def traverseTheStorm(bigCube, start, goal, startTime):
    walkersQueue = [start]
    dirs = [(0,0),(0,1),(0,-1),(1,0),(-1,0)]
    i = startTime

    while True:
        i += 1
        newQ = []

        for walker in walkersQueue:
            for dir in dirs:
                y,x = walker[0] + dir[0], walker[1] + dir[1]
                if y in range(len(bigCube[0])) and x in range(len(bigCube[0][0])):
                    if bigCube[i % len(bigCube)][y][x] in range (startTime+1):
                         bigCube[i % len(bigCube)][y][x] = i
                         newQ.append((y,x))
                         if (y,x) == goal:
                            print('got there in ', i, '!')
                            return i

        walkersQueue = newQ

def part1(input):
    bigCube = makeBigCube(input)

    traverseTheStorm(bigCube, (0,1), (len(input)-1, len(input[0])-2), 0)


def part2(input):
    bigCube = makeBigCube(input)

        
    leg1 = traverseTheStorm(copy.deepcopy(bigCube), (0,1), (len(input)-1, len(input[0])-2), 0)
    
    leg2 = traverseTheStorm(copy.deepcopy(bigCube), (len(input)-1, len(input[0])-2), (0,1), leg1)

    traverseTheStorm(copy.deepcopy(bigCube), (0,1), (len(input)-1, len(input[0])-2), leg2)





if __name__ == '__main__':
    inputFile = []
    infile = './input.txt'
    with open(infile) as f:
        inputFile = [line.strip() for line in f]

    part1(inputFile)

    part2(inputFile)
