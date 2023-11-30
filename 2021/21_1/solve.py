def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    result.append(int(line.split(':')[1]))
  return result

def turn(space, diceValue):
  return ((space + 3 * diceValue + 2) % 10) + 1

def firstStar(input):
  diceValue = 1
  diceRolls = 0
  firstSpace = input[0]
  secondSpace = input[1]
  firstScore = 0
  secondScore = 0
  while True:
    firstSpace = turn(firstSpace, diceValue)
    firstScore += firstSpace
    diceValue += 3
    diceValue = ((diceValue - 1) % 100) + 1
    diceRolls += 3
    if firstScore >= 1000:
      return secondScore*diceRolls
    secondSpace = turn(secondSpace, diceValue)
    secondScore += secondSpace
    diceValue += 3
    diceValue = ((diceValue - 1) % 100) + 1
    diceRolls += 3
    if secondScore >= 1000:
      return firstScore*diceRolls

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 604998

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
