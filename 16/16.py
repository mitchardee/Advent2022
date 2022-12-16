# Credit for test cases to u/i_have_no_biscuits

from collections import defaultdict
from itertools import combinations

def makeMap(input):
    dists = defaultdict(lambda:defaultdict(lambda: -1)) # uninitialized map entries are -1

    # input is bi-directional
    for line in input:
        for str in line[9:]:
            dists[line[1]][str.replace(',', '')] = 1 #total cost of going to and turning pipe will be this +1


    writtenOne = True
    while writtenOne:
        writtenOne = False
        for key, val in [x for x in dists.items()]: # val is the top level dict; need to make copies of the dicts or we get a runtime error
            for key1, val1 in [y for y in val.items()]:
                for key2, val2 in [z for z in dists[key1].items()]:
                    if key != key2 and (dists[key][key2] == -1 or val1 + val2 < dists[key][key2]):
                        writtenOne = True
                        dists[key][key2] = val1 + val2

    

    return dists
    # for key, val in dists.items():
    #     print(key)
    #     print(val)

    # Make sure the maps are symmetrical
    # for key, val in dists.items():
    #     for key1, val1 in val.items():
    #         if val1 != dists[key1][key]:
    #             print('ERROR', key, key1, val1, ' != ', dists[key1][key])

def addBenefits(dists, input):
    for line in input:
        pressure = int(line[4][5:-1])
        if pressure == 0:
            for key, val in dists.items():
                if key != line[1]:
                    val.pop(line[1])
            if line[1] != 'AA':
                dists.pop(line[1])
        else:
            dists[line[1]]['pressure'] = pressure

def costBenefit(start, end, dists, currentTime):
    cost = dists[start][end] + 1
    benefit = dists[end]['pressure'] * (currentTime - cost)
    return cost, benefit

def maximizeSteam(start, dists, currentTime, visited):
    if currentTime < 1:
        return 0
    
    maxSteam = 0
    for cave in dists[start].keys():
        if cave in visited or cave=='pressure':
            continue

        cost, benefit = costBenefit(start, cave, dists, currentTime)

        if benefit == 0:
            continue

        downThisPath= maximizeSteam(cave, dists, currentTime - cost, visited + [cave]) + benefit
        maxSteam = max(maxSteam, downThisPath)

    return maxSteam 



def part1(input):
    dists = makeMap(input)
    addBenefits(dists, input)

    # for key, val in dists.items():
    #      print(key)
    #      print(val)

    print(maximizeSteam('AA', dists, 30, []))


def maximizeSteamElephant(posMe, posElephant, dists, currentTimeMe, currentTimeElephant, visited):
    if currentTimeMe < 1 and currentTimeElephant < 1:
        return 0
    
    maxSteam = 0

    if currentTimeMe < 1 or currentTimeElephant < 1:
        me = currentTimeMe > 0
        pos = posMe if me else posElephant
        time = currentTimeMe if me else currentTimeElephant

        return maximizeSteam(pos, dists, time, visited)


    for cave in dists[posMe].keys():
        if cave in visited or cave=='pressure':
            continue

        cost, benefit = costBenefit(posMe, cave, dists, currentTimeMe)

        for eCave in dists[posElephant].keys():
            if eCave in visited or cave == eCave or eCave == 'pressure':
                continue

            eCost, eBenefit = costBenefit(posElephant, eCave, dists, currentTimeElephant)

            if eBenefit == 0:
                continue

            
            downThisPath= maximizeSteamElephant(cave, eCave, dists, currentTimeMe - cost, currentTimeElephant - eCost, visited + [eCave, cave]) + eBenefit + benefit
            maxSteam = max(maxSteam, downThisPath)

    # Try doing nothing as well
    # maxSteam = max(maxSteam, maximizeSteamElephant(posMe, posElephant, dists, currentTimeMe-1, currentTimeElephant, visited), maximizeSteamElephant(posMe, posElephant, dists, currentTimeMe, currentTimeElephant-1, visited))
 
    return maxSteam 

def firstCall(posMe, posElephant, dists, currentTimeMe, currentTimeElephant):
    maxSteam = 0
    tried = [] # Elephant can't start anywhere I've already checked as a starting position

    for cave in dists[posMe].keys():
        tried.append(cave)
        if cave=='pressure':
            continue

        cost, benefit = costBenefit(posMe, cave, dists, currentTimeMe)
        if benefit == 0:
            continue

        for eCave in dists[posElephant].keys():
            if eCave in tried or eCave == 'pressure':
                continue

            eCost, eBenefit = costBenefit(posElephant, eCave, dists, currentTimeElephant)

            if eBenefit == 0:
                continue

            downThisPath= maximizeSteamElephant(cave, eCave, dists, currentTimeMe - cost, currentTimeElephant - eCost, [cave, eCave]) + benefit + eBenefit
            maxSteam = max(maxSteam, downThisPath)

    return maxSteam 


def part2naive(input):
    dists = makeMap(input)
    addBenefits(dists, input)

    # for key, val in dists.items():
    #      print(key)
    #      print(val)

    print('Finished!: ', firstCall('AA', 'AA', dists, 26, 26))

def part2(input):
    dists = makeMap(input)
    addBenefits(dists, input)
    workingTime = 26

    netDists = []
    for key, value in dists.items():
        if key == 'AA':
            continue
        for val in value.values():
            if val != 'pressure':
                netDists.append(val + 1)

    # Find maximum number of actions either player could make in the given time
    rMax = 0
    minTime = 0
    for v in sorted(netDists):
        rMax += 1
        minTime += v
        if minTime > workingTime:
            break


    bestSplit = 0

    for r in range(rMax):
        for comb in combinations(dists.keys(), r):
            eleVisits = [key for key in dists.keys() if not key in comb]
            # print(comb)
            # print(eleVisits, end='\n\n')

            running = maximizeSteam('AA', dists, workingTime, list(comb)) + maximizeSteam('AA', dists, workingTime, eleVisits)
            bestSplit = max(bestSplit, running)

    print(bestSplit)



if __name__ == '__main__':
    input = []
    infile = './input.txt'
    with open(infile) as f:
        input = [line.strip().split() for line in f]

    
    part1(input)
    print(infile, 'part1')
    part2(input)
    print(infile, 'part2')