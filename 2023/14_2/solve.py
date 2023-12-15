from pathlib import Path

def readInput(file):
  cubeRocks = set()
  roundRocks = set()
  width = 0
  height = 0
  for i, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    for j, c in enumerate(line):
      if c =='#':
        cubeRocks.add((i, j))
      elif c == 'O':
        roundRocks.add((i, j))
    width = j
  height = i
  return roundRocks, cubeRocks, width, height

def tiltNorth(roundRocks, cubeRocks):
  result = set()
  for r in roundRocks:
    while r not in cubeRocks and r[0] > -1:
      r = (r[0] - 1, r[1])
    r = (r[0] + 1, r[1])
    while r in result:
      r = (r[0] + 1, r[1])
    result.add(r)
  return result

def tiltWest(roundRocks, cubeRocks):
  result = set()
  for r in roundRocks:
    while r not in cubeRocks and r[1] > -1:
      r = (r[0], r[1] - 1)
    r = (r[0], r[1] + 1)
    while r in result:
      r = (r[0], r[1] + 1)
    result.add(r)
  return result

def tiltSouth(roundRocks, cubeRocks, height):
  result = set()
  for r in roundRocks:
    while r not in cubeRocks and r[0] < height + 1:
      r = (r[0] + 1, r[1])
    r = (r[0] - 1, r[1])
    while r in result:
      r = (r[0] - 1, r[1])
    result.add(r)
  return result

def tiltEast(roundRocks, cubeRocks, width):
  result = set()
  for r in roundRocks:
    while r not in cubeRocks and r[1] < width + 1:
      r = (r[0], r[1] + 1)
    r = (r[0], r[1] - 1)
    while r in result:
      r = (r[0], r[1] - 1)
    result.add(r)
  return result

def totalLoadNorth(roundRocks, height):
  result = 0
  for r in roundRocks:
    result += height + 1 - r[0]
  return result

def printRocks(roundRocks, cubeRocks, width, height):
  for i in range(height + 1):
    for j in range(width + 1):
      if (i, j) in cubeRocks:
        print('#', end='')
      elif (i, j) in roundRocks:
        print('O', end='')
      else:
        print('.', end='')
    print()
  print()

def firstStar(input):
  roundRocks, cubeRocks, width, height = input
  roundRocks = tiltNorth(roundRocks, cubeRocks)
  return totalLoadNorth(roundRocks, height)

def secondStar(input):
  roundRocks, cubeRocks, width, height = input
  visited = set()
  cycle = 0
  startCycle = None
  cycleLength = None
  stopCycle = None
  while True:
    if startCycle is None:
      if frozenset(roundRocks) in visited:
        startCycle = cycle
        visited = set()
    elif stopCycle is None:
      if frozenset(roundRocks) in visited:
        cycleLength = cycle - startCycle
        stopCycle = (1000000000 - startCycle) % cycleLength
    else:
      if (cycle - startCycle) % cycleLength == stopCycle:
        return totalLoadNorth(roundRocks, height)
    cycle += 1
    visited.add(frozenset(roundRocks))
    roundRocks = tiltNorth(roundRocks, cubeRocks)
    roundRocks = tiltWest(roundRocks, cubeRocks)
    roundRocks = tiltSouth(roundRocks, cubeRocks, height)
    roundRocks = tiltEast(roundRocks, cubeRocks, width)
  

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 108857

print("The second star is : {}".format(secondStar(input)))
# The second star is : 95273
