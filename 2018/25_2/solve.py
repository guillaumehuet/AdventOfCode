from pathlib import Path

def readInput(file):
  return tuple(tuple(int(coord) for coord in line.split(',')) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def distance(aPoint, bPoint):
  return sum(abs(aPoint[i] - bPoint[i]) for i in range(len(aPoint)))

def getConstellations(points):
  result = []
  for i in range(len(points)):
    currConstellation = {i}
    for j in range(i + 1, len(points)):
      if distance(points[i], points[j]) <= 3:
        currConstellation.add(j)
    nearbyConstellations = []
    for k in range(len(result)):
      for c in currConstellation:
        if c in result[k] and k not in nearbyConstellations:
          nearbyConstellations.append(k)
    nearbyConstellations.sort()
    nNearbyConstellations = len(nearbyConstellations)
    if nNearbyConstellations == 0:
      result.append(set())
      result[-1] = currConstellation
    elif nNearbyConstellations == 1:
      result[nearbyConstellations[0]] |= currConstellation
    else:
      for offset, k in enumerate(nearbyConstellations):
        currConstellation |= result[k - offset]
        del result[k - offset]
      result.append(set())
      result[-1] = currConstellation
  return result

def firstStar(input):
  return len(getConstellations(input))

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 388
