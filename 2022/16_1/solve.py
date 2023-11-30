from pathlib import Path
from bisect import insort

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
  return result

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

def firstStar(input):
  result = 0
  paths, targets = inputToPathsTargets(input)
  totalTime = 30
  pressure = 0
  time = 0
  valve = 'AA'
  openValves = frozenset()
  valveOrder = tuple()
  boundary = []
  for nextValve in paths[valve]:
    nextTime = nextValve[1] + 1 + time
    insort(boundary, (pressure + targets[nextValve[0]]*(totalTime - nextTime), nextTime, nextValve[0], openValves | {nextValve[0]}, valveOrder + ((nextValve[0], nextTime), )))
  while boundary:
    pressure, time, valve, openValves, valveOrder = boundary.pop()
    if len(openValves) == len(targets) or time > 30:
      result = max(result, pressure)
      continue
    for nextValve in paths[valve]:
      if nextValve[0] not in openValves:
        nextTime = nextValve[1] + 1 + time
        newPressure = max(pressure, pressure + targets[nextValve[0]]*(totalTime - nextTime))
        insort(boundary, (newPressure, nextTime, nextValve[0], openValves | {nextValve[0]}, valveOrder + ((nextValve[0], nextTime), )))
  return result

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2077

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
