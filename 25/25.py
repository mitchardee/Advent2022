def digitConvert(c):
    if c in ['0', '1', '2']:
        return int(c)
    if c == '-':
        return -1
    if c == '=':
        return -2

def toDecimal(line):
    val = 0
    for c in line:
        val *= 5
        val += digitConvert(c)
    return val

def snafuConvert(v):
    if v in range(3):
        return str(v)
    if v == -1:
        return '-'
    if v == -2:
        return '='

def toSnafu(val):
    snafu = ''
    while val != 0:
        digit = val % 5
        if digit > 2:
            digit -= 5
        val -= digit

        snafu = snafuConvert(digit) + snafu
        val //= 5
    
    return snafu
        


def part1(input):
    total = 0
    for line in input:
        total += toDecimal(line)

    print(total)

    print(toSnafu(total))



if __name__ == '__main__':
    inputFile = []
    infile = './input.txt'
    with open(infile) as f:
        inputFile = [line.strip() for line in f]

    part1(inputFile)