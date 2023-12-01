from pathlib import Path
from collections import defaultdict
from bisect import insort

def readInput(file):
  distances = defaultdict(dict)
  places = set()
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    line = line.split()
    origin = line[0]
    destination = line[2]
    distance = int(line[4])
    distances[origin][destination] = distance
    distances[destination][origin] = distance
    places.add(origin)
    places.add(destination)
  return places, distances

def routes(places, distances):
  boundary = []
  minResult = None
  maxResult = None
  for place in places:
    insort(boundary, (0, place, frozenset((place,))))
  while boundary:
    currDistance, currPlace, visitedPlaces = boundary.pop()
    if len(visitedPlaces) == len(places):
      if not minResult or currDistance < minResult:
        minResult = currDistance
        continue
      if not maxResult or currDistance > maxResult:
        maxResult = currDistance
        continue
    for neighboor, distance in distances[currPlace].items():
      if neighboor not in visitedPlaces:
        insort(boundary, (currDistance + distance, neighboor, visitedPlaces | frozenset((neighboor,))))
  return minResult, maxResult

def firstStar(input):
  places, distances = input
  return routes(places, distances)[0]

def secondStar(input):
  places, distances = input
  return routes(places, distances)[1]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 207

print("The second star is : {}".format(secondStar(input)))
# The second star is : 804
