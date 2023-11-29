from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append([])
    for c in line:
      if c == '.':
        result[-1].append(0)
      elif c == '|':
        result[-1].append(1)
      elif c == '#':
        result[-1].append(2)
    result[-1] = tuple(result[-1])
  return tuple(result)

def printField(field):
  for line in field:
    for c in line:
      if c == 0:
        print('.', end = '')
      elif c == 1:
        print('|', end = '')
      elif c == 2:
        print('#', end = '')
    print()
  print()

def countRessources(field):
  numWood = 0
  numLumberyard = 0
  for line in field:
    for c in line:
      if c == 1:
        numWood += 1
      elif c == 2:
        numLumberyard += 1
  return numWood*numLumberyard

def neighboors(x, y, xmax, ymax):
  result = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      newY = y + i
      newX = x + j
      if 0 <= newX < xmax and 0 <= newY < ymax:
        result.append((newY, newX))
  return result

def aggregateNeighboors(x, y, xmax, ymax, field):
  numGround = 0
  numWood = 0
  numLumberyard = 0
  for (nY, nX) in neighboors(x, y, xmax, ymax):
    n = field[nY][nX]
    if n == 0:
      numGround += 1
    elif n == 1:
      numWood += 1
    else:
      numLumberyard += 1
  return numGround, numWood, numLumberyard

def nextSymbol(x, y, xmax, ymax, field):
  currSymbol = field[y][x]
  nGround, nWood, nLumberyard = aggregateNeighboors(x, y, xmax, ymax, field)
  if currSymbol == 0:
  # An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
    if nWood >= 3:
      return 1
    return 0
  if currSymbol == 1:
  # An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
    if nLumberyard >= 3:
      return 2
    return 1
  # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
  if nLumberyard >= 1 and nWood >= 1:
    return 2
  return 0

def evolve(field):
  xmax = len(field[0])
  ymax = len(field)
  newField = [[0 for _ in range(xmax)] for _ in range(ymax)]
  for y in range(ymax):
    for x in range(xmax):
      newField[y][x] = nextSymbol(x, y, xmax, ymax, field)
    newField[y] = tuple(newField[y])
  return tuple(newField)

def firstStar(input):
  rMax = 10
  field = input
  for i in range(rMax):
    field = evolve(field)
  return countRessources(field)

def secondStar(input):
  rMax = 1000000000
  field = input
  hashList = []
  loopFound = False
  i = 0
  while i < rMax:
    field = evolve(field)
    hField = hash(field)
    if not loopFound and hField in hashList:
      loopFound = True
      cycleStart = hashList.index(hField)
      cycleLength = i - cycleStart
      stepTo = rMax - ((rMax - cycleStart) % cycleLength)
      i = stepTo
    hashList.append(hField)
    i += 1
  return countRessources(field)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 483840

print("The second star is : {}".format(secondStar(input)))
# The second star is : 219919
