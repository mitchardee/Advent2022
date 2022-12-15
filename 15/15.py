import bisect
from interval import interval
import time

# Homemade interval ran in ~25% the time compared to pyinterval
class Interval:
    def __init__(self, ranges):

        self.items = [] 

        for range in ranges:
            if(range[0] > range[1]):
                self.union((range[1], range[0]))
            else:
                self.union(range)

    def __repr__(self):
        return str(self.items)

    def length(self):
        l = 0
        for range in self.items:
            l += range[1] - range[0] + 1 # +1 for the endpoint inclusion e.g. |(1,3)| == 3
        return l

    def union(self, newPair):
        
        if len(self.items) == 0:
            self.items.append(newPair)
            return

        insPoint = bisect.bisect(self.items, newPair[0], key=lambda p:p[0])
        if insPoint > 0:
            cmpPair = self.items[insPoint-1]
            if newPair[0] <= cmpPair[1] + 1:
                self.union((cmpPair[0], max((self.items.pop(insPoint-1))[1], newPair[1])))
                return

        if insPoint < len(self.items):
            cmpPair = self.items[insPoint]
            if newPair[1] >= cmpPair[0] - 1:
                self.union((newPair[0], max((self.items.pop(insPoint))[1], newPair[1])))
                return
                
                
        self.items.insert(insPoint, newPair)

    def remove(self, n):
        ind = bisect.bisect(self.items, n, key=lambda p:p[0])
        if ind == 0:
            return
        pair = self.items[ind-1]
        if pair[0] == n:
            if pair[1] == n:
                self.items.pop(ind-1)
            else:
                self.items[ind-1] = (pair[0]+1, pair[1])
        elif pair[1] == n:
            self.items[ind-1] = (pair[0], pair[1]-1)
        elif pair[1] > n:
            pair = self.items.pop(ind-1)
            self.union((pair[0], n-1))
            self.union((n+1, pair[1]))

    def checkForHoles(self):
        ind = bisect.bisect(self.items, 0, key=lambda p:p[0])
        if self.items[ind-1][1] <= 4000000:
            print(self)
            print(self.items[ind-1][1] + 1, end=', ')
            return True
        return False

def findIntervalHole(inter):
    if interval[0, 4000000] != (inter & interval[0, 4000000]):
        for x in inter:
            if x[0] <= 0 and x[1] > 0:
                return [True, x[1] + 1]
    return [False, None]

def part1(input):
    testRow = 2000000

    intervals = Interval([])

    for line in input:
        S_x = int(line[2][2:-1])
        S_y = int(line[3][2:-1])
        B_x = int(line[-2][2:-1])
        B_y = int(line[-1][2:])

        d = abs(S_x - B_x) + abs(S_y - B_y)

        if abs(testRow - S_y) <= d:
            w = d - abs(testRow - S_y)
            intervals.union((S_x - w, S_x + w))

    for line in input:
        B_x = int(line[-2][2:-1])
        B_y = int(line[-1][2:])

        if B_y == testRow:
            intervals.remove(B_x)

    print(intervals)

    print(intervals.length())

# ran in 76s
def part2(input):
    for testRow in range(4000001):

        intervals = Interval([])

        for line in input:
            S_x = int(line[2][2:-1])
            S_y = int(line[3][2:-1])
            B_x = int(line[-2][2:-1])
            B_y = int(line[-1][2:])

            d = abs(S_x - B_x) + abs(S_y - B_y)

            if abs(testRow - S_y) <= d:
                w = d - abs(testRow - S_y)
                intervals.union((S_x - w, S_x + w))
        
        if intervals.checkForHoles():
            print(testRow)
            print((intervals.items[0][1] + 1)*4000000 + testRow)
            return



# Trying a solution using pyinterval
# To run, use `pip install pyinterval`
def part1ints(input):
    testRow = 2000000

    intervals = interval()

    for line in input:
        S_x = int(line[2][2:-1])
        S_y = int(line[3][2:-1])
        B_x = int(line[-2][2:-1])
        B_y = int(line[-1][2:])

        d = abs(S_x - B_x) + abs(S_y - B_y)

        if abs(testRow - S_y) <= d:
            w = d - abs(testRow - S_y)
            intervals |= interval[S_x - w, S_x + w]

    beacons = set()
    for line in input:
        B_x = int(line[-2][2:-1])
        B_y = int(line[-1][2:])

        if B_y == testRow:
            beacons.add(B_x)

    length = 0
    for x in intervals:
        length += x[1] - x[0] + 1


    print(length - len(beacons))

# Ran in ~303s on my machine
def part2ints(input):
    for testRow in range(40000001):

        intervals = interval()

        for line in input:
            S_x = int(line[2][2:-1])
            S_y = int(line[3][2:-1])
            B_x = int(line[-2][2:-1])
            B_y = int(line[-1][2:])

            d = abs(S_x - B_x) + abs(S_y - B_y)

            if abs(testRow - S_y) <= d:
                w = d - abs(testRow - S_y)
                intervals |= interval[(S_x - w), (S_x + w)]
        
        [foundHole, val] = findIntervalHole(intervals)
        if foundHole:
            print(testRow)
            print(val)
            print(val*4000000 + testRow)
            return




if __name__ == '__main__':

    input = []
    with open('./input.txt') as f:
        input = [line.strip().split() for line in f]

    start = time.time()
    part1(input)
    lap0 = time.time()
    part1ints(input)
    lap1 = time.time()
    part2(input)
    lap2 = time.time()
    part2ints(input)
    stop = time.time()

    print('part1: ', lap0-start, 's')
    print('part1ints: ', lap1-lap0, 's')
    print('part2: ', lap2-lap1, 's')
    print('part2ints: ', stop-lap2, 's')
