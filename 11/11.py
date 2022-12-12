class Monke:

    def __init__(self, lines):
        #print(lines)
        self.items = [int(n.replace(',', '')) for n in lines[1][2:]]
        operation = lines[2][-2]
        c = (lines[2][-1])

        if c=='old':
            self.op = lambda x : (x**2)
        elif operation == '*':
            self.op = lambda x : (x * int(c))
        else:
            self.op = lambda x : (x + int(c))

        self.testMod = int(lines[3][-1])
        self.test = lambda x : (x % self.testMod) == 0
        self.truMonke, self.falseMonke = int(lines[4][-1]), int(lines[5][-1])
        self.inspections = 0

    def throw(self, worryVal, Monkes):
        if self.test(worryVal):
            Monkes[self.truMonke].items.append(worryVal)
        else:
            Monkes[self.falseMonke].items.append(worryVal)

    def print(self):
        print('Inspections:\t',self.inspections, '\nItems:\n',self.items)





def round(Monkes):
    for monke in Monkes:
        while len(monke.items) > 0:
            monke.inspections += 1
            itemVal = monke.op(monke.items.pop(0))//3
            monke.throw(itemVal, Monkes)
        

def part1(input):
    Monkes = [Monke(input[i*7:i*7+6]) for i in range((len(input)+1)//7)]


    for i in range(20):
        round(Monkes)
    
    for monke in Monkes:
        monke.print()



def round2(Monkes, mod):
    for monke in Monkes:
        while len(monke.items) > 0:
            monke.inspections += 1
            itemVal = monke.op(monke.items.pop(0)) % mod
            monke.throw(itemVal, Monkes)

def part2(input):
    Monkes = [Monke(input[i*7:i*7+6]) for i in range((len(input)+1)//7)]

    mod = 1
    for monke in Monkes:
        mod *= monke.testMod

    for i in range(10000):
        round2(Monkes, mod)
    
    Monkes.sort(key=lambda m : m.inspections)
    for monke in Monkes:
        monke.print()

    print(Monkes[-1].inspections * Monkes[-2].inspections)

if __name__ == '__main__':
    input_lines = []
    with open('./input.txt') as f:
        input_lines = [line.strip().split() for line in f]

    #part1(input_lines)
    part2(input_lines)