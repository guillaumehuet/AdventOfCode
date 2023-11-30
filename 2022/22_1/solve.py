from pathlib import Path

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def readInput(file):
  path = False
  result = dict()
  result['map'] = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      path = True
    if path:
      result['path'] = []
      isNumber = False
      currSymbol = 0
      for c in line:
        if c.isdigit():
          if isNumber:
            currSymbol *= 10
            currSymbol += int(c)
          else:
            result['path'].append(currSymbol)
            currSymbol = int(c)
          isNumber = True
        else:
          result['path'].append(currSymbol)
          currSymbol = c
          isNumber = False
      result['path'].append(currSymbol)
      del result['path'][0]
    else:
      result['map'].append([])
      # 0 = open tile, 1 = solid wall, 2 = wrapparound
      for c in line:
        if c == '.':
          result['map'][-1].append(0)
        elif c == '#':
          result['map'][-1].append(1)
        else:
          result['map'][-1].append(2)
  return result

def borderMap(map):
  width = max(len(line) for line in map) + 2
  map.insert(0, [2 for _ in range(width)])
  for line in map[1:]:
    line.insert(0, 2)
    for i in range(len(line), width):
      line.append(2)
  map.append([2 for _ in range(width)])

def nextTile(map, currTile, direction):
  nextTile = (currTile[0] + direction[0], currTile[1] + direction[1])
  nextValue = map[nextTile[1]][nextTile[0]]
  if nextValue == 0:
    return nextTile, True
  elif nextValue == 1:
    return currTile, False
  elif nextValue == 2:
    if direction[0] == 1:
      nextTile = (0, nextTile[1])
    elif direction[0] == -1:
      nextTile = (len(map[0]) - 1, nextTile[1])
    elif direction[1] == 1:
      nextTile = (nextTile[0], 0)
    else:
      nextTile = (nextTile[0], len(map) - 1)
    while map[nextTile[1]][nextTile[0]] == 2:
      nextTile = (nextTile[0] + direction[0], nextTile[1] + direction[1])
    nextValue = map[nextTile[1]][nextTile[0]]
    if nextValue == 0:
      return nextTile, True
    else:
      return currTile, False

def firstStar(input):
  map = input['map'].copy()
  path = input['path']
  borderMap(map)
  dirIndex = 0
  for col, value in enumerate(map[1]):
    if value != 2:
      currX = col
      break
  currTile = (currX, 1)
  for instruction in path:
    if isinstance(instruction, int):
      for _ in range(instruction):
        currTile, canMove = nextTile(map, currTile, directions[dirIndex%4])
        if not canMove:
          break
    else:
      if instruction == 'R':
        dirIndex += 1
      else:
        dirIndex -= 1
  return 1000*currTile[1]+4*currTile[0]+(dirIndex%4)

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 103224

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
