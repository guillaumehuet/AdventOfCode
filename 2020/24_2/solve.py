from pathlib import Path
from collections import defaultdict

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def decodePath(path):
  x = 0
  y = 0
  i = 0
  while i < len(path):
    if path[i] in 'ew':
      if path[i] == 'e':
        x += 1
      else:
        x -= 1
      i += 1
    else:
      if path[i] == 'n':
        y -= 1
        if path[i + 1] == 'w':
          x -= 1
      else:
        y += 1
        if path[i + 1] == 'e':
          x += 1
      i += 2
  return x, y

def neighbors(coord):
  x, y = coord
  return ((x - 1, y - 1), (x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1), (x + 1, y + 1))

def round(tileSet):
  newTileSet = defaultdict(lambda: False)
  tileSetCopy = tileSet.copy()
  for tile in tileSetCopy:
    for n in neighbors(tile):
      if n not in newTileSet:
        count = sum(tileSet[nn] for nn in neighbors(n))
        if tileSet[n]:
          if count in (1, 2):
            newTileSet[n] = True
        else:
          if count == 2:
            newTileSet[n] = True
  return newTileSet

def firstStar(input):
  flipedTiles = set()
  for path in input:
    x, y = decodePath(path)
    if (x, y) in flipedTiles:
      flipedTiles.remove((x, y))
    else:
      flipedTiles.add((x, y))
  return len(flipedTiles)

def secondStar(input):
  flipedTiles = set()
  for path in input:
    x, y = decodePath(path)
    if (x, y) in flipedTiles:
      flipedTiles.remove((x, y))
    else:
      flipedTiles.add((x, y))
  tileSet = defaultdict(lambda: False)
  for x, y in flipedTiles:
    tileSet[(x, y)] = True
  for _ in range(100):
    tileSet = round(tileSet)
  
  return sum(tileSet.values())

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 354

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3608
