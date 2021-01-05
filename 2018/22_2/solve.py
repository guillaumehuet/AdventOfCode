import heapq

def readInput(file):
  values = tuple(l.split(':')[1][1:] for l in open(file).read().splitlines())
  depth = int(values[0])
  target = tuple(int(i) for i in values[1].split(','))
  return depth, target

def printCave(cave, target):
  sprites = ('.', '=', '|')
  for y in range(len(cave)):
    line = ""
    for x in range(len(cave[y])):
      if (x, y) == (0, 0):
        line += 'M'
      elif (x, y) == target:
        line += 'T'
      else:
        line += sprites[cave[y][x]]
    print(line)

def riskLevel(cave):
  return sum(sum(l) for l in cave)

def defineCave(depth, target, upTo = None):
  upTo = upTo or target
  caveErosionLevel = []
  cave = []
  for y in range(upTo[1] + 1):
    caveErosionLevel.append([])
    cave.append([])
    for x in range(upTo[0] + 1):
      if (x, y) == target:
        geoIndex = 0
      elif y == 0:
        geoIndex = x*16807
      elif x == 0:
        geoIndex = y*48271
      else:
        geoIndex = caveErosionLevel[y - 1][x] * caveErosionLevel[y][x - 1]
      erosionLevel = (geoIndex + depth) % 20183
      caveErosionLevel[y].append(erosionLevel)
      cave[y].append(erosionLevel % 3)
  return cave

def around(pos, cave, distance, visited, target):
  delta = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0))
  tools = (0, 1, 2)
  result = []
  for j in range(len(delta)):
    new = []
    for i in range(len(pos)):
      new.append(pos[i] + delta[j][i])
    new = tuple(new)
    if min(new) >= 0 and new not in visited:
      if cave[new[1]][new[0]] != pos[2]:
        new = (distance + 1 + manhattanDistance(target, new), distance + 1) + new
        result.append(new)
  for j in range(len(tools)):
    if tools[j] != pos[2] and tools[j] != cave[pos[1]][pos[0]]:
      new = []
      new = list(pos)
      new[2] = tools[j]
      new = tuple(new)
      if new not in visited:
        new = (distance + 7 + manhattanDistance(target, new), distance + 7) + new
        result.append(new)
  return tuple(result)

def manhattanDistance(aPos, bPos):
  return sum(abs(aPos[i] - bPos[i]) for i in range(2)) + 7*(aPos[2] != bPos[2])

def navigateCave(depth, target):
  # Gear defined based on the region type its not allowed:
  # 0 = rocky  <=> 0 = neither
  # 1 = wet    <=> 1 = torch
  # 2 = narrow <=> 2 = climbing gear

  # If you get list index out of range error on cave, increase added coordinates
  addedCoords = 150

  visited = set()
  upTo = (target[0] + addedCoords, target[1] + addedCoords)
  cave = defineCave(depth, target, upTo)
  target += (1,)
  origin = (0, 0, 1)
  queue = [(manhattanDistance(target, origin), 0) + origin]
  while queue:
    nextItem = heapq.heappop(queue)
    distance = nextItem[1]
    position = nextItem[2:]
    if position in visited:
      continue
    if position == target:
      return distance
    visited.add(position)
    for neighbor in around(position, cave, distance, visited, target):
      heapq.heappush(queue, neighbor)
  return "Error"

def firstStar(input):
  depth, target = input
  cave = defineCave(depth, target)
  return riskLevel(cave)

def secondStar(input):
  depth, target = input
  return navigateCave(depth, target)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 8735

print("The second star is : {}".format(secondStar(input)))
# The second star is : 984
