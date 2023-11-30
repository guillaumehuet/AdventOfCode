from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    state, coords = line.split(' ')
    coords = coords.split(',')
    coords = [[int(n) for n in c.split('=')[1].split('..')] for c in coords]
    state = True if state == 'on' else False
    result.append([state, coords])
  return result

def step(grid, rebootStep):
  xMin = max(-50, rebootStep[1][0][0])
  xMax = min(50, rebootStep[1][0][1])
  yMin = max(-50, rebootStep[1][1][0])
  yMax = min(50, rebootStep[1][1][1])
  zMin = max(-50, rebootStep[1][2][0])
  zMax = min(50, rebootStep[1][2][1])
  for x in range(xMin, xMax + 1):
    for y in range(yMin, yMax + 1):
      for z in range(zMin, zMax + 1):
        grid[(x, y, z)] = rebootStep[0]

def cubesOn(grid):
  result = 0
  for k in grid:
    result += grid[k]
  return result

def firstStar(input):
  grid = dict()
  for rebootStep in input:
    step(grid, rebootStep)
  return cubesOn(grid)

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 596989

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
