# The winner of the whole tournament is the player with the highest score. 
# Your total score is the sum of your scores for each round. The score for 
# a single round is the score for the shape you selected (1 for Rock, 2 for 
# Paper, and 3 for Scissors) plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

#A, B, C: Opponent throws 🪨, 📄, ✂️
#X, Y, Z: I throw 🪨, 📄, ✂️
di1 = { 'B X':1, 'C Y':2, 'A Z':3, 'A X':4, 'B Y':5, 'C Z':6, 'C X':7, 'A Y':8, 'B Z':9 }

#A, B, C: Opponent throws 🪨, 📄, ✂️
#X, Y, Z: I lose, tie, win
di2 = { 'B X':1, 'C X':2, 'A X':3, 'A Y':4, 'B Y':5, 'C Y':6, 'C Z':7, 'A Z':8, 'B Z':9 }

if __name__ == '__main__':

    input_lines = []

    with open('./input.txt') as f:
        input_lines = f.readlines()
    
    total1 = 0
    total2 = 0

    for line in (input_lines):
        total1 += di1[line.strip()]
        total2 += di2[line.strip()]

    print (total1, total2)