#Donovan Smith
#Fantasy Football Calculator

print('Hello, welcome to the fantasy football score calculator!')
pos = input('What is the players position?')
name = input('What is the players name?')
weekYards = input('How many total yards?')
weekTd = input('How many total touchdowns?')
int1 = int(weekYards)
int2 = int(weekTd)
int1 = float(int1)
pointsOnYards = (int1*.1)
pointsOnTds = (int2*6)
int3 = int(pointsOnYards)
int4 = int(pointsOnTds)
totalPoints = (int3+int4)
int5 = int(totalPoints)
print(name , pos , "total points were", int5)
