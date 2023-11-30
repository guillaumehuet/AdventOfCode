from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    state, coords = line.split(' ')
    coords = coords.split(',')
    coords = tuple(tuple(int(n) for n in c.split('=')[1].split('..')) for c in coords)
    state = True if state == 'on' else False
    result.append((state, coords))
  return tuple(result)

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

def intersect(cube1, cube2):
  for coord in range(3):
    if cube1[coord][1] < cube2[coord][0] or cube2[coord][1] < cube1[coord][0]:
      return False
  return True

def slice(cube, tool):
  slices = {cube}
  for coord in range(3):
    newSlices = set()
    removedSlices = set()
    for side in range(2):
      newSlices = set()
      removedSlices = set()
      for slice in slices:
        if slice[coord][0] <= tool[coord][side] <= slice[coord][1]:
          removedSlices.add(slice)
          newSlice = [list(slice), list(slice)]
          cutPlane = tool[coord][side] + side
          newSlice[0][coord] = (slice[coord][0], cutPlane-1)
          newSlice[1][coord] = (cutPlane, slice[coord][1])
          newSlices.add(tuple(newSlice[0]))
          newSlices.add(tuple(newSlice[1]))
      slices -= removedSlices
      slices |= newSlices
  for slice in slices:
    if intersect(slice, tool):
      slices.remove(slice)
      return slices

def sumRegions(onRegions):
  result = 0
  for region in onRegions:
    volume = 1
    for coord in region:
      volume *= coord[1] - coord[0] + 1
    result += volume
  return result

def firstStar(input):
  grid = dict()
  for rebootStep in input:
    step(grid, rebootStep)
  return cubesOn(grid)

def secondStar(input):
  onRegions = set()
  for rebootStep in input:
    currCube = rebootStep[1]
    affectedCubes = set()
    slicedCubes = set()
    for otherCube in onRegions:
      if intersect(otherCube, currCube):
        affectedCubes.add(otherCube)
        slicedCubes |= slice(otherCube, currCube)
    onRegions -= affectedCubes
    onRegions |= slicedCubes
    if rebootStep[0]:
      onRegions.add(currCube)
  return sumRegions(onRegions)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 596989

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1160011199157381
