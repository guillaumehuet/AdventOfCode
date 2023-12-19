from pathlib import Path
from bisect import insort

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append(tuple(int(n) for n in line))
  return tuple(result)

def step(position, direction):
  return (position[0] + direction[0], position[1] + direction[1])

def heuristic(position, end):
  return abs(position[0] - end[0]) + abs(position[1] - end[1])

def opposite(direction):
  return (-direction[0], -direction[1])

def minimizeLoss(maze, minStraight = 0, maxStraight = 3, debug = False):
  height = len(maze)
  width = len(maze[0])
  start = (0, 0)
  end = (height - 1, width - 1)
  h = heuristic(start, end)
  boundary = [(h, 0, start, right, 1), (h, 0, start, down, 1),]
  visited = set()
  trackback = dict()
  while boundary:
    _, distance, position, direction, repeats = boundary.pop(0)
    if (position, direction, repeats) in visited:
      continue
    visited.add((position, direction, repeats))
    if position == end and minStraight <= repeats <= maxStraight:
      if debug:
        node = (distance, position, direction, repeats)
        while node in trackback:
          print(node)
          node = trackback[node]
        print(node)
      return distance
    for newDir in (up, down, left, right):
      if newDir == opposite(direction):
        continue
      if newDir == direction:
        if maxStraight <= repeats:
          continue
        newRepeats = repeats + 1
      else:
        if repeats < minStraight:
          continue
        newRepeats = 1
      newPos = step(position, newDir)
      if 0 <= newPos[0] < height and 0 <= newPos[1] < width and (newPos, newDir, newRepeats) not in visited:
        newDistance = distance + maze[newPos[0]][newPos[1]]
        trackback[(newDistance, newPos, newDir, newRepeats)] = (distance, position, direction, repeats)
        insort(boundary, (newDistance + heuristic(newPos, end), newDistance, newPos, newDir, newRepeats))

def firstStar(input):
  return minimizeLoss(input)

def secondStar(input):
  return minimizeLoss(input, 4, 10)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 791

print("The second star is : {}".format(secondStar(input)))
# The second star is : 900
