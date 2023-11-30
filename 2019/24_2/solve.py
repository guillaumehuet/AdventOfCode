from pathlib import Path
from collections import defaultdict

def readInput(file):
  return tuple(tuple(True if c == '#' else False for c in line) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def gridBiodiversityRating(grid):
  result = 0
  power = 0
  for line in grid:
    for c in line:
      if c:
        result += 2**power
      power += 1
  return result

def printGrid(grid):
  for line in grid:
    print("".join('#' if c else '.' for c in line))

def printRecursiveGrid(grid):
  for depth in grid:
    print("Depth " + str(depth) + " :")
    for line in grid[depth]:
      print("".join('#' if c else '.' for c in line))
    print()

def neighbors(x, y, width, height):
  result = []
  if x > 0:
    result.append((x - 1, y))
  if x < width - 1:
    result.append((x + 1, y))
  if y > 0:
    result.append((x, y - 1))
  if y < height - 1:
    result.append((x, y + 1))
  return tuple(result)

def recursiveNeighbors(x, y, z, width, height):
  result = []
  centerX = width // 2
  centerY = height // 2
  if x == centerX and y == centerY:
    return result
  if x > 0:
    if y != centerY or x != centerX + 1:
      result.append((x - 1, y, z))
  else:
    result.append((centerX - 1, centerY, z - 1))
  if x < width - 1:
    if y != centerY or x != centerX - 1:
      result.append((x + 1, y, z))
  else:
    result.append((centerX + 1, centerY, z - 1))
  if y > 0:
    if y != centerY + 1 or  x != centerX:
      result.append((x, y - 1, z))
  else:
    result.append((centerX, centerY - 1, z - 1))
  if y < height - 1:
    if y != centerY - 1 or  x != centerX:
      result.append((x, y + 1, z))
  else:
    result.append((centerX, centerY + 1, z - 1))

  if y == centerY:
    if x == centerX - 1:
      for i in range(height):
        result.append((0, i, z + 1))
    elif x == centerX + 1:
      for i in range(height):
        result.append((width - 1, i, z + 1))
  if x == centerX:
    if y == centerY - 1:
      for i in range(width):
        result.append((i, 0, z + 1))
    elif y == centerY + 1:
      for i in range(width):
        result.append((i, height - 1, z + 1))
  
  return tuple(result)

def recursiveStep(grid, minDepth, maxDepth):
  width = len(grid[0][0])
  height = len(grid[0])
  result = defaultdict(lambda: [[False for _ in range(width)] for _ in range(height)])
  for z in range(minDepth - 1, maxDepth + 2):
    for y in range(height):
      for x in range(width):
        if len([grid[z_][y_][x_] for x_, y_, z_ in recursiveNeighbors(x, y, z, width, height)]) > 8:
          print([grid[z_][y_][x_] for x_, y_, z_ in recursiveNeighbors(x, y, z, width, height)])
        nNeighbors = sum(grid[z_][y_][x_] for x_, y_, z_ in recursiveNeighbors(x, y, z, width, height))
        if grid[z][y][x] and nNeighbors != 1:
          result[z][y][x] = False
        elif not grid[z][y][x] and 1 <= nNeighbors <= 2:
          result[z][y][x] = True
        else:
          result[z][y][x] = grid[z][y][x]
      result[z][y] = tuple(result[z][y])
    result[z] = tuple(result[z])
  return result

def recursiveSize(grid):
  result = 0
  for depth in grid:
    for line in grid[depth]:
      result += sum(line)
  return result

def step(grid):
  result = []
  width = len(grid[0])
  height = len(grid)
  for y in range(height):
    result.append([])
    for x in range(width):
      nNeighbors = sum(grid[y_][x_] for x_, y_ in neighbors(x, y, width, height))
      if grid[y][x] and nNeighbors != 1:
        result[-1].append(False)
      elif not grid[y][x] and 1 <= nNeighbors <= 2:
        result[-1].append(True)
      else:
        result[-1].append(grid[y][x])
    result[-1] = tuple(result[-1])
  result = tuple(result)
  return result

def firstStar(input):
  seen = set()
  grid = input
  while True:
    r = gridBiodiversityRating(grid)
    if r in seen:
      return r
    seen.add(r)
    grid = step(grid)

def secondStar(input):
  width = len(input[0])
  height = len(input)
  grid = defaultdict(lambda: [[False for _ in range(width)] for _ in range(height)])
  minDepth = 0
  maxDepth = 0
  grid[0] = input
  for _ in range(200):
    grid = recursiveStep(grid, minDepth, maxDepth)
    minDepth -= 1
    maxDepth += 1
  return recursiveSize(grid)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 28717468

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2014
