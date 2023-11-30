from pathlib import Path

from bisect import insort
from collections import deque

def readInput(file):
  return [[int(n) for n in line] for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def expandCavern(cavern):
  xmax = len(cavern[0])
  ymax = len(cavern)
  for y in range(ymax):
    for delta in range(1, 5):
      for x in range(xmax):
        cavern[y].append((cavern[y][x] + delta - 1) % 9 + 1)
  xmax = len(cavern[0])
  for delta in range(1, 5):
    for y in range(ymax):
      cavern.append([])
      for x in range(xmax):
        cavern[-1].append((cavern[y][x] + delta - 1) % 9 + 1)

def heuristic(x, y, destionation):
  return abs(destionation[0] - x) + abs(destionation[1] - y)

def updateBoundary(position, visited, cavern, destination, boundary, prevDistance):
  xmax = len(cavern[0])
  ymax = len(cavern)
  for x_ in (position[0] - 1, position[0] + 1):
    y_ = position[1]
    if 0 <= x_ < xmax:
      if (x_, y_) not in visited:
        distance = prevDistance + cavern[y_][x_]
        insort(boundary, (heuristic(x_, y_, destination) + distance, distance, (x_, y_)))
  for y_ in (position[1] - 1, position[1] + 1):
    x_ = position[0]
    if 0 <= y_ < ymax:
      if (x_, y_) not in visited:
        distance = prevDistance + cavern[y_][x_]
        insort(boundary, (heuristic(x_, y_, destination) + distance, distance, (x_, y_)))

def navigateCavern(origin, destination, cavern):
  visited = {origin}
  boundary = deque()
  updateBoundary(origin, visited, cavern, destination, boundary, 0)
  while True:
    position = boundary.popleft()
    if position[2] == destination:
      return position[1]
    distance = position[1]
    position = position[2]
    if position in visited:
      continue
    visited.add(position)
    updateBoundary(position, visited, cavern, destination, boundary, distance)

def firstStar(input):
  origin = (0, 0)
  destination = (len(input[0]) - 1, len(input) - 1)
  return navigateCavern(origin, destination, input)

def secondStar(input):
  expandCavern(input)
  origin = (0, 0)
  destination = (len(input[0]) - 1, len(input) - 1)
  return navigateCavern(origin, destination, input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 652

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2938
