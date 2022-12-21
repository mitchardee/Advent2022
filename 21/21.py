def part1(input1):

    monkes = {}
    toPop = []

    for i, line in enumerate(input1):
        line[0] = line[0][:-1]

        if len(line) == 2:
            monkes[line[0]] = int(line[1])
            toPop.append(i)


    while(len(input1) > 0):
        for i in toPop[::-1]:
            input1.pop(i)
        toPop = []

        for i, line in enumerate(input1):

            if line[1] in monkes and line[3] in monkes:
                toPop.append(i)
                match line[2]:
                    case '+':
                        monkes[line[0]] = monkes[line[1]] + monkes[line[3]]
                    case '-':
                        monkes[line[0]] = monkes[line[1]] - monkes[line[3]]
                    case '*':
                        monkes[line[0]] = monkes[line[1]] * monkes[line[3]]
                    case '/':
                        monkes[line[0]] = monkes[line[1]] // monkes[line[3]]
                    case other:
                        print('uh oh')

                if line[0] == 'root':
                    print('Found root value: ', monkes['root'])
                    return

def tryHumnValue(monkes, inputTHV):
    while(len(inputTHV) > 0):
        
        toPop = []

        for i, line in enumerate(inputTHV):
            if line[1] in monkes and line[3] in monkes:
                allNumbers = isinstance(monkes[line[1]], int) and isinstance(monkes[line[3]], int)
                toPop.append(i)
                if allNumbers:
                    match line[2]:
                        case '+':
                            monkes[line[0]] = monkes[line[1]] + monkes[line[3]]
                        case '-':
                            monkes[line[0]] = monkes[line[1]] - monkes[line[3]]
                        case '*':
                            monkes[line[0]] = monkes[line[1]] * monkes[line[3]]
                        case '/':
                            monkes[line[0]] = monkes[line[1]] // monkes[line[3]]
                        case other:
                            print('uh oh')
                else:
                    (n, (coeff,b)) = (monkes[line[1]], monkes[line[3]]) if isinstance(monkes[line[1]], int) else (monkes[line[3]], monkes[line[1]])
                    rightN = isinstance(monkes[line[3]], int)

                    match line[2]:
                        case '+':
                            monkes[line[0]] = (coeff, b+n)
                        case '-':
                            monkes[line[0]] = (coeff, b-n) if rightN else (0 - coeff, n-b)
                        case '*':
                            monkes[line[0]] = (coeff*n, b*n)
                        case '/':
                            monkes[line[0]] = (coeff/n, b/n)
                        case other:
                            print('uh oh')

                if line[0] == 'root':
                    return monkes[line[1]], monkes[line[3]]

        if len(toPop) == 0:
            print('no available evaluations found!')
            return
        for i in toPop[::-1]:
            inputTHV.pop(i)


def part2(input2):
    monkes = {}
    toPop = []

    for i, line in enumerate(input2):
        line[0] = line[0][:-1]

        if len(line) == 2:
            monkes[line[0]] = int(line[1])
            toPop.append(i)

    for i in toPop[::-1]:
        input2.pop(i)   

    monkes['humn'] = (1.0,0.0)
     

    # print('got to loop', monkes, input2, end='\n')

    
    i1, i2 = tryHumnValue(monkes, input2)

    print(i1, '\n\n',i2)

    if isinstance(i1, int):
        (i1, i2) = (i2, i1)
    
    print((i2 - i1[1])/i1[0])



if __name__ == '__main__':
    inputFile = []
    infile = './test.txt'
    with open(infile) as f:
        inputFile = [line.strip().split() for line in f]


    part1([x.copy() for x in inputFile])
    part2([x.copy() for x in inputFile])