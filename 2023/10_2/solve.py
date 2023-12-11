from pathlib import Path

directions = {'up' : (-1, 0), 'down' : (1, 0), 'left' : (0, -1), 'right' : (0, 1)}
pipes = {'-' : {'left' : 'left', 'right' : 'right'},
         '|' : {'up' : 'up', 'down' : 'down'},
         '7' : {'up' : 'left', 'right' : 'down'},
         'J' : {'down' : 'left', 'right' : 'up'},
         'L' : {'down' : 'right', 'left' : 'up'},
         'F' : {'up' : 'right', 'left' : 'down'}}

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append([])
    for c in line:
      result[-1].append(c)
      if c == 'S':
        start = (len(result) - 1, len(result[-1]) - 1)
    result[-1] = tuple(result[-1])
  return tuple(result), start

def neighboors(cell):
  result = []
  for d in directions:
    result.append(((cell[0] + directions[d][0], cell[1] + directions[d][1]), d))
  return tuple(result)

def around(coord, grid):
  result = []
  for d in directions.values():
    newY = coord[0] + d[0]
    newX = coord[1] + d[1]
    if 0 <= newY < len(grid) and 0 <= newX < len(grid[0]):
      if grid[newY][newX] != '*':
        result.append((newY, newX))
  return result

def twiceGrid(grid):
  xLen = len(grid[0])
  yLen = len(grid)
  result = []
  for _ in range(yLen):
    result.append([])
    for _ in range(xLen):
      result[-1] += ['.', ' ']
    result.append([' ']*2*xLen)
  return result

def firstStar(input):
  grid, start = input
  loopNext = []
  for n in neighboors(start):
    if n[1] in pipes[grid[n[0][0]][n[0][1]]]:
      loopNext.append(n)
  loopMiddleDistance = 1
  while loopNext[0][0] != loopNext[1][0]:
    loopMiddleDistance += 1
    for i in range(2):
      d = pipes[grid[loopNext[i][0][0]][loopNext[i][0][1]]][loopNext[i][1]]
      loopNext[i] = ((loopNext[i][0][0] + directions[d][0], loopNext[i][0][1] + directions[d][1]), d)
  return loopMiddleDistance

def secondStar(input):
  grid, start = input
  twice = twiceGrid(grid)
  twice[2*start[0]][2*start[1]] = '*'
  loopNext = []
  for n in neighboors(start):
    if n[1] in pipes[grid[n[0][0]][n[0][1]]]:
      loopNext.append(n)
      for i in range(2):
        twice[2*start[0] + (i + 1)*directions[n[1]][0]][2*start[1] + (i + 1)*directions[n[1]][1]] = '*'
  while loopNext[0][0] != loopNext[1][0]:
    for i in range(2):
      d = pipes[grid[loopNext[i][0][0]][loopNext[i][0][1]]][loopNext[i][1]]
      for j in range(2):
        twice[2*loopNext[i][0][0] + (j + 1)*directions[d][0]][2*loopNext[i][0][1] + (j + 1)*directions[d][1]] = '*'
      loopNext[i] = ((loopNext[i][0][0] + directions[d][0], loopNext[i][0][1] + directions[d][1]), d)
  coord = (0, 0)
  twice[0][0] = ' '
  visited = set()
  boundary = {coord}
  while boundary:
    coord = boundary.pop()
    visited.add(coord)
    for next in around(coord, twice):
      if next not in visited:
        twice[next[0]][next[1]] = ' '
        boundary.add(next)
  result = 0
  for line in twice:
    result += line.count('.')
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 6714

print("The second star is : {}".format(secondStar(input)))
# The second star is : 429
