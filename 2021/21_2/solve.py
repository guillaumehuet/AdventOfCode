from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append(int(line.split(':')[1]))
  return result

def turn(space, diceValue):
  return ((space + 3 * diceValue + 2) % 10) + 1

def diracTurn(nUniverses, space, score, otherSpace, otherScore, distribution):
  result = []
  wins = 0
  for roll, nRolls in distribution.items():
    newSpace = (space + roll - 1) % 10 + 1
    newScore = score + newSpace
    if newScore >= 21:
      wins += nUniverses*nRolls
    else:
      result.append((nUniverses*nRolls, otherSpace, otherScore, newSpace, newScore))
  return tuple(result), wins

def diracDistribution(nDice, nSides):
  result = {v:0 for v in range(nDice, nDice*nSides + 1)}
  rolls = [0]
  for _ in range(nDice):
    currDie = list(range(1, nSides + 1))
    rolls = [d1 + d2 for d1 in rolls for d2 in currDie]
  for r in rolls:
    result[r] += 1
  return result

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
  distribution = diracDistribution(3, 3)
  universes = ((1, input[0], 0, input[1], 0), )
  totalWins = [0, 0]
  currPlayer = 0
  while universes:
    allNewUniverses = []
    for nUniverses, space, score, otherSpace, otherScore in universes:
      newUniverses, wins = diracTurn(nUniverses, space, score, otherSpace, otherScore, distribution)
      totalWins[currPlayer] += wins
      allNewUniverses += newUniverses
    universes = tuple(allNewUniverses)
    currPlayer += 1
    currPlayer %= 2
  return max(totalWins)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 604998

print("The second star is : {}".format(secondStar(input)))
# The second star is : 157253621231420
