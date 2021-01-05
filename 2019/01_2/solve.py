def readInput(file):
  return [int(line) for line in open(file).read().splitlines()]

def calcFuel(mass):
  return max(mass//3 - 2, 0)

def calcTotalFuel(mass):
  totalFuel = 0
  fuel = mass//3 - 2
  while(fuel > 0):
    totalFuel += fuel
    fuel = fuel//3 - 2
  return totalFuel

def firstStar(input):
  return sum(calcFuel(mass) for mass in input)

def secondStar(input):
  return sum(calcTotalFuel(mass) for mass in input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3538016

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5304147
