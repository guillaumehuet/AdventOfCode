from pathlib import Path
import heapq

def readInput(file):
  maze = []
  keys1 = dict()
  keys2 = dict()
  doors = dict()
  y = 0
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    x = 0
    maze.append([])
    for c in line:
      if c == '.':
        maze[-1].append(True)
      elif c == '#':
        maze[-1].append(False)
      elif c == '@':
        maze[-1].append(True)
        origin1 = ((x, y),)
        origin2 = ((x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1))
        keys1[(x, y)] = c
        for i, (x_, y_) in enumerate(origin2):
          keys2[(x_, y_)] = c + str(i)
      elif 'a' <= c <= 'z':
        maze[-1].append(True)
        keys1[(x, y)] = c
        keys2[(x, y)] = c
      elif 'A' <= c <= 'Z':
        maze[-1].append(True)
        doors[(x, y)] = c.lower()
      else:
        return "Unknown character : " + c
      x += 1
    y += 1
  maze1 = tuple(tuple(line) for line in maze)
  x, y = origin1[0]
  maze[y][x] = False
  maze[y - 1][x] = False
  maze[y + 1][x] = False
  maze[y][x - 1] = False
  maze[y][x + 1] = False
  maze2 = tuple(tuple(line) for line in maze)
  return keys1, keys2, doors, origin1, origin2, maze1, maze2

def printMaze(maze):
  for line in maze:
    print("".join(' ' if walkable else '#' for walkable in line))

def around(position):
  neighbors = ((0, -1), (0, 1), (-1, 0), (1, 0))
  return tuple((position[0] + x, position[1] + y) for x, y in neighbors)

def boundaryKeys(origin, maze, doors, visited):
  result = set()
  for position in around(origin):
    if maze[position[1]][position[0]]:
      newState = position + (origin[2],)
      if position in doors:
        newState = position + (origin[2] | {doors[position]},)
      if position not in visited:
        result.add(newState)
  return result

def reachableKeys(origin, keys, doors, maze):
  result = set()
  visited = set()
  originKey = keys[origin]
  state = origin + (frozenset(),)
  visited.add(origin)
  distance = 0
  nextBoundary = boundaryKeys(state, maze, doors, visited)
  while nextBoundary:
    distance += 1
    currBoundary = nextBoundary
    nextBoundary = set()
    for state in currBoundary:
      position = state[0:2]
      neededKeys = state[2]
      if state[0:2] in keys:
        result.add((distance, frozenset({originKey, keys[position]}), neededKeys))
      nextBoundary |= boundaryKeys(state, maze, doors, visited)
    for state in currBoundary:
      visited.add(state[0:2])
  return result

def findAllKeyPaths(keys, doors, maze):
  result = set()
  for origin in keys:
    result |= reachableKeys(origin, keys, doors, maze)
  return result

def findNeighboorStates(position, reachedKeys, keyPaths):
  result = set()
  for distance, keys, neededKeys in keyPaths:
    for origin in position:
      if origin in keys:
        newKey = next(iter(keys - {origin}))
        if newKey not in reachedKeys:
          destination = tuple(p if p != origin else newKey for p in position)
          if reachedKeys > neededKeys:
            result.add((distance, frozenset(reachedKeys | {newKey}), destination))
  return result

def findAllKeys(origin, keys, doors, maze):
  position = tuple(keys[position] for position in origin)
  reachedKeys = frozenset(position)
  visited = set()
  allKeys = set(keys.values())
  keyPaths = findAllKeyPaths(keys, doors, maze)
  queue = [(0, reachedKeys, position)]
  while queue:
    previousDistance, previousReachedKeys, previousPosition = heapq.heappop(queue)
    if previousReachedKeys == allKeys:
      return previousDistance
    if (previousPosition, previousReachedKeys) in visited:
      continue
    for distance, reachedKeys, position in findNeighboorStates(previousPosition, previousReachedKeys, keyPaths):
      heapq.heappush(queue, (previousDistance + distance, reachedKeys, position))
    visited.add((previousPosition, previousReachedKeys))
  return "Impossible to reach all keys"

def firstStar(input):
  keys, _, doors, origin, _, maze, _ = input
  return findAllKeys(origin, keys, doors, maze)

def secondStar(input):
  _, keys, doors, _, origin, _, maze = input
  return findAllKeys(origin, keys, doors, maze)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3546

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1988
