# pythonintegration
print('hello welcome to the fantasy football calculator!')
print('Print 1 for WR, 2 for RB, 3 for TE, 4 for QB, 5 for Defense/Speacial Teams, or 6 for kickers')
pos = int(input('What position is the player?'))
name = input('What is the name of the player?')
num = int(input('how many weeks would you like to calculate?'))
for x in range(num):
    if pos == 1:
        weekRushTds = int(input('How many touchdowns did your player rush or catch this week?'))
        weekReceivingYds = int(input('How many yards did your player have receiving or rushing this week?'))
        receps = int(input('How many receptions did your player have this week?'))
        totalPoints = int(((weekRushTds * 6) + (weekReceivingYds *  .1) + (receps)))
    elif pos == 2:
        weekRushTds = int(input('How many touchdowns did your player rush or catch this week?'))
        weekReceivingYds = int(input('How many yards did your player have receiving or rushing this week?'))
        receps = int(input('How many receptions did your player have this week?'))
        totalPoints = int(((weekRushTds * 6) + (weekReceivingYds *  .1) + (receps)))
    elif pos == 3:
        weekRushTds = int(input('How many touchdowns did your player rush or catch this week?'))
        weekReceivingYds = int(input('How many yards did your player have receiving or rushing this week?'))
        receps = int(input('How many receptions did your player have this week?'))
        totalPoints = int(((weekRushTds * 6) + (weekReceivingYds *  .1) + (receps)))
    elif pos == 4:
        weekPassTds = int(input('How many touchdowns did your player throw for?'))
        weekPassYds = int(input('How many yards did your player throw for?'))
        weekInt = int(input('How many interceptions did your player throw?'))
        totalPoints = int(((weekPassTds * 4) + (weekPassYds * .05) + (weekInt * -2)))
    elif pos == 5:
        kickPuntRet = int(input("How many kcikoffs or punt returns did your speacial team return?"))
        defTouchdown = int(input("How many touchdowns did your defense score?"))
        sack = int(input("How many sacks did your defense have?"))
        blocks = int(input("How many field goal or extra points did your defense block?"))
        fumbIntSafety = int(input("How many total fumble recoveries, interceptions(Not for a Touchdown), and safeties did your defense get?"))
        pointsAllow = int(input("How many points did your defense allow?"))
        yardsAllow = int(input("How many total yards did your defense allow?"))
        if pointsAllow == 0:
            (pointsGiven) = 5
        elif 1 <= pointsAllow <= 6:
            (pointsGiven) = 4
        elif 7 <= pointsAllow <= 13:
            (pointsGiven) = 3
        elif 14 <= pointsAllow <= 17:
            (pointsGiven) = 1
        elif 18 <= pointsAllow <= 27:
            (pointsGiven) = 0
        elif 28 <= pointsAllow <= 34:
            (pointsGiven) = -1
        elif 35 <= pointsAllow <= 45:
            (pointsGiven) = -3
        elif pointsAllow >= 46:
            (pointsGiven) = -5
        if yardsAllow < 100:
            (yardsGiven) = 5
        elif 100 <= yardsAllow <= 199:
            (yardsGiven) = 3
        elif 200 <= yardsAllow <= 299:
            (yardsGiven) = 2
        elif 300 <= yardsAllow <= 349:
            (yardsGiven) = 0
        elif 350 <= yardsAllow <= 399:
            (yardsGiven) = -1
        elif 400 <= yardsAllow <=449:
            (yardsGiven) = -3
        elif 450 <= yardsAllow <= 499:
            (yardsGiven) = -5
        elif 500 <= yardsAllow <= 549:
            (yardsGiven) = -6
        elif yardsAllow >= 550:
            (yardsGiven) = -7
        totalPoints = int((kickPuntRet * 6) + (defTouchdown * 6) + (sack) + (blocks * 2) + (fumbIntSafety * 2) + (pointsGiven) + (yardsGiven))
    if pos == 6:
        PAT = int(input("How many extra points did you kicker make?"))
        missedFG = int(input("How many total fields goals and extra points did your kicker miss?"))
        madeFG = int(input("How many field goals did your kicker make"))
        for y in range(madeFG):
            distance = int(input("How far was the field goal?"))
            if 0 <= distance <= 39:
                (pointsOnFgs) = 3
            elif 40 <= distance <= 49:
                (pointsOnFgs) = 4
            elif distance >= 50:
                (pointsOnFgs) = 5
        totalPoints = int((PAT) + (missedFG * -1) + (pointsOnFgs))
    print(name,"week",(x + 1),"totals were",totalPoints)
