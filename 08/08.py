def taller(h, blockers):
    for b in blockers:
        if b >= h:
            return False
    return True

def visible(i, j, input):
    h = input[i][j]
    if taller(h, input[i][:j]) or taller(h, input[i][j+1:]) or taller(h, [input[x][j] for x in range(i)]) or taller(h, [input[x][j] for x in range(i+1, len(input))]):
        return True
    return False

def part1(input):
    visibles = 0

    for i, line in enumerate(input):
        for j in range(len(line)):
            if visible(i, j, input):
                visibles += 1
    
    print(visibles)

def viewingDistance(h, trees):
    for i, t in enumerate(trees):
        if t >= h:
            return i+1
    return len(trees)


def scenicness(i, j, input):
    h = int(input[i][j])
    return viewingDistance(h, (input[i][:j])[::-1]) * viewingDistance(h, input[i][j+1:]) * viewingDistance(h, [input[x][j] for x in range(i)][::-1]) * viewingDistance(h, [input[x][j] for x in range(i+1, len(input))])


def part2(input):
    mostScenic = 0

    for i, line in enumerate(input):
        for j in range(len(line)):
            if scenicness(i, j, input) > mostScenic:
                mostScenic = scenicness(i, j, input)
    print(mostScenic)
    

if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = [[int(c) for c in list(line.strip())] for line in f.readlines()]

    part1(input_lines)
    part2(input_lines)
