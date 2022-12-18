
def adjacents(cubes, cube):
    adj = 0
    dirs = [(0,0,-1), (0,0,1), (0,-1,0), (0,1,0), (-1,0,0), (1,0,0)]
    for dir in dirs:
        if (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]) not in cubes:
            adj += 1
    return adj

def surfaceArea(cubes):
    sa = 0
    for cube in cubes:
        sa += adjacents(cubes, cube)
    return sa

def part1(input):
    cubes = set()
    for line in input:
        cubes.add(tuple(map(int, line)))

    print (cubes)

    print(surfaceArea(cubes))

def exposedAdjacents(cubes, cube, exposed, dim):
    exposures = 0
    dirs = [(0,0,-1), (0,0,1), (0,-1,0), (0,1,0), (-1,0,0), (1,0,0)]
    for dir in dirs:
        testT = (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2])
        if (testT[0] in range(dim)) and (testT[1] in range(dim)) and (testT[2] in range(dim)):
            if testT not in cubes and exposed[testT[0]][testT[1]][testT[2]]:
                exposures += 1
    return exposures

def exposedSurfaceArea(cubes, exposed, dim):
    sa = 0
    for cube in cubes:
        sa += exposedAdjacents(cubes, cube, exposed, dim)
    return sa

def part2(input):
    cubes = set()
    for line in input:
        cubes.add(tuple(map(lambda s: int(s)+1, line))) #adjusting up one so there's room to go around, would use xmin for a less easy data set

    minX = min([x for (x,_,_) in cubes])
    maxX = max([x for (x,_,_) in cubes])
    minY = min([y for (_,y,_) in cubes])
    maxY = max([y for (_,y,_) in cubes])
    minZ = min([z for (_,_,z) in cubes])
    maxZ = max([z for (_,_,z) in cubes])

    dim = max(maxX-minX, maxY-minY, maxZ-minZ) + 4

    exposed = [[[False for _ in range(dim)]for _ in range(dim)] for _ in range(dim)]

    reached = [(0,0,0)] # seed djikstra's
    dirs = [(0,0,-1), (0,0,1), (0,-1,0), (0,1,0), (-1,0,0), (1,0,0)]

    while len(reached) > 0:
        newlyReached = []

        for triple in reached:
            for dir in dirs:
                testT = (triple[0] + dir[0], triple[1] + dir[1], triple[2] + dir[2])
                if (testT[0] in range(dim)) and (testT[1] in range(dim)) and (testT[2] in range(dim)):
                    if exposed[testT[0]][testT[1]][testT[2]] == False and testT not in cubes:
                        newlyReached.append(testT)
                        exposed[testT[0]][testT[1]][testT[2]] = True
        
        reached = newlyReached

    
    # for i in range(dim):
    #     for j in range(dim):
    #         for k in range(dim):
    #             if not exposed[i][j][k]:
    #                 print(i, j, k, (i,j,k) in cubes)


    print(exposedSurfaceArea(cubes, exposed, dim))




if __name__ == '__main__':
    input = []
    infile = './input.txt'
    with open(infile) as f:
        input = [line.strip().split(',') for line in f]

    part2(input)
