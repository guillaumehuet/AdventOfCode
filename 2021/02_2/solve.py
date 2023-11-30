from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  forward = 0
  down = 0
  for line in input:
    direction, value = line.split()
    value = int(value)
    if direction == 'forward':
      forward += value
    elif direction == 'down':
      down += value
    elif direction == 'up':
      down -= value
  return forward*down


def secondStar(input):
  forward = 0
  down = 0
  aim = 0
  for line in input:
    direction, value = line.split()
    value = int(value)
    if direction == 'forward':
      forward += value
      down += aim*value
    elif direction == 'down':
      aim += value
    elif direction == 'up':
      aim -= value
  return forward*down

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1480518

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1282809906
