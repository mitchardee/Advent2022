def finalize_e(grid):
    for line in grid:
        for c in line:
            if c == 'm':
                c = 'e'

def finalize_s(grid):
    for line in grid:
        for c in line:
            if c == 'm':
                c = 's'

def iterate(grid, first_row, first_column):

    for i,line in enumerate(grid):
        ## iterate backward so buds don't move twice
        for j,c in enumerate(line[:-1]):
            if c == 'e':
                if line[j+1] == 'f':
                    line[j+1] = 'm'
                    line[j] = 'f'
        if line[-1] == 'e' and 
                    
        
    



def part1(input_lines):
    # e: east, s: south, f: free, m:moved
    grid = [['e' if c=='>' else 's' if c=='v' else 'f' for c in line] for line in input_lines]
    
    first_column = [line[0] for line in grid]
    first_row = grid[0]

if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = f.readlines()
    
    iterate('>.', '.>')