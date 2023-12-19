from pathlib import Path
from bisect import insort

def readInput(file):
  blizzards = {'^' : set(), 'v' : set(), '<' : set(), '>' : set()}
  for i, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    for j, c in enumerate(line):
      if c in '<>v^':
        blizzards[c].add((i - 1, j - 1))
  return blizzards, i - 1, j - 1

def step(position, direction):
  return (position[0] + direction[0], position[1] + direction[1])

def collision(position, time, height, width, blizzards):
  if ((position[0] - time) % height, position[1]) in blizzards['v']:
    return True
  if ((position[0] + time) % height, position[1]) in blizzards['^']:
    return True
  if (position[0], (position[1] - time) % width) in blizzards['>']:
    return True
  if (position[0], (position[1] + time) % width) in blizzards['<']:
    return True
  return False

def neighboors(position, time, height, width, blizzards):
  result = []
  for dir in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
    newPos = step(position, dir)
    if (dir == (0, 0) or (0 <= newPos[0] < height and 0 <= newPos[1] < width)) and not collision(newPos, time, height, width, blizzards):
      result.append(newPos)
  return result

def heuristic(position, end):
  return abs(position[0] - end[0]) + abs(position[1] - end [1])

def reachGoal(blizzards, height, width, reversed = False, startTime = 0):
  if reversed:
    start = (height, width - 1)
    end = (0, 0)
  else:
    start = (-1, 0)
    end = (height - 1, width - 1)
  boundary = [(heuristic(start, end) + startTime, startTime, start)]
  visited = set()
  while boundary:
    _, time, position = boundary.pop(0)
    if position == end:
      return time + 1
    if (time, position) in visited:
      continue
    visited.add((time, position))
    newTime = time + 1
    for newPos in neighboors(position, newTime, height, width, blizzards):
      insort(boundary, (heuristic(newPos, end) + newTime, newTime, newPos))

def firstStar(input):
  blizzards, height, width = input
  return reachGoal(blizzards, height, width)

def secondStar(input):
  blizzards, height, width = input
  time = reachGoal(blizzards, height, width)
  time = reachGoal(blizzards, height, width, True, time)
  return reachGoal(blizzards, height, width, False, time)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 221

print("The second star is : {}".format(secondStar(input)))
# The second star is : 739
