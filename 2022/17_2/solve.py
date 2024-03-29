from pathlib import Path

def readInput(file):
  result = []
  for c in Path(__file__).with_name(file).open('r').read().splitlines()[0]:
    # Right push correspond to True, left to False
    result.append(c == '>')
  return tuple(result)

# The chamber is reversed top to bottom, so must the rock types
rockTypes = (
  # ####
  (
    (True, True, True, True), 
  ),
  # .#.
  # ###
  # .#.
  (
    (False, True, False),
    (True, True, True),
    (False, True, False)
  ),
  # ..#                        ###
  # ..#                        ..#
  # ###    /!\ : Reversed as : ..#
  (
    (True, True, True),
    (False, False, True),
    (False, False, True)
  ),
  # #
  # #
  # #
  # #
  (
    (True, ),
    (True, ),
    (True, ),
    (True, )
  ),
  # ##
  # ##
  (
    (True, True),
    (True, True)
  )
)

def printChamber(chamber):
  for line in reversed(chamber):
    print('|', end='')
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print('|')
  print('+', end='')
  for c in chamber[0]:
    print('-', end='')
  print('+')

def simulateChamber(input, rockNumber, findRepeat=False):
  chamber = []
  currRock = 0
  currDir = 0
  modRock = len(rockTypes)
  modDir = len(input)
  configsMods = set()
  configsHeights = dict()
  prevTotalHeight = 0
  confirmedHeight = 0
  while True:
    if findRepeat:
      if (currRock % modRock, currDir % modDir) in configsMods:
        initRock, initHeight = configsHeights[(currRock % modRock, currDir % modDir)]
        cycleLength = currRock - initRock
        cycleHeight = len(chamber) - initHeight
        repeats = int((rockNumber-initRock)/cycleLength)
        remainder = rockNumber - cycleLength*repeats
        for c in configsHeights.values():
          if c[0] == remainder:
            remainderHeight = c[1]
            break
        totalHeight = remainderHeight + cycleHeight*repeats
        if prevTotalHeight == totalHeight:
          confirmedHeight += 1
          if confirmedHeight == 100:
            return totalHeight
        else:
          prevTotalHeight = 0
          confirmedHeight = 0
        prevTotalHeight = totalHeight
      configsMods.add((currRock % modRock, currDir % modDir))
      configsHeights[(currRock % modRock, currDir % modDir)] = (currRock, len(chamber))
    else:
      if currRock >= rockNumber:
        break
    rockType = rockTypes[currRock % modRock]
    currX = 2
    currY = len(chamber) + 3
    rockHeight = len(rockType)
    rockWidth = len(rockType[0])
    for _ in range(rockHeight + 3):
      chamber.append([False for _ in range(7)])
    while True:
      # Jet pushing
      dir = input[currDir % modDir]
      currDir += 1
      collision = False
      if dir:
        if currX + rockWidth < 7:
          tentativeX = currX + 1
        else:
          collision = True
      else:
        if currX > 0:
          tentativeX = currX - 1
        else:
          collision = True
      # Colision detection
      for x in range(rockWidth):
        if collision:
          break
        for y in range(rockHeight):
          if rockType[y][x] and chamber[currY + y][tentativeX + x]:
            collision = True
            break
      if not collision:
        currX = tentativeX
      # Falling
      collision = False
      if currY > 0:
        tentativeY = currY - 1
      else:
        collision = True
      # Colision detection
      for x in range(rockWidth):
        if collision:
          break
        for y in range(rockHeight):
          if rockType[y][x] and chamber[tentativeY + y][currX + x]:
            collision = True
            break
      if not collision:
        currY = tentativeY
      else:
        for x in range(rockWidth):
          for y in range(rockHeight):
            if rockType[y][x]:
              chamber[currY + y][currX + x] = True
        while not any(chamber[-1]):
          del chamber[-1]
        break
    currRock += 1
  # printChamber(chamber)
  return len(chamber)


def firstStar(input):
  return simulateChamber(input, 1090)

def secondStar(input):
  return simulateChamber(input, 1e12, True)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3171

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1586627906921
