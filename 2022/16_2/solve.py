from pathlib import Path
from bisect import insort

def inputToPathsTargets(input):
  targets = dict()
  targets['AA'] = 0
  for valve in input:
    if input[valve][0] > 0:
      targets[valve] = input[valve][0]
  paths = dict()
  for source in targets:
    for dest in targets:
      if source == dest or dest == 'AA':
        continue
      visited = {source}
      boundary = [(1, valve) for valve in input[source][1]]
      while boundary:
        curr = boundary.pop(0)
        if curr[1] == dest:
          if source in paths:
            paths[source].append((dest, curr[0]))
          else:
            paths[source] = [(dest, curr[0])]
          break
        if curr[1] in visited:
          continue
        visited.add(curr[0])
        boundary += [(curr[0] + 1, valve) for valve in input[curr[1]][1]]
    paths[source] = tuple(paths[source])
  del targets['AA']
  return paths, targets

def readInput(file):
  result = dict()
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    line = line.split()
    valve = line[1]
    flowRate = line[4]
    flowRate = int(flowRate.split('=')[1][:-1])
    tunnels = line[9:]
    tunnels = tuple(tunnel.removesuffix(',') for tunnel in tunnels)
    result[valve] = (flowRate, tunnels)
  return inputToPathsTargets(result)

def maxPressure(paths, targets, totalTime, openValves = frozenset(), elephant = False):
  result = 0
  resultValves = frozenset()
  remainingValves = len(targets)
  if elephant:
    myBest, myValves = maxPressure(paths, targets, totalTime)
    elephantMin = maxPressure(paths, targets, totalTime, myValves)[0]
    result = myBest + elephantMin
  boundary = [(0, 0, 'AA', openValves)]
  while boundary:
    pressure, time, valve, openValves = boundary.pop()
    for nextValve in paths[valve]:
      if elephant and pressure > elephantMin:
        elephantPressure, elephantOpenValves = maxPressure(paths, targets, totalTime, openValves)
        totalPressure = pressure + elephantPressure
        totalOpenValves = openValves | elephantOpenValves
        if totalPressure > result:
          result = totalPressure
          resultValves = totalOpenValves
      if nextValve[0] not in openValves:
        newTime = nextValve[1] + 1 + time
        if newTime > totalTime:
          if pressure > result:
            result = pressure
            resultValves = openValves
          continue
        newPressure = pressure + targets[nextValve[0]]*(totalTime - newTime)
        newOpenValves = openValves | {nextValve[0]}
        if len(newOpenValves) >= remainingValves:
          if newPressure > result:
            result = newPressure
            resultValves = newOpenValves
          continue
        insort(boundary, (newPressure, newTime, nextValve[0], newOpenValves))
  return result, resultValves

def firstStar(input):
  paths, targets = input
  return maxPressure(paths, targets, 30)[0]

def secondStar(input):
  paths, targets = input
  return maxPressure(paths, targets, 26, elephant=True)[0]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2077

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2741
