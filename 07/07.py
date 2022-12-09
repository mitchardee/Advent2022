from collections import defaultdict

class Node:
    smalls = 0

    def __init__(self, parent):
        self.parent = parent
        self.size = None
        self.child_dirs = defaultdict(lambda:Node(self))
        self.files = {}

    def babies(self, lines):
        for line in lines:
            if line[0] == 'dir':
                #handled by default dict
                continue
            else:
                self.files[line[1]] = int(line[0])

    def getSize(self):
        fileSum = 0
        for size in self.files.values():
            fileSum += size

        folderSum = 0
        for folder in self.child_dirs.values():
            folderSum += folder.getSize()
        
        self.size = fileSum + folderSum
        if self.size <= 100000:
            Node.smalls += self.size
        return self.size

    def searchForSmallest(self, spaceNeeded, smallestYet):
        smol = smallestYet
        for dir in self.child_dirs.values():
            mins = [smol, dir.size, dir.searchForSmallest(spaceNeeded, smol)]
            smol = min( [m for m in mins if m >= spaceNeeded ] )
        
        return smol


    def printTree(self):
        print('files :',self.files)
        print('subdirs :', [key for key in self.child_dirs.keys()])
        for filename, contents in self.child_dirs.items():
            print(filename, contents.size)
            contents.printTree()

def makeTree(root, input):
    cur = root
    ls_output = []

    for line in input[1:]:
        if line[0] == '$':
            cur.babies(ls_output)
            ls_output.clear()
            if line[1] == 'cd':
                if line[2] == '..':
                    cur = cur.parent
                else:
                    cur = cur.child_dirs[line[2]]
        else:
            ls_output.append(line)
    cur.babies(ls_output)


def part1(input):
    root = Node(None)

    makeTree(root, input)
    
    print('/', root.getSize())
    print('smalls: ', Node.smalls)


def part2(input):
    root = Node(None)
    makeTree(root, input)

    spaceNeeded = root.getSize() - 40000000
    print (spaceNeeded)
    print(root.searchForSmallest(spaceNeeded, root.size))



if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = [line.split() for line in f.readlines()]

    part1(input_lines)
    part2(input_lines)
