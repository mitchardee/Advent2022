def hMove(h, dir):
    moves = {'U': [-1,0], 'D': [1,0], 'L': [0,-1], 'R': [0,1]}
    return [h[0] + moves[dir][0], h[1] + moves[dir][1]]

def tUpdate(h, t):
    xGap, yGap = h[0] - t[0], h[1]-t[1]
    if abs(xGap) == 2 and abs(yGap) == 2:
        return [t[0] + xGap//2, t[1] + (yGap//2)]
    if abs(xGap) == 2:
        return [t[0] + (xGap//2), h[1]]
    if abs(yGap) == 2:
        return [h[0], t[1] + (yGap//2)]
    return t

def part1(input):

    tVisited = set()
    h = [0,0]
    t = [0,0]

    for line in input:
        for _ in range(int(line[1])):
            h = hMove(h, line[0])
            t = tUpdate(h,t)
            tVisited.add(tuple(t))
    print(len(tVisited))

def part2(input):
    tVisited = set()

    knots = [[0,0] for _ in range(10)]

    for line in input:
        for _ in range(int(line[1])):
            knots[0] = hMove(knots[0], line[0])
            for i in range(1,len(knots)):
                knots[i] = tUpdate(knots[i-1], knots[i])
            tVisited.add(tuple(knots[9]))
    
    print(len(tVisited))

if __name__ == '__main__':
    input_lines = []
    with open('./input.txt') as f:
        input_lines = [line.strip().split() for line in f if line.strip() != '']

    part1(input_lines)
    part2(input_lines)