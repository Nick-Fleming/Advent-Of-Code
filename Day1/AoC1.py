import math

f = open("/Users/nickfleming/Code/Advent of Code/Day1/input1.txt", "r")
totalFuel = 0
for x in f:
    fuel = math.floor(int(x) / 3) - 2
    totalFuel += fuel
    fuel = math.floor(int(fuel) / 3) - 2
    while fuel > 0:
        totalFuel += fuel
        fuel = math.floor(fuel/3) - 2

print(totalFuel)
