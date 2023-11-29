from pathlib import Path
from copy import deepcopy
from math import gcd

def lcm(a, b):
  return a*b // gcd(a, b)

def readInput(file):
  result = []
  for l in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append([tuple(int(c.split("=")[1].replace('>', '')) for c in l.split(",")), (0,0,0)])
  return tuple(result)

def sign(value):
  if value == 0:
    return 0
  if value < 0:
    return -1
  return 1

def gravity(aMoon, bMoon):
  return tuple(sign(bMoon[0][i] - aMoon[0][i]) + aMoon[1][i] for i in range(len(aMoon[0])))

def moveMoon(moon):
  return tuple(moon[0][i] + moon[1][i] for i in range(len(moon[0])))

def step(state):
  for aMoon in state:
    for bMoon in state:
      if aMoon != bMoon:
        aMoon[1] = gravity(aMoon, bMoon)
  for moon in state:
    moon[0] = moveMoon(moon)

def tuplify(state):
  return tuple(tuple(moon) for moon in state)

def separateCoord(state):
  result = ([], [], [])
  for moon in state:
    for i in range(len(moon[0])):
      result[i].append((moon[0][i], moon[1][i]))
  return tuple(tuple(coord) for coord in result)

def pot(moon):
  return sum(abs(pos) for pos in moon[0])

def kin(moon):
  return sum(abs(vel) for vel in moon[1])

def energy(state):
  return sum(pot(moon) * kin(moon) for moon in state)

def firstStar(input):
  state = deepcopy(input)
  for _ in range(1000):
    step(state)
  return energy(state)

def secondStar(input):
  state = deepcopy(input)

  statesSetX = set()
  statesSetY = set()
  statesSetZ = set()

  newStateX, newStateY, newStateZ = separateCoord(state)

  statesSetX.add(newStateX)
  statesSetY.add(newStateY)
  statesSetZ.add(newStateZ)
  prevSetXLength = len(statesSetX)
  prevSetYLength = len(statesSetY)
  prevSetZLength = len(statesSetZ)

  xNotFound = True
  yNotFound = True
  zNotFound = True

  xLoop = 0
  yLoop = 0
  zLoop = 0

  while xNotFound or yNotFound or zNotFound:
    step(state)

    newStateX, newStateY, newStateZ = separateCoord(state)
    statesSetX.add(newStateX)
    statesSetY.add(newStateY)
    statesSetZ.add(newStateZ)

    newSetXLength = len(statesSetX)
    newSetYLength = len(statesSetY)
    newSetZLength = len(statesSetZ)
    if(prevSetXLength == newSetXLength):
      xLoop = newSetXLength
      xNotFound = False
    prevSetXLength = newSetXLength
    if(prevSetYLength == newSetYLength):
      yLoop = newSetYLength
      yNotFound = False
    prevSetYLength = newSetYLength
    if(prevSetZLength == newSetZLength):
      zLoop = newSetZLength
      zNotFound = False
    prevSetZLength = newSetZLength
  return lcm(lcm(xLoop, yLoop), zLoop)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 6423

print("The second star is : {}".format(secondStar(input)))
# The second star is : 327636285682704
