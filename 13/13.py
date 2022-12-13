import functools

class Lizst:

    def __init__(self, lines):
        self.items = []
        self.isDecoder = lines in ['[[2]]', '[[6]]']
        if isinstance(lines, int):
            self.items.append(lines)
        else:
            self.parseLine(lines[1:-1])

    def __repr__(self):
        return '[' + ','.join(map(str, self.items)) + ']'

    def parseLine(self, line):
        # open-closed brackets case
        if line == '':
            return

        try:
            separatorInd = line.index(',') 
        except ValueError:
            separatorInd = len(line)

        if str(line[:separatorInd]).isnumeric():
            self.items.append(int(line[:separatorInd]))
            self.parseLine(line[separatorInd+1:]) # recurse with items after comma
            return
            
        else: #should need to be a '['
            opens = 0
            for i, c in enumerate(line):
                if c == '[':
                    opens += 1
                elif c == ']':
                    opens -= 1
                if opens == 0:
                    self.items.append(Lizst(line[:i+1]))
                    self.parseLine(line[i+2:]) # after the close bracket
                    return



def order(i1, i2):
    if isinstance(i1, int) and isinstance(i2, int):
        if i1<i2:
            return -1
        if i1 > i2:
            return 1
        return 0

    list1 = i1 if isinstance(i1, Lizst) else Lizst(i1)
    list2 = i2 if isinstance(i2, Lizst) else Lizst(i2)

    for i, item in enumerate(list1.items):
        if i == len(list2.items):
            return 1
        match order(item, list2.items[i]):
            case -1:
                return -1
            case 1:
                return 1
            case other:
                continue

    if len(list1.items) < len(list2.items):
        return -1
    return 0



def part1(input):
    total = 0
    for i in range(len(input)//3):
        if order(Lizst(input[i*3]), Lizst(input[i*3 + 1])) == -1:
            total += i+1
    
    print(total)

def part2(input):
    lists = [Lizst('[[2]]'), Lizst('[[6]]')]
    for i in range(len(input)//3):
       lists.append(Lizst(input[i*3]))
       lists.append(Lizst(input[i*3 + 1]))

    decoder = 1
    for i, list in enumerate(sorted(lists, key=functools.cmp_to_key(order))):
        if list.isDecoder:
            decoder *= (i+1)
    print(decoder)


if __name__ == '__main__':
    input_lines = []
    with open('./input.txt') as f:
        input_lines = [line.strip() for line in f]
    input_lines.append('')

    part1(input_lines)
    part2(input_lines)