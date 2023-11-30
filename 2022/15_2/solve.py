from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    line = line.split()
    sensorX = line[2]
    sensorY = line[3]
    beaconX = line[-2]
    beaconY = line[-1]

    sensorX = int(sensorX.split('=')[1][:-1])
    sensorY = int(sensorY.split('=')[1][:-1])
    beaconX = int(beaconX.split('=')[1][:-1])
    beaconY = int(beaconY.split('=')[1])

    result.append((sensorX, sensorY, beaconX, beaconY))
  return tuple(result)

def firstStar(input):
  row = 2000000
  sensorRow = []
  beaconsInRow = set()
  for sensor in input:
    sensorRange = abs(sensor[3] - sensor[1]) + abs(sensor[2] - sensor[0])
    rowDelta = abs(row - sensor[1])
    if sensor[3] == row:
      beaconsInRow.add(sensor[2:])
    if rowDelta <= sensorRange:
      minX = sensor[0] - (sensorRange - rowDelta)
      maxX = sensor[0] + (sensorRange - rowDelta)
      sensorRow.append((minX, maxX))
  sensorRow.sort()
  i = 0
  while True:
    if i + 2 > len(sensorRow):
      break
    if sensorRow[i][1] >= sensorRow[i + 1][0]:
      minX = min(sensorRow[i][0], sensorRow[i + 1][0])
      maxX = max(sensorRow[i][1], sensorRow[i + 1][1])
      sensorRow[i:i + 2] = [(minX, maxX)]
    else:
      i += 1
  result = 0
  for s in sensorRow:
    result += s[1] + 1 - s[0]
  result -= len(beaconsInRow)
  return result

def secondStar(input):
  sensorRange = []
  for sensor in input:
    sensorRange.append(sensor[:2] + (abs(sensor[3] - sensor[1]) + abs(sensor[2] - sensor[0]),))
  sensorRange = tuple(sensorRange)
  for row in range(4000000):
    sensorRow = []
    for sensor in sensorRange:
      rowDelta = abs(row - sensor[1])
      if rowDelta <= sensor[2]:
        minX = sensor[0] - (sensor[2] - rowDelta)
        maxX = sensor[0] + (sensor[2] - rowDelta)
        sensorRow.append((minX, maxX))
    sensorRow.sort()
    i = 0
    while True:
      if i + 2 > len(sensorRow):
        break
      if sensorRow[i][1] >= sensorRow[i + 1][0]:
        minX = min(sensorRow[i][0], sensorRow[i + 1][0])
        maxX = max(sensorRow[i][1], sensorRow[i + 1][1])
        sensorRow[i:i + 2] = [(minX, maxX)]
      else:
        i += 1
    if len(sensorRow) > 1:
      for i in range(len(sensorRow) - 1):
        if 0 < sensorRow[i][1] + 1 < 4000000:
          return row + (sensorRow[i][1] + 1)*4000000
    if sensorRow[0][0] > 0:
      return row
    if sensorRow[-1][1] < 4000000:
      return row + 4000000*4000000

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4665948

print("The second star is : {}".format(secondStar(input)))
# The second star is : 13543690671045
