from pathlib import Path
from collections import defaultdict

def readInput(file):
  maze = []
  letters = dict()
  y = 0
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    x = 0
    maze.append([])
    for c in line:
      if c == '.':
        maze[-1].append(True)
      elif c in ['#', ' ']:
        maze[-1].append(False)
      elif 'A' <= c <= 'Z':
        maze[-1].append(False)
        letters[(x, y)] = c
      else:
        return "Unknown character : " + c
      x += 1
    y += 1
  maze = tuple(tuple(line) for line in maze)

  mazeHeight = len(maze)
  mazeWidth = len(maze[0])

  portalsPositions = defaultdict(lambda:set())
  for x, y in letters:
    for dCoord in (-1, 1):
      if (x + dCoord, y) in letters:
        firstLetter = (min(x, x + dCoord), y)
        secondLetter = (max(x, x + dCoord), y)
        direction = (1, 0)
      elif (x, y + dCoord) in letters:
        firstLetter = (x, min(y, y + dCoord))
        secondLetter = (x, max(y, y + dCoord))
        direction = (0, 1)
    portalName = letters[firstLetter] + letters[secondLetter]
    if firstLetter[0] == 0: # Portal in on the left
      portalPosition = (secondLetter[0] + 1, secondLetter[1])
    elif secondLetter[0] == mazeWidth - 1: # Portal in on the right
      portalPosition = (firstLetter[0] - 1, firstLetter[1])
    elif firstLetter[1] == 0: # Portal in on the top
      portalPosition = (secondLetter[0], secondLetter[1] + 1)
    elif secondLetter[1] == mazeHeight - 1: # Portal in on the bottom
      portalPosition = (firstLetter[0], firstLetter[1] - 1)
    else:
      for dCoord in (-1, 2):
        portalPosition = (firstLetter[0] + dCoord*direction[0], firstLetter[1] + dCoord*direction[1])
        if maze[portalPosition[1]][portalPosition[0]]:
          break
    portalsPositions[portalName].add(portalPosition)
  
  origin = portalsPositions['AA'].pop() + (0,)
  destination = portalsPositions['ZZ'].pop() + (0,)

  portalsOuter = dict()
  portalsInner = dict()

  for portal in portalsPositions.values():
    for portalOrigin in portal:
      portalDestination = (portal - {portalOrigin}).pop()
      if 2 in portalOrigin or portalOrigin[0] == mazeWidth - 3 or portalOrigin[1] == mazeHeight - 3:
        portalsOuter[portalOrigin] = portalDestination
      else:
        portalsInner[portalOrigin] = portalDestination

  return origin, destination, maze, portalsInner, portalsOuter

def printMaze(maze):
  for line in maze:
    print("".join(' ' if walkable else '#' for walkable in line))

def around(position):
  neighbors = ((0, -1), (0, 1), (-1, 0), (1, 0))
  return tuple((position[0] + x, position[1] + y, position[2]) for x, y in neighbors)

def boundary(origin, maze, portalsInner, portalsOuter, visited, depth = False):
  result = set()
  for position in around(origin):
    if maze[position[1]][position[0]]:
      if position not in visited:
        result.add(position)
  if origin[0:2] in portalsInner:
    position = portalsInner[origin[0:2]]
    if position not in visited:
      if depth:
        result.add(position + (origin[2] + 1,))
      else:
        result.add(position + (origin[2],))
  if origin[0:2] in portalsOuter:
    position = portalsOuter[origin[0:2]]
    if position not in visited:
      if depth:
        if origin[2] > 0:
          result.add(position + (origin[2] - 1,))
      else:
        result.add(position + (origin[2],))
  return result

def findDestination(origin, destination, portalsInner, portalsOuter, maze, depth = False):
  visited = set()
  position = origin
  visited.add(position)
  distance = 0
  nextBoundary = boundary(position, maze, portalsInner, portalsOuter, visited, depth)
  while nextBoundary:
    distance += 1
    currBoundary = nextBoundary
    nextBoundary = set()
    for position in currBoundary:
      if position == destination:
        return distance
      nextBoundary |= boundary(position, maze, portalsInner, portalsOuter, visited, depth)
    visited |= currBoundary
  return visited

def firstStar(input):
  origin, destination, maze, portalsInner, portalsOuter = input
  return findDestination(origin, destination, portalsInner, portalsOuter, maze)

def secondStar(input):
  origin, destination, maze, portalsInner, portalsOuter = input
  return findDestination(origin, destination, portalsInner, portalsOuter, maze, True)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 490

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5648
