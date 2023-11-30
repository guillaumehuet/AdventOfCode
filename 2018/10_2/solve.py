from pathlib import Path
from copy import deepcopy

gTime = 0

def readInput(file):
  return [[[int(coord) for coord in str.split('<')[1].split(',')] for str in line.split('>')[:-1]] for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def firstStar(input):
  global gTime
  state = deepcopy(input)
  prevSize = step(state)
  while(True):
    gTime += 1
    newSize = step(state)
    if newSize > prevSize:
      step(state, -1)
      return stateToStr(state)
    prevSize = newSize

def stateToStr(state):
  result = ''
  pos = tuple(tuple(c[0]) for c in state)
  allX = tuple(c[1] for c in pos)
  allY = tuple(c[0] for c in pos)
  
  minX = min(allX)
  maxX = max(allX)
  
  minY = min(allY)
  maxY = max(allY)
  
  for x in range(minX, maxX + 1):
    result += '\n'
    for y in range(minY, maxY + 1):
      if (y, x) in pos:
        result += '#'
      else:
        result += '.'
  return result

def step(state, dir = 1):
  for point in state:
    point[0][0] += dir*point[1][0]
    point[0][1] += dir*point[1][1]
  
  pos = tuple(tuple(c[0]) for c in state)
  allX = tuple(c[1] for c in pos)
  allY = tuple(c[0] for c in pos)
  
  minX = min(allX)
  maxX = max(allX)
  
  minY = min(allY)
  maxY = max(allY)
  
  return (maxX - minX + 1)*(maxY - minY + 1)

def secondStar(input):
  return gTime

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : XLZAKBGZ

print("The second star is : {}".format(secondStar(input)))
# The second star is : 10656
