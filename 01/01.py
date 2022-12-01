
if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = f.readlines()
    
    max = [0, 0, 0]
    running = 0

    for line in (input_lines):
        if line.strip() == '' :
            if running > min(max):
                max[max.index(min(max))] = running
            running = 0
        else:
            running += int(line)



    print(max)
    print(sum(max))
