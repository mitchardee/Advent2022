def part1(input):
    reg = 1
    held = False
    line_num = 0

    signal_strength = 0

    for i in range(1, 222):
        if i in [20, 60, 100, 140, 180, 220]:
            signal_strength += i * reg

        if input[line_num][0] == 'noop':
            held = False
            line_num += 1
            continue
        elif not held:
            held = True
        else:
            held = False
            reg += int(input[line_num][1])
            line_num += 1

    print(signal_strength)

def part2(input):
    reg = 1
    held = False
    line_num = 0

    image = ''


    for i in range(1, 241):

        if abs(((i-1)%40)-reg)<2:
            image += '#'
        else:
            image += ' '

        if input[line_num][0] == 'noop':
            held = False
            line_num += 1
            continue
        elif not held:
            held = True
        else:
            held = False
            reg += int(input[line_num][1])
            line_num += 1

    for i in range(6):
        print(image[i*40:(i+1)*40])


if __name__ == '__main__':
    input_lines = []
    with open('./input.txt') as f:
        input_lines = [line.strip().split() for line in f if line.strip() != '']

    part1(input_lines)
    part2(input_lines)