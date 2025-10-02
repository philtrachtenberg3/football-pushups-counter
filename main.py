# Make a counter to track the number of pushups done in a game

# ask user to enter the number of points just scored (2, 3, or 7)
# show current total
# ask user to enter "end" when game is over

import math


totalPushups = 0
totalPoints = 0

while True:
    points = input("How many points were just scored: ")
    if points.lower() == "exit":
        break

    try:
        points = int(points)
        totalPoints += points
        totalPushups += totalPoints
        print(f'Total pushups so far: {totalPushups}')
        print(f'Total points so far: {totalPoints}')
    except:
        print("Enter a number or \"exit\"")

print(f'Total number of pushups: {totalPushups}')
print(f'Final points total: {totalPoints}')