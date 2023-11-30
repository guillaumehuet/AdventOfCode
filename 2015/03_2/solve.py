def readInput(file):
  return open(file).read().splitlines()[0]

def firstStar(input):
  coord = [0, 0]
  visited = {tuple(coord)}
  for c in input:
    if c == '<':
      coord[0] -= 1
    elif c == '>':
      coord[0] += 1
    elif c == '^':
      coord[1] += 1
    elif c == 'v':
      coord[1] -= 1
    visited.add(tuple(coord))
  return len(visited)

def secondStar(input):
  santa = [0, 0]
  robot = [0, 0]
  visited = {tuple(santa)}
  robotTurn = False
  for c in input:
    if robotTurn:
      coord = robot
    else:
      coord = santa
    robotTurn = not robotTurn
    if c == '<':
      coord[0] -= 1
    elif c == '>':
      coord[0] += 1
    elif c == '^':
      coord[1] += 1
    elif c == 'v':
      coord[1] -= 1
    visited.add(tuple(coord))
  return len(visited)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2565

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2639
