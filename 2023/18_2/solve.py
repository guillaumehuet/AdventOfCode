from pathlib import Path

directions = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
dirCodes = ['R', 'D', 'L', 'U']

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    dir, dist, hex = line.split()
    dist = int(dist)
    hexdist = int(hex[2:-2], 16)
    hexdir = dirCodes[int(hex[-2:-1], 16)]
    result.append((dir, dist, hexdir, hexdist))
  return tuple(result)

def step(position, direction, steps=1):
  return (position[0] + steps*direction[0], position[1] + steps*direction[1])

def crossProduct(position1, position2):
  return position1[0]*position2[1] - position1[1]*position2[0]

def polygonArea(plan, hex = False):
  doubleArea = 0
  addedBorder = 1
  position = (0, 0)
  for dir, dist, dirHex, distHex in plan:
    if hex:
      dir = dirHex
      dist = distHex
    newPosition = step(position, directions[dir], dist)
    doubleArea += crossProduct(newPosition, position)
    position = newPosition
    if dir in 'DL':
      addedBorder += dist
  return int(doubleArea / 2) + addedBorder

def firstStar(input):
  return polygonArea(input)

def secondStar(input):
  return polygonArea(input, True)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 40761

print("The second star is : {}".format(secondStar(input)))
# The second star is : 106920098354636
