import z3

def readInput(file):
  nanobots = []
  for line in open(file).read().splitlines():
    pos, r = line.split('>')
    pos = tuple(int(c) for c in pos[5:].split(','))
    r = int(r[4:])
    nanobots.append((pos, r))
  return tuple(nanobots)

def findLargest(nanobots):
  largest = nanobots[0]
  for n in nanobots:
    if n[1] > largest[1]:
      largest = n
  return largest

def manhattanDistance(n1, n2):
  return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1]) + abs(n1[2] - n2[2])

def numInRange(center, nanobots):
  result = 0
  r = center[1]
  for n in nanobots:
    if manhattanDistance(center[0], n[0]) <= r:
      result += 1
  return result

def z3Abs(x):
  return z3.If(x >= 0, x, -x)

def z3Solve(nanobots):
  nNanobots = len(nanobots)
  x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')
  inRanges = [z3.Int('inRange' + str(i)) for i in range(nNanobots)]
  nInRange = z3.Int('nInRange')
  optimizer = z3.Optimize()
  for i in range(nNanobots):
    (_x, _y, _z), _range = nanobots[i]
    optimizer.add(inRanges[i] == z3.If(z3Abs(x - _x) + z3Abs(y - _y) + z3Abs(z - _z) <= _range, 1, 0))
  optimizer.add(nInRange == sum(inRanges))
  distanceOrigin = z3.Int('distanceOrigin')
  optimizer.add(distanceOrigin == z3Abs(x) + z3Abs(y) + z3Abs(z))
  optimizer.maximize(nInRange)
  result = optimizer.minimize(distanceOrigin)
  optimizer.check()
  return optimizer.lower(result)

def firstStar(input):
  center = findLargest(input)
  return numInRange(center, input)

def secondStar(input):
  return z3Solve(input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 613

print("The second star is : {}".format(secondStar(input)))
# The second star is : 101599540
