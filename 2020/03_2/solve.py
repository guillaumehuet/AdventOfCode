from pathlib import Path

def readInput(file):
  return [[True if c == '#' else False for c in line] for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def numTreesOnSlope(x_step, y_step, input):
  result = 0
  height = len(input)
  width = len(input[0])
  x = 0
  y = 0
  while y < height:
    if input[y][x]:
      result += 1
    x += x_step
    y += y_step
    if x >= width:
      x -= width
  return result

def firstStar(input):
  return numTreesOnSlope(3, 1, input)

def secondStar(input):
  return numTreesOnSlope(1, 1, input)*numTreesOnSlope(3, 1, input)*numTreesOnSlope(5, 1, input)*numTreesOnSlope(7, 1, input)*numTreesOnSlope(1, 2, input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 247

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2983070376
