from pathlib import Path

def readInput(file):
  return tuple(tuple(int(coord) for coord in line.split(',')) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def countFaces(input):
  nElements = len(input)
  xSort = list(input)
  ySort = list(input)
  zSort = list(input)
  xSort.sort(key=lambda x : (x[1], x[2], x[0]))
  ySort.sort(key=lambda x : (x[0], x[2], x[1]))
  zSort.sort()
  result = 0
  for i, cube in enumerate(xSort):
    if i <= 0:
      result += 1
    else:
      previous = xSort[i - 1]
      if not (previous[1:] == cube[1:] and previous[0] + 1 == cube[0]):
        result += 1
    if i + 1 >= nElements:
      result += 1
    else:
      following = xSort[i + 1]
      if not (following[1:] == cube[1:] and following[0] == cube[0] + 1):
        result += 1
  for i, cube in enumerate(ySort):
    if i <= 0:
      result += 1
    else:
      previous = ySort[i - 1]
      if not (previous[::2] == cube[::2] and previous[1] + 1 == cube[1]):
        result += 1
    if i + 1 >= nElements:
      result += 1
    else:
      following = ySort[i + 1]
      if not (following[::2] == cube[::2] and following[1] == cube[1] + 1):
        result += 1
  for i, cube in enumerate(zSort):
    if i <= 0:
      result += 1
    else:
      previous = zSort[i - 1]
      if not (previous[:2] == cube[:2] and previous[2] + 1 == cube[2]):
        result += 1
    if i + 1 >= nElements:
      result += 1
    else:
      following = zSort[i + 1]
      if not (following[:2] == cube[:2] and following[2] == cube[2] + 1):
        result += 1
  return result

def firstStar(input):
  return countFaces(input)
  
def negative(input):
  minX = input[0][0]
  maxX = input[0][0]
  minY = input[0][1]
  maxY = input[0][1]
  minZ = input[0][2]
  maxZ = input[0][2]
  positive = set(input)
  for (x, y, z) in positive:
    minX = min(minX, x)
    maxX = max(maxX, x)
    minY = min(minY, y)
    maxY = max(maxY, y)
    minZ = min(minZ, z)
    maxZ = max(maxZ, z)
  result = []
  for x in range(minX, maxX + 1):
    for y in range(minY, maxY + 1):
      for z in range(minZ, maxZ + 1):
        if (x, y, z) not in positive:
          result.append((x, y, z))
  return result

def neighboors(position):
  result = []
  for delta in [-1, 1]:
    result.append((position[0] + delta, position[1], position[2]))
    result.append((position[0], position[1] + delta, position[2]))
    result.append((position[0], position[1], position[2] + delta))
  return result

def inside(negative):
  current = negative[0]
  negativeSet = set(negative)
  boundary = neighboors(current)
  while boundary:
    current = boundary.pop()
    if current not in negativeSet:
      continue
    negativeSet.remove(current)
    boundary += neighboors(current)
  return negativeSet

def secondStar(input):
  negativeCube = negative(input)
  insideCube = inside(negativeCube)
  outsideCube = list(set(negativeCube) - insideCube)
  globalCube = negative(outsideCube)
  return firstStar(globalCube)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4512

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2554
