def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    result.append([])
    for coord in line.split(' -> '):
      x, y = coord.split(',')
      x = int(x)
      y = int(y)
      result[-1].append((x, y))
    result[-1] = tuple(result[-1])
  return tuple(result)

def pathsToGrid(paths, secondStar = False):
  xMin = 500
  xMax = 500
  yMin = 0
  yMax = 0
  for line in paths:
    for x, y in line:
      xMin = min(x, xMin)
      xMax = max(x, xMax)
      yMin = min(y, yMin)
      yMax = max(y, yMax)
  yMax += 1
  xMin = min(xMin, 500 - yMax)
  xMax = max(xMax, 500 + yMax)
  grid = [[False for x in range(xMax - xMin + 1)] for y in range(yMax - yMin + 1)]
  for line in paths:
    prevX, prevY = line[0]
    for x, y in line[1:]:
      if x >= prevX:
        dirX = 1
      else:
        dirX = -1
      for i in range(prevX, x + dirX, dirX):
        if y >= prevY:
          dirY = 1
        else:
          dirY = -1
        for j in range(prevY, y + dirY, dirY):
          grid[j - yMin][i - xMin] = True
      prevX = x
      prevY = y
  return grid, xMin, yMin, yMax

def printGrid(grid):
  for line in grid:
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

def firstStar(input):
  grid, xMin, yMin, yMax = pathsToGrid(input)
  sandUnit = 0
  while True:
    pos = (500 - xMin, 0 - yMin)
    while True:
      for dir in (0, 1), (-1, 1), (1, 1):
        newPos = (pos[0] + dir[0], pos[1] + dir[1])
        if newPos[1] > yMax:
          return sandUnit
        if not grid[newPos[1]][newPos[0]]:
          pos = newPos
          break
      else:
        grid[pos[1]][pos[0]] = True
        break
    sandUnit += 1

def secondStar(input):
  grid, xMin, yMin, yMax = pathsToGrid(input)
  sandUnit = 0
  while True:
    pos = (500 - xMin, 0 - yMin)
    while True:
      for dir in (0, 1), (-1, 1), (1, 1):
        newPos = (pos[0] + dir[0], pos[1] + dir[1])
        if newPos[1] > yMax:
          continue
        if not grid[newPos[1]][newPos[0]]:
          pos = newPos
          break
      else:
        if pos[1] == 0:
          return sandUnit + 1
        grid[pos[1]][pos[0]] = True
        break
    sandUnit += 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1406

print("The second star is : {}".format(secondStar(input)))
# The second star is : 20870
