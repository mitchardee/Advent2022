def moveDir1(walker, maze, instruction):
    if instruction == 'R':
        return (walker[0], walker[1], (walker[2]+1)%4)
    if instruction == 'L':
        return (walker[0], walker[1], (walker[2]-1)%4)

    steps = int(instruction)
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    stepped = (walker[0], walker[1], walker[2])

    for i in range(steps):
        nextSpot = ((stepped[0] + dirs[walker[2]][0]) % len(maze), (stepped[1] + dirs[walker[2]][1]) % len(maze[0]), walker[2])
        # print(i, stepped, nextSpot, maze[nextSpot[0]][nextSpot[1]], '\'')

        while maze[nextSpot[0]][nextSpot[1]] == ' ':
            nextSpot = ((nextSpot[0] + dirs[walker[2]][0]) % len(maze), (nextSpot[1] + dirs[walker[2]][1]) % len(maze[0]), walker[2])
            # print('nS', nextSpot, )

        if maze[nextSpot[0]][nextSpot[1]] == '#':
            return stepped

        stepped = nextSpot
    
    return nextSpot




def part1(input):
    directions = input[-1].strip()
    commands = []
    written = 0
    for i, c in enumerate(directions):
        if c in ['R', 'L']:
            commands.append(directions[written:i])
            commands.append(c)
            written = i+1
        if i == len(directions)-1:
            commands.append(directions[written:])

    longestLine = max([len(line) for line in input[:-2]])
    maze = [[' ' if i >= len(line) - 1 else line[i] for i in range(longestLine)] for line in input[:-2]]


    walker = (0, maze[0].index('.'), 0)

    for com in commands:
        # print(com)
        walker = moveDir1(walker, maze, com)
        # print(walker)

    print('final position: ', walker)
    print('password: ', (1000 * (walker[0]+1)) + (4 * (walker[1]+1)) + walker[2])

        
def mapToEdge(walker):
    match walker[2]:
        case 0:
            if walker[0] in range(0, 50):
                return (149-walker[0], 99, 2)
            if walker[0] in range(50, 100):
                return (49, walker[0] + 50, 3)
            if walker[0] in range(100, 150):
                return (149-walker[0],149, 2)
            else:
                return (149, walker[0]-100, 3)
        case 1:
            if walker[1] in range(0, 50):
                return (0, walker[1]+100, 1)
            if walker[1] in range(50, 100):
                return (walker[1]+100, 49, 2)
            else:
                return (walker[1]-50, 99, 2)
        case 2:
            if walker[0] in range(0, 50):
                return (149-walker[0],0, 0)
            if walker[0] in range(50, 100):
                return (100, walker[0]-50, 1)
            if walker[0] in range(100, 150):
                return (149-walker[0], 50, 0)
            else:
                return (0, walker[0]-100, 1)
        case 3:
            if walker[1] in range(0, 50):
                return (walker[1]+50, 50, 0)
            if walker[1] in range(50, 100):
                return (walker[1]+100, 0, 0)
            else:
                return (199, walker[1]-100, 3)


        
def moveDir2(walker, maze, instruction):
    if instruction == 'R':
        return (walker[0], walker[1], (walker[2]+1)%4)
    if instruction == 'L':
        return (walker[0], walker[1], (walker[2]-1)%4)

    steps = int(instruction)
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    stepped = (walker[0], walker[1], walker[2])

    for i in range(steps):
        nextSpot = ((stepped[0] + dirs[stepped[2]][0]) % len(maze), (stepped[1] + dirs[stepped[2]][1]) % len(maze[0]), stepped[2])

        if maze[nextSpot[0]][nextSpot[1]] == ' ':
            nextSpot = mapToEdge(stepped)

        if maze[nextSpot[0]][nextSpot[1]] == '#':
            return stepped
        else:
            stepped = nextSpot
    
    return nextSpot




def part2(input):
    directions = input[-1].strip()
    commands = []
    written = 0
    for i, c in enumerate(directions):
        if c in ['R', 'L']:
            commands.append(directions[written:i])
            commands.append(c)
            written = i+1
        if i == len(directions)-1:
            commands.append(directions[written:])

    longestLine = max([len(line) for line in input[:-2]])
    maze = [[' ' if i >= len(line) - 1 else line[i] for i in range(longestLine)] for line in input[:-2]]


    walker = (0, maze[0].index('.'), 0)

    for com in commands:
        # print(com)
        walker = moveDir2(walker, maze, com)
        # print(walker)

    print('final position: ', walker)
    print('password: ', (1000 * (walker[0]+1)) + (4 * (walker[1]+1)) + walker[2])






if __name__ == '__main__':
    inputFile = []
    infile = './input.txt'
    with open(infile) as f:
        inputFile = [line for line in f]


    part1(inputFile)
    part2(inputFile)

    for tuple in ([(0, i, 3) for i in range(50, 150)] + \
        [(100, i, 3) for i in range(0, 50)] + \
            [(i, 0, 2) for i in range(100, 200)] + \
                [(i, 50, 2) for i in range(0, 100)] + \
                    [(199, i, 1) for i in range(0, 50)] + \
                        [(149, i, 1) for i in range(50, 100)] + \
                            [(49, i, 1) for i in range(100, 150)] + \
                                [(i, 149, 0) for i in range(0, 50)] + \
                                    [(i, 99, 0) for i in range(50, 150)] + \
                                        [(i, 49, 0) for i in range(150, 200)]):
        nex = mapToEdge(tuple)
        back = mapToEdge((nex[0], nex[1], (nex[2]+2)%4))
        if tuple != (back[0], back[1], (back[2]+2)%4):
            print('error detected', tuple, nex)

