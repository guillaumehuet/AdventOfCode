secondStarResult = 0

def readInput(file):
  beacons = []
  for line in open(file).read().splitlines():
    if 'scanner' in line:
      beacons.append([])
    elif line != '':
      beacons[-1].append([int(n) for n in line.split(',')])
  return beacons

def manhattantDistance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def distanceMatrix(scannerBeacons):
  result = []
  size = len(scannerBeacons)
  for i in range(size):
    result.append([])
    for j in range(size):
      result[-1].append(manhattantDistance(scannerBeacons[i], scannerBeacons[j]))
  return result

def correlate(distancesA, distancesB):
  commonBeacons = []
  for i, a in enumerate(distancesA):
    for j, b in enumerate(distancesB):
      margin = len(a) + len(b) - len(set(a)) - len(set(b))
      common = len(set(a) & set(b))
      if margin + common >= 12:
        commonBeacons.append((i, j))
  return commonBeacons

def firstStar(input):
  global secondStarResult
  d = []
  for scannerBeacons in input:
    d.append(distanceMatrix(scannerBeacons))
  
  maxD = len(d)
  commons = dict()
  for i in range(maxD):
    for j in range(i + 1, maxD):
      c = correlate(d[i], d[j])
      if len(c) > 0:
        commons[i,j] = c
  rotated = [0]
  deltas = {0: (0, 0, 0)}
  while len(rotated) < len(input):
    for (i, j) in commons:
      if j in rotated and i not in rotated:
        commons[(j, i)] = [(nJ, nI) for (nI, nJ) in commons[(i, j)]]
        del commons[(i, j)]
        i, j = j, i
      if i in rotated and j not in rotated:
        for r in range(24):
          delta = None
          for (nI, nJ) in commons[(i, j)]:
            xI, yI, zI = input[i][nI]
            xJ, yJ, zJ = input[j][nJ]
            orientation = r % 6
            if orientation == 1:
              xJ, yJ = yJ, -xJ
            elif orientation == 2:
              xJ, yJ = -xJ, -yJ
            elif orientation == 3:
              xJ, yJ = -yJ, xJ
            elif orientation == 4:
              xJ, zJ = zJ, -xJ
            elif orientation == 5:
              xJ, zJ = -zJ, xJ
            rotation = r // 6
            if rotation == 1:
              yJ, zJ = zJ, -yJ
            elif rotation == 2:
              yJ, zJ = -yJ, -zJ
            elif rotation == 3:
              yJ, zJ = -zJ, yJ
            newDelta = (xJ - xI, yJ - yI, zJ - zI)
            if delta is not None:
              if newDelta != delta:
                break
            else:
              delta = newDelta
          else:
            deltas[j] = delta
            for index, (xJ, yJ, zJ) in enumerate(input[j]):
              orientation = r % 6
              if orientation == 1:
                xJ, yJ = yJ, -xJ
              elif orientation == 2:
                xJ, yJ = -xJ, -yJ
              elif orientation == 3:
                xJ, yJ = -yJ, xJ
              elif orientation == 4:
                xJ, zJ = zJ, -xJ
              elif orientation == 5:
                xJ, zJ = -zJ, xJ
              rotation = r // 6
              if rotation == 1:
                yJ, zJ = zJ, -yJ
              elif rotation == 2:
                yJ, zJ = -yJ, -zJ
              elif rotation == 3:
                yJ, zJ = -zJ, yJ
              xJ -= delta[0]
              yJ -= delta[1]
              zJ -= delta[2]
              input[j][index] = [xJ, yJ, zJ]
            rotated.append(j)
            break
  sMax = len(deltas)
  maxScannerDistance = 0
  for s1 in range(sMax):
    for s2 in range(s1 + 1, sMax):
      maxScannerDistance = max(maxScannerDistance, manhattantDistance(deltas[s1], deltas[s2]))
  secondStarResult = maxScannerDistance
  unique = set()
  for scanner in input:
    for beacon in scanner:
      unique.add(tuple(beacon))
  return len(unique)

def secondStar(input):
  return secondStarResult

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 436

print("The second star is : {}".format(secondStar(input)))
# The second star is : 10918
