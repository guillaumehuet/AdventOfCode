from pathlib import Path
from copy import deepcopy

def readInput(file):
  return [[int(n) for n in line] for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def neighboors(x, y, xmax, ymax):
  allneighboors = ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))
  result = []
  for xn, yn in allneighboors:
    if 0 <= xn < xmax and 0 <= yn < ymax:
      result.append((xn, yn))
  return result

def printGrid(grid):
  for line in grid:
    print("".join(str(n) for n in line))
  print()

def step(grid):
  flashes = 0
  ymax = len(grid)
  xmax = len(grid[0])
  for y in range(ymax):
    for x in range(xmax):
      grid[y][x] += 1
  remaining = True
  while remaining:
    remaining = False
    for y in range(ymax):
      for x in range(xmax):
        if grid[y][x] >= 10:
          remaining = True
          flashes += 1
          grid[y][x] = 0
          for xn, yn in neighboors(x, y, xmax, ymax):
            if grid[yn][xn] > 0:
              grid[yn][xn] += 1
  return flashes

def firstStar(input):
  grid = deepcopy(input)
  flashes = 0
  generations = 100
  for s in range(generations):
    flashes += step(grid)
  return flashes

def secondStar(input):
  grid = deepcopy(input)
  flashes = 0
  generation = 0
  while True:
    flashes = step(grid)
    generation += 1
    if flashes == 100:
      return generation

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1620

print("The second star is : {}".format(secondStar(input)))
# The second star is : 371
