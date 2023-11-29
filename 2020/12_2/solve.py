from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

directions = ['E', 'S', 'W', 'N']
unitVectors = {'E':(1, 0), 'S':(0, -1), 'W':(-1, 0), 'N':(0, 1)}
turnRight = [[0, 1], [-1, 0]]

def move(instruction, position, direction):
  action = instruction[0]
  value = int(instruction[1:])
  if action in 'RL':
    value //= 90
    if action == 'R':
      direction += value
    else:
      direction -= value
    direction %= 4
  else:
    if action in 'ESWN':
      unitVector = unitVectors[action]
    else:
      unitVector = unitVectors[directions[direction]]
    position = (unitVector[0]*value + position[0], unitVector[1]*value + position[1])
  return position, direction

def moveWithWaypoint(instruction, position, waypoint):
  action = instruction[0]
  value = int(instruction[1:])
  if action in 'ESWN':
    unitVector = unitVectors[action]
    waypoint = (unitVector[0]*value + waypoint[0], unitVector[1]*value + waypoint[1])
  elif action in 'RL':
    value //= 90
    if action == 'L':
      value = 4 - value
    for _ in range(value):
      waypoint = (turnRight[0][0]*waypoint[0] + turnRight[0][1]*waypoint[1], turnRight[1][0]*waypoint[0] + turnRight[1][1]*waypoint[1])
  else:
    position = (waypoint[0]*value + position[0], waypoint[1]*value + position[1])
  return position, waypoint

def firstStar(input):
  position = (0, 0)
  direction = 0
  for line in input:
    position, direction = move(line, position, direction)
  return abs(position[0]) + abs(position[1])

def secondStar(input):
  position = (0, 0)
  waypoint = (10, 1)
  for line in input:
    position, waypoint = moveWithWaypoint(line, position, waypoint)
  return abs(position[0]) + abs(position[1])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 796

print("The second star is : {}".format(secondStar(input)))
# The second star is : 39446
