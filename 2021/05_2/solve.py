from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    start, end = line.split(' -> ')
    start = tuple(int(n) for n in start.split(','))
    end = tuple(int(n) for n in end.split(','))
    result.append((start, end))
  return tuple(result)

def printGrid(grid):
  for line in grid:
    for n in line:
      if n == 0:
        print('.', end='')
      else:
        print(n, end='')
    print()

def firstStar(input):
  filteredX = []
  filteredY = []
  for line in input:
    if line[0][0] == line[1][0]:
      filteredY.append(line)
    elif line[0][1] == line[1][1]:
      filteredX.append(line)

  filteredX = tuple(filteredX)
  filteredY = tuple(filteredY)
  maxX = 0
  maxY = 0
  for line in filteredX:
    maxX = max(maxX, line[0][0], line[1][0])
    maxY = max(maxY, line[1][0], line[1][1])
  for line in filteredY:
    maxX = max(maxX, line[0][0], line[1][0])
    maxY = max(maxY, line[1][0], line[1][1])
  grid = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
  for line in filteredX:
    minX = min(line[0][0], line[1][0])
    maxX = max(line[0][0], line[1][0])
    y = line[0][1]
    for x in range(minX, maxX + 1):
      grid[y][x] += 1
  for line in filteredY:
    minY = min(line[0][1], line[1][1])
    maxY = max(line[0][1], line[1][1])
    x = line[0][0]
    for y in range(minY, maxY + 1):
      grid[y][x] += 1
  result = 0
  for line in grid:
    for n in line:
      if n > 1:
        result += 1
  return result

def secondStar(input):
  maxX = 0
  maxY = 0
  for line in input:
    maxX = max(maxX, line[0][0], line[1][0])
    maxY = max(maxY, line[1][0], line[1][1])
  grid = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
  for line in input:
    minX = min(line[0][0], line[1][0])
    maxX = max(line[0][0], line[1][0])
    minY = min(line[0][1], line[1][1])
    maxY = max(line[0][1], line[1][1])
    nPoints = max(maxX - minX, maxY - minY)
    for p in range(nPoints + 1):
      x = line[0][0] + ((line[1][0] - line[0][0])*p)//nPoints
      y = line[0][1] + ((line[1][1] - line[0][1])*p)//nPoints
      grid[y][x] += 1
  result = 0
  for line in grid:
    for n in line:
      if n > 1:
        result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 8350

print("The second star is : {}".format(secondStar(input)))
# The second star is : 19374
