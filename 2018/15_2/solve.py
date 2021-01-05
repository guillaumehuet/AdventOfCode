from copy import deepcopy

def readInput(file):
  terrain = []
  monsters = dict()
  y = 0
  for line in open(file).read().splitlines():
    x = 0
    terrain.append([])
    for c in line:
      if c in 'GE':
        terrain[-1].append(True)
        monsters[(y, x)] = [c, 200]
      else:
        if c == '.':
          terrain[-1].append(True)
        else:
          terrain[-1].append(False)
      x += 1
    y += 1
  terrain = tuple(tuple(line) for line in terrain)
  return terrain, monsters

def printTerrainWithMonsters(terrain, monsters):
  for y in range(len(terrain)):
    for x in range(len(terrain[0])):
      if (y, x) in monsters:
        print(monsters[(y, x)][0], end = '')
      else:
        if terrain[y][x]:
          print('.', end = '')
        else:
          print('#', end = '')
    print('   ', end = '')
    first = True
    for (y_, x_) in sorted(monsters):
      if y_ == y:
        if first:
          first = False
        else:
          print(', ', end = '')
        print(monsters[(y_, x_)][0] + '(' + str(monsters[(y_, x_)][1]) + ')', end = '')
    print()
  print()

def around(pos):
  y = pos[0]
  x = pos[1]
  return ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x))

def boundary(origin, monsters, terrain, visited):
  result = set()
  for pos in around(origin):
    if terrain[pos[0]][pos[1]] and pos not in monsters and pos not in visited:
      result.add(pos)
  return result

def findDestination(origin, destinations, monsters, terrain):
  visited = set()
  position = origin
  visited.add(position)
  distance = 0
  nextBoundary = boundary(position, monsters, terrain, visited)
  result = []
  stopLoop = False
  while nextBoundary and not stopLoop:
    distance += 1
    currBoundary = nextBoundary
    nextBoundary = set()
    for position in currBoundary:
      if position in destinations:
        stopLoop = True
        result.append(position)
      nextBoundary |= boundary(position, monsters, terrain, visited)
    visited |= currBoundary
  return min(result, default=False)

def backtrack(origin, destination, monsters, terrain):
  if destination in around(origin):
    return destination
  visited = set()
  position = destination
  visited.add(position)
  distance = 0
  nextBoundary = boundary(position, monsters, terrain, visited)
  result = []
  stopLoop = False
  while nextBoundary and not stopLoop:
    distance += 1
    currBoundary = nextBoundary
    nextBoundary = set()
    for position in currBoundary:
      if position in around(origin):
        stopLoop = True
        result.append(position)
      nextBoundary |= boundary(position, monsters, terrain, visited)
    visited |= currBoundary
  return min(result)

def fight(monsterCoord, monsters, elfDamage = 3):
  monsterType = monsters[monsterCoord][0]
  targets = []
  for pos in around(monsterCoord):
    if pos in monsters:
      if monsters[pos][0] != monsterType:
        targets.append(pos)
  minHP = min(monsters[t][1] for t in targets)
  targets = (t for t in targets if monsters[t][1] == minHP)
  target = min(targets)
  if monsterType == 'G':
    monsters[target][1] -= 3
  else:
    monsters[target][1] -= elfDamage
  if monsters[target][1] <= 0:
    del monsters[target]

def turn(monsterCoord, monsters, terrain, elfDamage = 3):
  if monsterCoord not in monsters:
    return False
  monster = monsters[monsterCoord]
  targets = []
  enemies = {k:v for k, v in monsters.items() if v[0] != monster[0]}
  if len(enemies) == 0:
    return True
  for e in enemies:
    for y, x in around(e):
      if terrain[y][x]:
        targets.append((y, x))
  if monsterCoord in targets:
    fight(monsterCoord, monsters, elfDamage)
    return False
  destination = findDestination(monsterCoord, targets, monsters, terrain)
  if not destination:
    return False
  moveTo = backtrack(monsterCoord, destination, monsters, terrain)
  monsters[moveTo] = monster
  del monsters[monsterCoord]
  if moveTo in targets:
    fight(moveTo, monsters, elfDamage)
    return False

def totalHP(monsters):
  return sum(monsters[m][1] for m in monsters)

def firstStar(input):
  terrain = input[0]
  monsters = deepcopy(input[1])
  round = 0
  while True:
    for m in sorted(monsters):
      if turn(m, monsters, terrain):
        return totalHP(monsters)*round
    round += 1

def secondStar(input):
  terrain = input[0]
  elfDamage = 3
  while True:
    elfDamage += 1
    monsters = deepcopy(input[1])
    nElfs = len([m for m in monsters if monsters[m][0] == 'E'])
    loop = True
    round = 0
    while loop:
      for m in sorted(monsters):
        if turn(m, monsters, terrain, elfDamage):
          if nElfs == len([m for m in monsters if monsters[m][0] == 'E']):
            return totalHP(monsters)*round
          loop = False
      round += 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 214731

print("The second star is : {}".format(secondStar(input)))
# The second star is : 53222
