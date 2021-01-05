def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  size = 1000
  fabric = [[0 for _ in range(size)] for _ in range(size)]
  for claim in input:
    applyClaim(claim, fabric)
  return countOverlaps(fabric)

def applyClaim(claim, fabric):
  topLeft, size = claim.split('@')[1].split(':')
  left, top = topLeft.split(',')
  width, heigth = size.split('x')
  left = int(left)
  top = int(top)
  width = int(width)
  heigth = int(heigth)
  for x in range(left, left + width):
    for y in range(top, top + heigth):
      fabric[x][y] += 1

def countOverlaps(fabric):
  result = 0
  for row in fabric:
    for square in row:
      if square > 1:
        result += 1
  return result

def secondStar(input):
  size = 1000
  fabric = [[0 for _ in range(size)] for _ in range(size)]
  for claim in input:
    applyClaim(claim, fabric)
  for claim in input:
    if checkClaim(claim, fabric):
      return int(claim.split('@')[0][1:])

def checkClaim(claim, fabric):
  topLeft, size = claim.split('@')[1].split(':')
  left, top = topLeft.split(',')
  width, heigth = size.split('x')
  left = int(left)
  top = int(top)
  width = int(width)
  heigth = int(heigth)
  for x in range(left, left + width):
    for y in range(top, top + heigth):
      if fabric[x][y] > 1:
        return False
  return True

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 120419

print("The second star is : {}".format(secondStar(input)))
# The second star is : 445
