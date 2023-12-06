from pathlib import Path

def readInput(file):
  result = []
  lines = Path(__file__).with_name(file).open('r').read().splitlines()
  times = [int(n) for n in lines[0].split(':')[1].split()]
  distances = [int(n) for n in lines[1].split(':')[1].split()]
  for i in range(len(times)):
    result.append((times[i], distances[i]))
  return tuple(result)

def mergeInput(input):
  time = ""
  distance = ""
  for race in input:
    time += str(race[0])
    distance += str(race[1])
  return int(time), int(distance)

def possibleDistances(time):
  result = []
  for speed in range(time + 1):
    result.append(speed *(time - speed))
  return result

def countWaysToBeat(time, target):
  result = 0
  for speed in range(time + 1):
    distance = speed *(time - speed)
    if distance > target:
      result += 1
  return result

def firstStar(input):
  result = 1
  for race in input:
    result *= countWaysToBeat(race[0], race[1])
  return result

def secondStar(input):
  race = mergeInput(input)
  return countWaysToBeat(race[0], race[1])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 219849

print("The second star is : {}".format(secondStar(input)))
# The second star is : 29432455
