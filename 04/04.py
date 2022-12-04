# In how many assignment pairs does one range fully contain the other?

def part1(input_lines):
    
    total = 0

    for line in input_lines:
        [l1, u1, l2, u2] = [int(s) for s in line.replace('-',',').split(',')]

        if (l1 <= l2 and u1 >= u2) or (l2 <= l1 and u2 >= u1):
            total += 1

    print(total)
    
# In how many assignment pairs do the ranges overlap?

def part2(input_lines):

    total = 0

    for line in input_lines:
        [l1, u1, l2, u2] = [int(s) for s in line.replace('-',',').split(',')]

        if (l1 <= l2 <= u1 or l1 <= u2 <= u1 or l2 <= l1 <= u2 or l2 <= u1 <= u2):
            total += 1

    print(total)

if __name__ == '__main__':
    input_lines = []

    with open('./input.txt') as f:
        input_lines = [ line.strip() for line in f ]

    part1(input_lines)
    part2(input_lines)