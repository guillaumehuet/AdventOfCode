from copy import deepcopy

def readInput(file):
  return [[int(c) for c in line.split(',')] for line in open(file).read().splitlines()]

def manhattan(a, b):
  return (abs(b[0] - a[0]) + abs(b[1] - a[1]))

def firstStar(input):
  workingInput = deepcopy(input)
  allX = [c[0] for c in workingInput]
  allY = [c[1] for c in workingInput]
  minX = min(allX)
  minY = min(allY)
  maxX = max(allX) - minX
  maxY = max(allY) - minY
  workingInput = [[c[0] - minX, c[1] - minY] for c in workingInput]
  grid = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
  infiniteSectors = set()
  for x in range(maxX + 1):
    for y in range(maxY + 1):
      distances = [manhattan((x,y), place) for place in workingInput]
      closest = [i for i, j in enumerate(distances) if j == min(distances)]
      if (len(closest) == 1):
        value = closest[0] + 1
        # Every sector on the exterior is infinite
        if x == 0 or x == maxX or y == 0 or y == maxY:
          infiniteSectors.add(value)
        if value not in infiniteSectors:
          grid[y][x] = value
  return largestSector(grid)

def largestSector(grid):
  maxValue = max(max(line) for line in grid)
  count = [0 for _ in range(maxValue + 1)]
  for line in grid:
    for case in line:
      count[case] += 1
  count[0] = 0
  return max(count)

def gridToStr(grid):
  result = ''
  for line in grid:
    result += '\n'
    for c in line:
      result += str(c)
  return result

def secondStar(input):
  distanceThreshold = 10000
  workingInput = deepcopy(input)
  allX = [c[0] for c in workingInput]
  allY = [c[1] for c in workingInput]
  minX = min(allX)
  minY = min(allY)
  maxX = max(allX) - minX
  maxY = max(allY) - minY
  workingInput = [[c[0] - minX, c[1] - minY] for c in workingInput]
  grid = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
  infiniteSectors = set()
  for x in range(maxX + 1):
    for y in range(maxY + 1):
      distance = sum([manhattan((x,y), place) for place in workingInput])
      if (distance < distanceThreshold):
        grid[y][x] = 1
  return largestSector(grid)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4186

print("The second star is : {}".format(secondStar(input)))
# The second star is : 45509
