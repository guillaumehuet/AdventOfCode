from pathlib import Path

def readInput(file):
  firstLine = True
  image = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if firstLine:
      algorithm = tuple(True if c == '#' else False for c in line)
      firstLine = False
    elif line != '':
      image.append(tuple(True if c == '#' else False for c in line))
  return algorithm, tuple(image)

def prettyPrint(image):
  for line in image:
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

def neighboor(image, x0, y0, xmax, ymax, offGridState = False):
  result = 0
  for y in (y0 - 1, y0, y0 + 1):
    for x in (x0 - 1, x0, x0 + 1):
      if y < 0 or y >= ymax or x < 0 or x >= xmax:
        result *= 2
        result += offGridState
      else:
        result *= 2
        result += image[y][x]
  return result

def step(image, algorithm, offGridState = False):
  newImage = []
  xmax = len(image[0])
  ymax = len(image)
  for y in range(-1, xmax + 1):
    newImage.append([])
    for x in range(-1, ymax + 1):
      newImage[-1].append(algorithm[neighboor(image, x, y, xmax, ymax, offGridState)])
  if offGridState:
    offGridState = algorithm[511]
  else:
    offGridState = algorithm[0]
  return newImage, offGridState

def countPixels(image):
  result = 0
  for line in image:
    for pix in line:
      if pix:
        result += 1
  return result

def firstStar(input):
  algorithm, image = input
  offGridState = False
  for _ in range(2):
    image, offGridState = step(image, algorithm, offGridState)
  return countPixels(image)

def secondStar(input):
  algorithm, image = input
  offGridState = False
  for _ in range(50):
    image, offGridState = step(image, algorithm, offGridState)
  return countPixels(image)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 5432

print("The second star is : {}".format(secondStar(input)))
# The second star is : 16016
