def declareIntentions(elves, startDir):
    allDirs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1, 0), (1, -1), (0,-1)]
    dirs = [[(-1,-1), (-1,0), (-1,1)], [(1,1), (1, 0), (1, -1)], [(1,-1), (0,-1), (-1,-1)], [(-1,1), (0, 1), (1,1)]]

    
    for elf in elves:
        alone = True
        for dir in allDirs:
            if (elf[0] + dir[0], elf[1] + dir[1]) in elves:
                alone = False
                break
        if alone:
            elves[elf] = elf
            continue

        declared = False
        for lookingDir in range(startDir, startDir + 4):
            canGoDirection = True
            for dir in dirs[lookingDir % 4]:
                if (elf[0] + dir[0], elf[1] + dir[1]) in elves:
                    canGoDirection = False
                    break
            if canGoDirection:
                elves[elf] = (elf[0] + dirs[lookingDir % 4][1][0], elf[1] + dirs[lookingDir % 4][1][1])
                declared = True
                break
        
        if not declared:
            elves[elf] = elf

def move(elves):
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    moved = False

    #check for overlaps
    for elf, intention in elves.items():
        if intention == elf:
            continue
        
        interlopers = list(filter((lambda x: x in elves and elves[x] == intention), [(intention[0] + dir[0], intention[1] + dir[1]) for dir in dirs]))
        if len(interlopers) > 1:
            for intr in interlopers:
                elves[intr] = intr

    itms = list(elves.keys())
    for elf in itms:
        intention = elves.pop(elf)
        if intention != elf:
            moved = True
        elves[intention] = intention
    
    return moved

            
            
def printElves(elves):
    minX, minY = min(x for (_,x) in elves), min(y for (y,_) in elves)
    maxX, maxY = max(x for (_,x) in elves), max(y for (y,_) in elves)
    print()
    for i in range(minY-1, maxY+2):
        for j in range(minX-1, maxX+2):
            print('#' if (i,j) in elves else '.', end='')
        print()


def part1(input):
    elves = {}

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == '#':
                elves[(i,j)] = (i,j)

    for i in range(10):
        declareIntentions(elves, i)
        move(elves)

    printElves(elves)

    minX, minY = min(x for (_,x) in elves), min(y for (y,_) in elves)
    maxX, maxY = max(x for (_,x) in elves), max(y for (y,_) in elves)

    print('unoccupied: ', ((maxX-minX+1)*(maxY-minY+1) - len(elves)))


def part2(input):
    elves = {}

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == '#':
                elves[(i,j)] = (i,j)

    i = 0
    while True:
        declareIntentions(elves, i)
        moved = move(elves)
        if not moved:
            printElves(elves)
            print(i+1)
            return
        i += 1

   

if __name__ == '__main__':
    inputFile = []
    infile = './input.txt'
    with open(infile) as f:
        inputFile = [line.strip() for line in f]

    part1(inputFile)
    part2(inputFile)