# In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.
# How many characters need to be processed before the first start-of-packet marker is detected?
def part1(input):
    for i in range(len(input)-3):
        if len(set(input[i:i+4])) == 4:
            print(i+4)
            break

# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
# How many characters need to be processed before the first start-of-message marker is detected?
def part2(input):
    for i in range(len(input)-13):
        if len(set(input[i:i+14])) == 14:
            print(i+14)
            break

if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = f.readlines()

    part1(input_lines[0])
    part2(input_lines[0])