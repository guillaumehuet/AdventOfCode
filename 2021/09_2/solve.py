from pathlib import Path

def readInput(file):
  return tuple(tuple(int(n) for n in line) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def neighboors(x, y, xmax, ymax):
  result = []
  if x > 0:
    result.append((x - 1, y))
  if x < xmax - 1:
    result.append((x + 1, y))
  if y > 0:
    result.append((x, y - 1))
  if y < ymax - 1:
    result.append((x, y + 1))
  return result

def bassinSize(grid, x, y, xmax, ymax):
  coords = {(x, y)}
  edge = set(neighboors(x, y, xmax, ymax))
  while edge:
    currX, currY = edge.pop()
    if grid[currY][currX] != 9:
      coords.add((currX, currY))
      edge |= set(neighboors(currX, currY, xmax, ymax))
      edge -= coords
  return len(coords)

def firstStar(input):
  result = 0
  xmax = len(input[0])
  ymax = len(input)
  for y in range(ymax):
    for x in range(xmax):
      value = input[y][x]
      for xn, yn in neighboors(x, y, xmax, ymax):
        if input[yn][xn] <= value:
          break
      else:
        result += 1 + value
  return result

def secondStar(input):
  bassins = []
  xmax = len(input[0])
  ymax = len(input)
  for y in range(ymax):
    for x in range(xmax):
      value = input[y][x]
      for xn, yn in neighboors(x, y, xmax, ymax):
        if input[yn][xn] <= value:
          break
      else:
        bassins.append(bassinSize(input, x, y, xmax, ymax))
  maxBassins = sorted(bassins, reverse=True)[:3]
  result = 1
  for b in maxBassins:
    result *= b
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 594

print("The second star is : {}".format(secondStar(input)))
# The second star is : 858494
