from bisect import insort

def readInput(file):
  grid = []
  start = None
  end = None
  x = 0
  y = 0
  for line in open(file).read().splitlines():
    grid.append([])
    for c in line:
      if c == 'S':
        c = 'a'
        start = (x, y)
      elif c == 'E':
        c = 'z'
        end = (x, y)
      grid[-1].append(ord(c) - ord('a'))
      x += 1
    x = 0
    y += 1
  return start, end, grid

def neighboors(grid, position, visited, inversed = False):
  result = list()
  width = len(grid[0])
  height = len(grid)
  elevation = grid[position[2]][position[1]]
  for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    x = position[1] + direction[0]
    y = position[2] + direction[1]
    if (x, y) in visited:
      continue
    if 0 <= x < width and 0 <= y < height:
      newElevation = grid[y][x]
      if not inversed:
        if newElevation <= elevation + 1:
          result.append((position[0] + 1, x, y))
      else:
        if elevation <= newElevation + 1:
          result.append((position[0] + 1, x, y))
  return result

def firstStar(input):
  start, end, grid = input
  visited = {start}
  boundary = list(neighboors(grid, (0,) + start, visited))
  while True:
    position = boundary.pop(0)
    if position[1:] == end:
      return position[0]
    if position[1:] in visited:
      continue
    visited.add(position[1:])
    boundary += neighboors(grid, position, visited)

def secondStar(input):
  start, end, grid = input
  visited = {end}
  boundary = list(neighboors(grid, (0,) + end, visited, True))
  while True:
    position = boundary.pop(0)
    if grid[position[2]][position[1]] == 0:
      return position[0]
    if position[1:] in visited:
      continue
    visited.add(position[1:])
    boundary += neighboors(grid, position, visited, True)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 440

print("The second star is : {}".format(secondStar(input)))
# The second star is : 439
