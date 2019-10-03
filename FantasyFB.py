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


print('hello welcome to the fantasy football calculator!')
print('Print 1 for WR, 2 for RB, 3 for TE, 4 for QB')
pos = input('What position is the player?')
name = input('What is the name of the player?')
weekRushTds = int(input('How many touchdowns did your player rush or catch this week?'))
weekReceivingYds = int(input('How many yards did your player have receiving or rushing this week?'))
receps = int(input('How many receptions did your player have this week?'))
weekRushTds = float(weekRushTds)
weekReceivingYards = float(weekReceivingYds)
receps = float(receps)
weekPassTds = int(input('How many touchdowns did your player throw for?'))
weekPassYds = int(input('How many yards did your player throw for?'))
if pos ==  1 or 2 or 3:
    totalPoints = int(((weekRushTds * 6) + (weekReceivingYds *  .1) + (weekPassTds * 4) + (weekPassYds * .05) + (receps)))
    print('Total points were',format(totalPoints,'.2f'))
elif pos == 4:
    totalPoints = int(((weekPassTds * 4) + (weekPassYds * .05) + (weekRushTds * 6) + (weekReceivingYds *  .1) + (receps)))
    print('Total Points are',(totalPoints,'.2f'))
