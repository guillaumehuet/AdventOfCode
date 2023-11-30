from pathlib import Path

def readInput(file):
  x, y = Path(__file__).with_name(file).open('r').read().splitlines()[0].split(':')[1].split(',')
  x = tuple(int(n) for n in x.split('=')[1].split('..'))
  y = tuple(int(n) for n in y.split('=')[1].split('..'))
  return x, y

def step(x, y, vx, vy):
  x += vx
  y += vy
  if vx > 0:
    vx -= 1
  elif vx < 0:
    vx += 1
  vy -= 1
  return x, y, vx, vy

def inArea(x, y, area):
  if y < min(area[1]):
    return -2
  if x > max(area[0]):
    return -1
  if min(area[0]) <= x <= max(area[0]) and min(area[1]) <= y <= max(area[1]):
    return 1
  return 0

def firstStar(input):
  missedLines = 0
  vy0 = min(input[1]) - 1
  maxvy = 0
  while True:
    if missedLines > 15:
      return (maxvy + 1)*maxvy//2
    vy0 += 1
    vx0 = -1
    found = False
    while vx0 <= max(input[0]):
      vx0 += 1
      x, y = 0, 0
      vx, vy = vx0, vy0
      while inArea(x, y, input) == 0:
        x, y, vx, vy = step(x, y, vx, vy)
      res = inArea(x, y, input)
      if res == 1:
        maxvy = vy0
        found = True
        missedLines = 0
        break
    if not found:
      missedLines += 1

def secondStar(input):
  result = 0
  missedLines = 0
  vy0 = min(input[1]) - 1
  maxvy = 0
  while True:
    if missedLines > 15:
      return result
    vy0 += 1
    vx0 = -1
    found = False
    while vx0 <= max(input[0]):
      vx0 += 1
      x, y = 0, 0
      vx, vy = vx0, vy0
      while inArea(x, y, input) == 0:
        x, y, vx, vy = step(x, y, vx, vy)
      res = inArea(x, y, input)
      if res == 1:
        result += 1
        found = True
        missedLines = 0
    if not found:
      missedLines += 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4851

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1739
