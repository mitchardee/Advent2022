def makeStacks(input):
    stacks = [[] for _ in range(len(input[0])//4)]
    for line in input:
        for i,c in enumerate(line[1::4]):
            if c != ' ':
                stacks[i].append(c)
    return stacks

#moving one crate at a time
def part1(input):
    #reverse stacks for ease of parsing
    stacks = makeStacks(input[input.index('\n')-2::-1])
    moves = input[input.index('\n')+1:]
    
    for line in moves:
        n = int(line.split()[1])
        src = int(line.split()[3]) - 1
        dst = int(line.split()[5]) - 1

        for _ in range(n):
            stacks[dst].append(stacks[src].pop())

    for s in stacks:
        print(s[-1])

#moving n crates at a time
def part2(input):
    #reverse stacks for ease of parsing
    stacks = makeStacks(input[input.index('\n')-2::-1])
    moves = input[input.index('\n')+1:]
    
    for line in moves:
        n = int(line.split()[1])
        src = int(line.split()[3]) - 1
        dst = int(line.split()[5]) - 1

        stacks[dst].extend(stacks[src][-n:])
        del stacks[src][-n:]


    for s in stacks:
        print(s[-1])

#After the rearrangement procedure completes, what crate ends up on top of each stack?
if __name__ == '__main__':
    input_lines = []

    with open('./input.txt') as f:
        input_lines = f.readlines()

    part1(input_lines)
    part2(input_lines)