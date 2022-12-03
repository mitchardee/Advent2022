from collections import defaultdict

# To help prioritize item rearrangement, every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def priority(c):
    if(ord(c)>95):
        return ord(c)-96
    else:
         return ord(c)-38

# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?
def part1(input_lines):
    
    total = 0

    for line in input_lines:
        di = defaultdict(lambda:0)
        for i,c in enumerate(line):
            if i < len(line)/2:
                di[c] += 1
            elif di[c] != 0:
                total += priority(c)
                break

    print(total)

#Find the item type that corresponds to the badges of each three-Elf group. 
# What is the sum of the priorities of those item types?
def part2(input_lines):
    total = 0

    for i in range(len(input_lines)//3):
        for c in input_lines[3*i]:
            if c in input_lines[3*i + 1] and c in input_lines[3*i + 2]:
                total += priority(c)
                break
    
    print(total)

if __name__ == '__main__':
    input_lines = []

    with open('./input.txt') as f:
        input_lines = [ line.strip() for line in f ]

    part1(input_lines)
    part2(input_lines)