from pathlib import Path
from bisect import bisect

def readInput(file):
  result = []
  for i, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    for j, cell in enumerate(line):
      if cell == '#':
        result.append((i, j))
  return result

def expand(galaxies, factor):
  minX = galaxies[0][0]
  maxX = minX
  minY = galaxies[0][1]
  maxY = minY
  for g in galaxies:
    minX = min(minX, g[0])
    maxX = max(maxX, g[0])
    minY = min(minY, g[1])
    maxY = max(maxY, g[1])
  missingX = []
  missingY = []
  for x in range(minX, maxX):
    if x not in (g[0] for g in galaxies):
      missingX.append(x)
  for y in range(minY, maxY):
    if y not in (g[1] for g in galaxies):
      missingY.append(y)
  result = []
  for g in galaxies:
    newX = (factor - 1)*bisect(missingX, g[0]) + g[0]
    newY = (factor - 1)*bisect(missingY, g[1]) + g[1]
    result.append((newX, newY))
  return result

def distance(g1, g2):
  return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def sumOfDistances(galaxies):
  result = 0
  for i, gi in enumerate(galaxies):
    for j, gj in enumerate(galaxies):
      if j > i:
        result += distance(gi, gj)
  return result

def firstStar(input):
  galaxies = expand(input, 2)
  return sumOfDistances(galaxies)

def secondStar(input):
  galaxies = expand(input, 1000000)
  return sumOfDistances(galaxies)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 9609130

print("The second star is : {}".format(secondStar(input)))
# The second star is : 702152204842
