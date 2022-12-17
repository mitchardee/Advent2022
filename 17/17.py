def spawnBlock(blockNum, highestSettled):

    blks = [[(3,2), (3,3), (3,4), (3,5)], \
        [(3,3),(4,2), (4,3), (4,4), (5,3)], \
        [(3,2), (3,3),(3,4),(4,4),(5,4)], \
        [(3,2), (4,2), (5,2), (6,2)], \
        [(3,2), (3,3), (4,2), (4,3)]]

    return [( i + highestSettled + 1, j) for (i,j) in blks[blockNum%5]]


def printChute(chute, highestSettled, block):
    for i in range(highestSettled+7, -1, -1):
        print(i, '\t', end='')
        for j in range(7):
            if (i, j) in block:
                print('@', end=' ')
            else:
                print(chute[i][j], end=' ')
        print()
    print('\t---------------')

def printChuteH(chute, H, highestSettled, block):
    for i in range(highestSettled+7, highestSettled - H, -1):
        print(i, '\t', end='')
        for j in range(7):
            if (i, j) in block:
                print('@', end=' ')
            else:
                print(chute[i][j], end=' ')
        print()
    print('\t---------------')    

def moveBlock(chute, direction, block):
    match direction:
        case '<':
            for p in block:
                if p[1] < 1 or chute[p[0]][p[1]-1] != '.':
                    return False, block
            return True, [(i, j-1) for (i,j) in block]
        case '>':
            for p in block:
                if p[1] > 5 or chute[p[0]][p[1]+1] != '.':
                    return False, block
            return True, [(i, j+1) for (i,j) in block]
        case 'V':
            for p in block:
                if p[0] == 0 or chute[p[0]-1][p[1]] != '.':
                    return False, block
            return True, [(i-1, j) for (i,j) in block]
        case 'n':
            return False, block


def part1(input, TOTALBLOCKS):
    chute = [['.' for _ in range(7)] for _ in range(4500)]
    highestSettled = 0
    blocksSettled = 0
    blockType = 0
    block = spawnBlock(blockType, highestSettled - 1)
    inputIter = -1

    while True:
        inputIter += 1
        # printChute(chute, highestSettled, block)
        movedLR, block = moveBlock(chute, input[inputIter % len(input)], block)
        # print('movedLR', movedLR)
        # printChute(chute, highestSettled, block)
        movedD, block = moveBlock(chute, 'V', block)
        # print('movedD', movedD)

        if not movedD:
            for (i,j) in block:
                chute[i][j] = '#'
            blocksSettled += 1
            highestSettled = max(highestSettled, max([i for (i, _) in block]))
            blockType += 1
            block = spawnBlock(blockType, highestSettled)

            if blocksSettled >= TOTALBLOCKS:
                break

    print('blocks settled: ', blocksSettled, '\nheight: ', highestSettled + 1)

def rocksHeight(k):
    # print('rocks: ', 15 + 1725*k, 'height:', 2659*k + 19)
    print('rocks: ', 1600 + 1725*k, 'height:', 2659*k + 2469)


def part2(input, TOTALBLOCKS):
    chute = [['.' for _ in range(7)] for _ in range(TOTALBLOCKS*2)]
    highestSettled = 0
    blocksSettled = 0
    blockType = 0
    block = spawnBlock(blockType, highestSettled - 1)
    inputIter = -1

    while True:
        inputIter += 1
        _, block = moveBlock(chute, input[inputIter % len(input)], block)
        movedD, block = moveBlock(chute, 'V', block)
        if not movedD:
            for (i,j) in block:
                chute[i][j] = '#'
            blocksSettled += 1
            highestSettled = max(highestSettled, max([i for (i, _) in block]))
            blockType += 1
            block = spawnBlock(blockType, highestSettled)

            if (blocksSettled-1600)%1725 == 0:
                print(inputIter, blocksSettled, highestSettled + 1)

            if blocksSettled >= TOTALBLOCKS:
                break

    print('blocks settled: ', blocksSettled, '\nheight: ', highestSettled + 1)


    #   This is a partial account of the math used to do regression on the input
    # The height and rocks settled were both cyclical with repeating the input
    # Cycle spacing for rocks was 1725 and 2659 for height (see rocksHeight()),
    # so this math finds a value x := 10^12 (mod 1725) and works from there

    # for i in range(7):
    #     (rocksHeight(i))

    # print((10**12 - 15)%1725)
    # print((10**12 - 15)//1725)
    # rocksHeight((10**12 - 15)//1725)

    # print( (10**12 - 1600) / 1725)

    

if __name__ == '__main__':
    input = ''
    infile = './input.txt'
    with open(infile) as f:
        input = f.readline().strip()

    part2(input, 10000)
