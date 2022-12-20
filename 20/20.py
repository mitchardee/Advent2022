def part1(input):
    pairs = [[n, i] for i, n in enumerate(input)]
    mappy = [x for x in pairs]

    for pair in pairs:
        ind = mappy.index(pair)
        mappy.pop(ind)
        # print(pair, ind, len(mappy),( ind + pair[0]) % len(mappy))
        mappy.insert((ind + pair[0]) % len(mappy), pair)


    ind0 = None
    for i,x in enumerate(mappy):
        if x[0] == 0:
            ind0 = i
            break

    print(mappy[(ind0+1000) % len(mappy)][0] + mappy[(ind0+2000) % len(mappy)][0] + mappy[(ind0+3000) % len(mappy)][0])

def part2(input):
    pairs = [[n * 811589153, i] for i, n in enumerate(input)]
    mappy = [x for x in pairs]

    for _ in range(10):
        for pair in pairs:
            ind = mappy.index(pair)
            mappy.pop(ind)
            # print(pair, ind, len(mappy),( ind + pair[0]) % len(mappy))
            mappy.insert((ind + pair[0]) % len(mappy), pair)


    ind0 = None
    for i,x in enumerate(mappy):
        if x[0] == 0:
            ind0 = i
            break

    print(mappy[(ind0+1000) % len(mappy)][0] + mappy[(ind0+2000) % len(mappy)][0] + mappy[(ind0+3000) % len(mappy)][0])


if __name__ == '__main__':
    input = []
    infile = './input.txt'
    with open(infile) as f:
        input = [int(line.strip()) for line in f]

    part1(input)
    part2(input)
