import sys
import random

stake = int(input("Enter the stake amount:"))
goal = int(input("Enter the amount you want to win: "))
trials = int(input("Enter How mny trials youi want to play:"))

bets = 0
wins = 0
for t in range(trials):
   
    cash = stake
    while cash > 0 and cash < goal:
       
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print(str(100 * wins//trials) + '% wins')
print('Avg # bets: ' + str(bets//trials))