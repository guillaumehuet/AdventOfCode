import sys

def readInput(file):
  clayLines = []
  for line in open(file).read().splitlines():
    line = [l.split('=') for l in line.split(', ')]
    first = int(line[0][1])
    secondMin, secondMax = [int(c) for c in line[1][1].split('..')]
    if line[0][0] == 'x':
      clayLines.append([[first, first], [secondMin, secondMax]])
    else:
      clayLines.append([[secondMin, secondMax], [first, first]])
  minX = min(clayLine[0][0] for clayLine in clayLines) - 2
  maxX = max(clayLine[0][1] for clayLine in clayLines) + 2
  minY = min(clayLine[1][0] for clayLine in clayLines)
  maxY = max(clayLine[1][1] for clayLine in clayLines)
  terrain = [['.' for _ in range(minX, maxX + 1)] for y in range(minY, maxY + 1)]
  for clayLine in clayLines:
    for x in range(clayLine[0][0], clayLine[0][1] + 1):
      for y in range(clayLine[1][0], clayLine[1][1] + 1):
        terrain[y - minY][x - minX] = '#'
  terrain[0][500 - minX] = '|'
  return terrain

def drop(x, y, terrain):
  if y < len(terrain):
    if terrain[y][x] == '.':
      terrain[y][x] = '|'
    elif terrain[y][x] in '~#':
      fill(x, y - 1, terrain)

def fill(x, y, terrain):
  xmin = 0
  xmax = len(terrain[0])
  waterType = '~'
  for i in range(x, xmax):
    if terrain[y + 1][i] not in '~#':
      waterType = '|'
      xmax = i
      break
    if terrain[y][i] == '#':
      xmax = i
      break
  for i in range(x, xmin, -1):
    if terrain[y + 1][i] not in '~#':
      waterType = '|'
      xmin = i
      break
    if terrain[y][i] == '#':
      xmin = i
      break
  for i in range(xmin + 1, xmax):
    terrain[y][i] = waterType
  if waterType == '|':
    if terrain[y][xmin] == '.':
      terrain[y][xmin] = '|'
    if terrain[y][xmax] == '.':
      terrain[y][xmax] = '|'

def step(terrain):
  for y in range(len(terrain)):
    for x in range(len(terrain[0])):
      if terrain[y][x] == '|':
        drop(x, y + 1, terrain)

def printTerrain(terrain):
  print("\n".join(["".join(line) for line in terrain]))

def score(terrain):
  resultStill = 0
  resultTotal = 0
  for line in terrain:
    for c in line:
      if c in '~|':
        resultTotal += 1
        if c == '~':
          resultStill += 1
  return resultTotal, resultStill

def waterInTerrain(terrain):
  oldScore = (0, 0)
  newScore = score(terrain)
  while oldScore != newScore:
    oldScore = newScore
    step(terrain)
    newScore = score(terrain)
  return newScore

input = readInput('input')
firstStar, secondStar = waterInTerrain(input)

print("The first star is : {}".format(firstStar))
# The first star is : 36790

print("The second star is : {}".format(secondStar))
# The second star is : 30765
