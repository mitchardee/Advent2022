

def makeBlueprints(input):
    return [[(int(line[6]), 0, 0, 0), (int(line[12]), 0, 0, 0), (int(line[18]), int(line[21]), 0, 0), (int(line[27]), 0, int(line[30]), 0)] for line in input]

def canBuild(botRecipe, bots, time, resources):
    for i, cost in enumerate(botRecipe):
        if cost > resources[i] + bots[i] * time:
            return False

    return True

def stateToBuild(botRecipe, timeLeft, bots, resources):
    for i in range(timeLeft):
        if canBuild(botRecipe, bots, i, resources):
            return (True, timeLeft - i - 1, [resources[j] - botRecipe[j] + bots[j]*(i + 1) for j in range(len(botRecipe))])

    return (False, None, None)

def maxGeodes(blueprint, timeLeft, bots, resources, costMax, totalTime):
    # print(blueprint, timeLeft, bots, resources)
    if timeLeft < 1:
        return resources[3], ''

    
    if canBuild(blueprint[3], bots, 0, resources):
        updatedBots = [bots[j] + 1 if 3 == j else bots[j] for j in range(len(bots))]
        (buildable, updatedTime, updatedResources) = stateToBuild(blueprint[3], timeLeft, bots, resources)
        if not buildable:
            print('big problem', blueprint, timeLeft, bots, resources)

        [maxGeo, maxRecipe] = maxGeodes(blueprint, updatedTime, updatedBots, updatedResources, costMax, totalTime)
        return [maxGeo, str(totalTime-updatedTime)+ ' 3'+ ' bots:' + str(updatedBots) + ' res: ' + str(updatedResources) + ', \n'+ maxRecipe]
        

    maxG = [resources[3] + timeLeft * bots[3], '']
        
    for i, recipe in enumerate(blueprint):
        (buildable, updatedTime, updatedResources) = stateToBuild(recipe, timeLeft, bots, resources)

        if not buildable or (i<3 and (bots[i] * timeLeft + resources[i]) >= timeLeft * costMax[i]):
            continue

        updatedBots = [bots[j] + 1 if i == j else bots[j] for j in range(len(bots))]

        [maxGeo, maxRecipe] = maxGeodes(blueprint, updatedTime, updatedBots, updatedResources, costMax, totalTime)
        if maxG[0] < maxGeo:
            maxG = [maxGeo, str(32-updatedTime)+ ' '+str(i)+ ' bots:' + str(updatedBots) + ' res: ' + str(updatedResources) + ', \n'+ maxRecipe]


    return maxG
    




def part1(input):
    blueprints = makeBlueprints(input)

    totalQuality = 0
    print()

    for i, blueprint in enumerate(blueprints):
        bots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]
        costMax = [max([recipe[i] for recipe in blueprint]) for i in range(3)]

        geodes, message = maxGeodes(blueprint, 24, bots, resources, costMax, 24)
        print(geodes, '\n', message)

        totalQuality += geodes * (i+1)
    
    print('totalQuality: ',totalQuality)

def part2(input):
    blueprints = makeBlueprints(input)

    print()

    product = 1

    for blueprint in blueprints[0:3]:
        bots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]
        costMax = [max([recipe[i] for recipe in blueprint]) for i in range(3)]

        geodes, message = maxGeodes(blueprint, 32, bots, resources, costMax, 32)
        print(geodes, '\n', message)
        product *= geodes

    print('product:', product)


if __name__ == '__main__':
    input = []
    infile = './input.txt'
    with open(infile) as f:
        input = [line.strip().split() for line in f]

    part1(input)
    part2(input)
