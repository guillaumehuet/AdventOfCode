from pathlib import Path

def readInput(file):
  stillCoords = True
  coords = []
  folds = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      stillCoords = False
    elif stillCoords:
      a, b = line.split(',')
      coords.append((int(a), int(b)))
    else:
      a, b = line.split('=')
      folds.append((a[-1], int(b)))
  return tuple(coords), tuple(folds)

def printGrid(grid):
  for line in grid:
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

def toGrid(input):
  xmax = 0
  ymax = 0
  for x, y in input[0]:
    xmax = max(xmax, x)
    ymax = max(ymax, y)
  grid = [[False for _ in range(xmax + 1)] for _ in range(ymax + 1)]
  for x, y in input[0]:
    grid[y][x] = True
  return grid

def foldX(grid, column):
  width = len(grid[0])
  height = len(grid)
  for y in range(height):
    for x in range(column + 1, width):
      if grid[y][x]:
        grid[y][2*column - x] = True
    grid[y] = grid[y][:column]
  return grid

def foldY(grid, row):
  width = len(grid[0])
  height = len(grid)
  for y in range(row + 1, height):
    for x in range(width):
      if grid[y][x]:
        grid[2*row - y][x] = True
  grid = grid[:row]
  return grid

def count(grid):
  result = 0
  for line in grid:
    for c in line:
      if c:
        result += 1
  return result


def firstStar(input):
  grid = toGrid(input)
  fold = input[1][0]
  if fold[0] == 'x':
    grid = foldX(grid, fold[1])
  else:
    grid = foldY(grid, fold[1])
  return count(grid)


def secondStar(input):
  grid = toGrid(input)
  folds = input[1]
  for fold in folds:
    if fold[0] == 'x':
      grid = foldX(grid, fold[1])
    else:
      grid = foldY(grid, fold[1])
  printGrid(grid)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 763

print("The second star is : {}".format(secondStar(input)))
# The second star is : RHALRCRA
###..#..#..##..#....###...##..###...##..
#..#.#..#.#..#.#....#..#.#..#.#..#.#..#.
#..#.####.#..#.#....#..#.#....#..#.#..#.
###..#..#.####.#....###..#....###..####.
#.#..#..#.#..#.#....#.#..#..#.#.#..#..#.
#..#.#..#.#..#.####.#..#..##..#..#.#..#.
