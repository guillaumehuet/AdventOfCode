def readInput(file):
  return [wirePath.split(',') for wirePath in open(file).read().splitlines()]

def calculateCrossings(input):
  wirePaths = []
  for wire in input:
    position = [0, 0]
    wirePath = set()
    for instruction in wire:
      dir = instruction[0]
      length = int(instruction[1:])
      if dir == 'U':
        for _ in range(length):
          position[0] -= 1
          wirePath.add(tuple(position))
      elif dir == 'D':
        for _ in range(length):
          position[0] += 1
          wirePath.add(tuple(position))
      elif dir == 'L':
        for _ in range(length):
          position[1] -= 1
          wirePath.add(tuple(position))
      elif dir == 'R':
        for _ in range(length):
          position[1] += 1
          wirePath.add(tuple(position))
    wirePaths.append(wirePath)
  return wirePaths[0].intersection(wirePaths[1])

def firstStar(input):
  return min(abs(c[0]) + abs(c[1]) for c in calculateCrossings(input))

def secondStar(input):
  crossings = calculateCrossings(input)
  allCrossTimes = []
  for wire in input:
    position = [0, 0]
    time = 0
    crossTimes = dict()
    for instruction in wire:
      dir = instruction[0]
      length = int(instruction[1:])
      if dir == 'U':
        for _ in range(length):
          time += 1
          position[0] -= 1
          if tuple(position) in crossings and tuple(position) not in crossTimes:
            crossTimes[tuple(position)] = time
      elif dir == 'D':
        for _ in range(length):
          time += 1
          position[0] += 1
          if tuple(position) in crossings and tuple(position) not in crossTimes:
            crossTimes[tuple(position)] = time
      elif dir == 'L':
        for _ in range(length):
          time += 1
          position[1] -= 1
          if tuple(position) in crossings and tuple(position) not in crossTimes:
            crossTimes[tuple(position)] = time
      elif dir == 'R':
        for _ in range(length):
          time += 1
          position[1] += 1
          if tuple(position) in crossings and tuple(position) not in crossTimes:
            crossTimes[tuple(position)] = time
    allCrossTimes.append(crossTimes)
  return min(allCrossTimes[0][key] + allCrossTimes[1][key] for key in allCrossTimes[0])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 227

print("The second star is : {}".format(secondStar(input)))
# The second star is : 20286
