from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def readAround(input, i, j, inci, incj):
  result = ''
  for k in range(4):
    newI = i + inci*k
    newJ = j + incj*k
    if newI < 0 or newI >= len(input) or newJ < 0 or newJ >= len(input[0]):
      return result
    result += input[newI][newJ]
  return result

def countAround(input, i, j):
  result = 0
  for inci in range(-1, 2):
    for incj in range(-1, 2):
      if inci == 0 and incj == 0:
        continue
      if readAround(input, i, j, inci, incj) == 'XMAS':
          result += 1
  return result

def xMas(input, i, j):
  tl = input[i-1][j-1]
  tr = input[i-1][j+1]
  bl = input[i+1][j-1]
  br = input[i+1][j+1]
  if (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M'):
    if (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'):
      return 1
  return 0

def firstStar(input):
  result = 0
  columns = len(input[0])
  rows = len(input)
  for i in range(rows):
    for j in range(columns):
        if input[i][j] == 'X':
          result += countAround(input, i, j)
  return result

def secondStar(input):
  result = 0
  columns = len(input[0])
  rows = len(input)
  for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        if input[i][j] == 'A':
          result += xMas(input, i, j)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2350

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1921
