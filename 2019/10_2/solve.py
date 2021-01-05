from math import gcd, atan2

def readInput(file):
  return [[1 if c == '#' else 0 for c in line] for line in open(file).read().splitlines()]

def arrayToCoords(array):
  result = []
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j]:
        result.append((j, i))
  return result

def direction(aCoord, bCoord):
  return ((aCoord[0] - bCoord[0]), (aCoord[1] - bCoord[1]))

def reduceCoords(coord):
  fac = gcd(coord[0], coord[1])
  return (coord[0] // fac, coord[1] // fac)

def countVisible(coords):
  allResults = dict()
  for aCoord in coords:
    allResults[aCoord] = len(listAngles(aCoord, coords))
  return allResults

def listAngles(aCoord, coords):
  results = set()
  for bCoord in coords:
    if aCoord != bCoord:
      results.add(reduceCoords(direction(aCoord, bCoord)))
  return results

def firstStar(input):
  return max(countVisible(arrayToCoords(input)).values())

def secondStar(input):
  coords = arrayToCoords(input)
  tableOfVisibles = countVisible(coords)
  station = max(tableOfVisibles, key=tableOfVisibles.get)
  angles = list(listAngles(station, coords))
  angles.sort(key=lambda x : atan2(x[0], -x[1]))
  if angles[-1][0] == 0:
    angles = [angles[-1]] + angles[0:-1]
  dir200 = angles[199] # Only because firstStar is over 200
  return (station[0] - dir200[0])*100 + station[1] - dir200[1] # Can be a multiple of dir, but here dir is enough

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 303

print("The second star is : {}".format(secondStar(input)))
# The second star is : 408