from pathlib import Path

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def step(position, direction):
  return ((position[0] + direction[0], position[1] + direction[1]), direction)

def mirrorPositive(direction):
  return (direction[1], direction[0])

def mirrorNegative(direction):
  return (-direction[1], -direction[0])

def energize(maze, start=((0, 0), right)):
  height = len(maze)
  width = len(maze[0])
  boundary = [start]
  visited = set()
  while boundary:
    position, direction = boundary.pop()
    if (position, direction) in visited:
      continue
    visited.add((position, direction))
    obstacle = maze[position[0]][position[1]]
    newPos = []
    if obstacle == '/':
      newPos.append(step(position, mirrorNegative(direction)))
    elif obstacle == '\\':
      newPos.append(step(position, mirrorPositive(direction)))
    elif obstacle == '-' and direction[0] != 0:
      newPos.append(step(position, left))
      newPos.append(step(position, right))
    elif obstacle == '|' and direction[1] != 0:
      newPos.append(step(position, up))
      newPos.append(step(position, down))
    else:
      newPos.append(step(position, direction))
    for pos in newPos:
      if 0 <= pos[0][0] < height and 0 <= pos[0][1] < width and pos not in visited:
        boundary.append(pos)
  return len(set(v[0] for v in visited))

def firstStar(input):
  return energize(input)

def secondStar(input):
  result = 0
  height = len(input)
  width = len(input[0])
  for i in range(height):
    result = max(result, energize(input, ((i, 0), right)))
    result = max(result, energize(input, ((i, width - 1), left)))
  for j in range(width):
    result = max(result, energize(input, ((0, j), down)))
    result = max(result, energize(input, ((height - 1, j), up)))
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 8389

print("The second star is : {}".format(secondStar(input)))
# The second star is : 8564
