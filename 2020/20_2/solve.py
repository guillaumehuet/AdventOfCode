from pathlib import Path

def readInput(file):
  tileset = dict()
  currentTile = []
  currentTileNumber = -1
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if 'Tile' in line:
      if currentTileNumber != -1:
        tileset[currentTileNumber] = tuple(currentTile)
      currentTileNumber = int(line.split()[1][:-1])
      currentTile = []
    elif line != '':
      currentTile.append(tuple(True if c == '#' else False for c in line))
  tileset[currentTileNumber] = tuple(currentTile)
  return tileset

def getSideSignatures(tile):
  result = []
  # Order of the sides in the list is [North, East, South, West]
  # Order for the orientation of each side is [clockwise, counterclockwise]
  for side in (tile[0], [t[-1] for t in tile], list(reversed(tile[-1])), list(reversed([t[0] for t in tile]))):
    result.append([])
    for direction in (side, reversed(side)):
      n = 0
      for c in direction:
        n <<= 1
        if c:
          n |= 1
      result[-1].append(n)
  return result

def getTransformedPixel(x, y, tile, rotation, mirrored):
  side = len(tile) - 1
  if mirrored:
    x = side - x
  if rotation == 1:
    x, y = side - y, x
  elif rotation == 2:
    x, y = side - x, side - y
  elif rotation == 3:
    x, y = y, side - x
  return tile[y][x]

def printPicture(picture):
  for row in picture:
    line = ''
    for c in row:
      if c:
        line += '#'
      else:
        line += '.'
    print(line)
  print()

def firstStar(input):
  sideSignatures = dict()
  for n, t in input.items():
    sideSignatures[n] = getSideSignatures(t)
  
  result = 1
  for n, s in sideSignatures.items():
    otherSides = set()
    for n2, s2 in sideSignatures.items():
      if n2 != n:
        for side in s2:
          otherSides |= set(side)
    missingSides = 0
    for side in s:
      if not (side[0] in otherSides or side[1] in otherSides):
        missingSides += 1
    if missingSides == 2:
      result *= n
  return result

def secondStar(input):
  sideSignatures = dict()
  for n, t in input.items():
    sideSignatures[n] = getSideSignatures(t)
  
  # Check if every edges have unique combination
  fullListOfEdges = [orientedEdge for tileEdges in sideSignatures.values() for edge in tileEdges for orientedEdge in edge]
  for orientedEdge in fullListOfEdges:
    if fullListOfEdges.count(orientedEdge) > 2:
      return "Error with edge " + str(orientedEdge)
  
  # Find a corner and its orientation (considering it's the top left one)
  # We don't need to evaluate if the tile is mirrored or not since it will define all subsequent mirroring
  for n, s in sideSignatures.items():
    otherSides = set()
    for n2, s2 in sideSignatures.items():
      if n2 != n:
        for side in s2:
          otherSides |= set(side)
    missingSides = 0
    missingSideIds = []
    for sideId, side in enumerate(s):
      if not (side[0] in otherSides or side[1] in otherSides):
        missingSides += 1
        missingSideIds.append(sideId)
    if missingSides == 2:
      # Missing sides are next to one another, they are either [0, 1]/[1, 2]/[2, 3]/[3, 0]
      # The orientation is defined as the side that needs to go on top
      # The side that need to go on top in order to have the piece oriented in the top left corner is either 0 if the missing sides are [3, 0]
      # or the maximum of the pair (1 for [0, 1], 2 for [1, 2], 3 for [2, 3])
      if 0 in missingSideIds and 3 in missingSideIds:
        rotation = 0
      else:
        rotation = max(missingSideIds)
      break
  
  puzzle = dict()
  mirrored = False
  x = 0
  y = 0
  puzzle[(x, y)] = (n, rotation, mirrored)
  foundNextLine = True
  while foundNextLine:
    foundNextPiece = True
    while foundNextPiece:
      # Get the clockwise value of the right side of the current piece:
      side = sideSignatures[n][(rotation + (-1 if mirrored else 1)) % 4][0]
      x += 1
      # Get the next piece going right
      foundNextPiece = False
      for n2, s2 in sideSignatures.items():
        if n2 != n:
          for rotation, values in enumerate(s2):
            if side in values:
              foundNextPiece = True
              # We tested for clockwise right side, it should match to anticlockwise left side, else it is mirrored compared to previous piece
              if values[0] == side:
                mirrored = not mirrored
              n = n2
              # "rotation" points to the left side, we need it to point to the top side
              rotation = (rotation + (-1 if mirrored else 1)) % 4
              puzzle[(x, y)] = (n, rotation, mirrored)
              break
        if foundNextPiece:
          break
    n, rotation, mirrored = puzzle[(0, y)]
    y += 1
    x = 0
    # Get the clockwise value of the bottom side of the current piece:
    side = sideSignatures[n][(rotation + 2) % 4][0]
    foundNextLine = False
    for n2, s2 in sideSignatures.items():
      if n2 != n:
        for rotation, values in enumerate(s2):
          if side in values:
            foundNextLine = True
            # We tested for clockwise bottom side, it should match to anticlockwise top side, else it is mirrored compared to previous piece
            if values[0] == side:
              mirrored = not mirrored
            n = n2
            # "rotation" points to the top side, we need it to represent the top side
            rotation = (rotation) % 4
            puzzle[(x, y)] = (n, rotation, mirrored)
            break
      if foundNextLine:
        break
  
  # Create picture from the puzzle parts
  maxX = max(coord[0] for coord in puzzle) + 1
  maxY = max(coord[1] for coord in puzzle) + 1
  puzzleSide = len(input[puzzle[(0, 0)][0]]) - 2
  width = maxX*puzzleSide
  height = maxY*puzzleSide
  picture = [[False for _ in range(width)] for _ in range(height)]

  for coord in puzzle:
    piece, rotation, mirrored = puzzle[coord]
    for y in range(puzzleSide):
      for x in range(puzzleSide):
        picture[y + coord[1]*puzzleSide][x + coord[0]*puzzleSide] = getTransformedPixel(x + 1, y + 1, input[piece], rotation, mirrored)
  
  pictures = []
  # Create every rotated and mirrored pictures
  for rotation in range(4):
    for mirrored in (False, True):
      pictures.append([])
      for y in range(len(picture)):
        pictures[-1].append([])
        for x in range(len(picture[0])):
          pictures[-1][-1].append(getTransformedPixel(x, y, picture, rotation, mirrored))
  
  seaMonster = [[False]*18 + [True, False],
                [True] + ([False]*4 + [True]*2)*3 + [True],
                [False] + ([True] + [False]*2)*6 + [False]]

  monsterWidth = len(seaMonster[0])
  monsterHeight = len(seaMonster)

  for picture in pictures:
    monsterCount = 0
    for y0 in range(height - monsterHeight):
      for x0 in range(width - monsterWidth):
        notAMonster = False
        for y in range(monsterHeight):
          if notAMonster:
            break
          for x in range(monsterWidth):
            if seaMonster[y][x]:
              if not picture[y + y0][x + x0]:
                notAMonster = True
                break
        if not notAMonster:
          monsterCount += 1
    if monsterCount > 0:
      break
  
  result = sum(sum(row) for row in picture) - sum(sum(row) for row in seaMonster)*monsterCount

  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 23386616781851

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2376
