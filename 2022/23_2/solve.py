def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    result.append([])
    for c in line:
      if c == '#':
        result[-1].append(True)
      else:
        result[-1].append(False)
  return result

def gridToElves(grid):
  elves = set()
  width = len(grid[0])
  heigth = len(grid)
  for x in range(width):
    for y in range(heigth):
      if grid[y][x]:
        elves.add((x, y))
  return elves

def elvesToGrid(elves):
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0
  for elf in elves:
    minX = min(minX, elf[0])
    maxX = max(maxX, elf[0])
    minY = min(minY, elf[1])
    maxY = max(maxY, elf[1])
  result = []
  for y in range(minY, maxY + 1):
    result.append([])
    for x in range(minX, maxX + 1):
      if (x, y) in elves:
        result[-1].append(True)
      else:
        result[-1].append(False)
  return result

def printGrid(grid):
  for line in grid:
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print('')
  print('')

def neighboors(position, elves):
  result = set()
  for x in range(-1, 2):
    for y in range(-1, 2):
      if x != 0 or y != 0:
        currX = x + position[0]
        currY = y + position[1]
        if (currX, currY) in elves:
          result.add((x + position[0], y + position[1]))
  return result

def moveNorth(position, elves):
  currY = position[1] - 1
  for x in range(-1, 2):
    currX = x + position[0]
    if (currX, currY) in elves:
      return False
  return position[0], currY

def moveSouth(position, elves):
  currY = position[1] + 1
  for x in range(-1, 2):
    currX = x + position[0]
    if (currX, currY) in elves:
      return False
  return position[0], currY

def moveWest(position, elves):
  currX = position[0] - 1
  for y in range(-1, 2):
    currY = y + position[1]
    if (currX, currY) in elves:
      return False
  return currX, position[1]

def moveEast(position, elves):
  currX = position[0] + 1
  for y in range(-1, 2):
    currY = y + position[1]
    if (currX, currY) in elves:
      return False
  return currX, position[1]

def nextPos(currElf, elves, moveOrder):
  closeElves = neighboors(currElf, elves)
  if not closeElves:
    return currElf
  for i in range(4):
    result = moveOrder[i](currElf, elves)
    if result:
      return result
  return currElf

def round(elves, moveOrder):
  propositions = dict()
  alreadyProposed = set()
  duplicate = set()
  for currElf in elves:
    currProposition = nextPos(currElf, elves, moveOrder)
    if currProposition in alreadyProposed:
      duplicate.add(currProposition)
    propositions[currElf] = currProposition
    alreadyProposed.add(currProposition)
  for currElf in propositions:
    if propositions[currElf] in duplicate:
      propositions[currElf] = currElf
  return set(propositions.values())

def countEmpty(elves):
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0
  for elf in elves:
    minX = min(minX, elf[0])
    maxX = max(maxX, elf[0])
    minY = min(minY, elf[1])
    maxY = max(maxY, elf[1])
  result = 0
  for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
      if (x, y) not in elves:
        result += 1
  return result

def firstStar(input):
  elves = gridToElves(input)
  moveOrder = [moveNorth, moveSouth, moveWest, moveEast]
  for r in range(10):
    elves = round(elves, moveOrder)
    moveOrder = moveOrder[1:] + moveOrder[:1]
  return countEmpty(elves)

def secondStar(input):
  elves = gridToElves(input)
  moveOrder = [moveNorth, moveSouth, moveWest, moveEast]
  currRound = 0
  while True:
    currRound += 1
    newElves = round(elves, moveOrder)
    if newElves == elves:
      return currRound
    elves = newElves
    moveOrder = moveOrder[1:] + moveOrder[:1]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3990

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1057
