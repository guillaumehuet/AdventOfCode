from copy import deepcopy

def readInput(file):
  return tuple(tuple(True if c == 'L' else False for c in line) for line in open(file).read().splitlines())

def printState(seatLayout, seatState):
  for y in range(len(seatLayout)):
    line = ''
    for x in range(len(seatLayout[y])):
      if not seatLayout[y][x]:
        line += '.'
      else:
        if seatState[y][x]:
          line += '#'
        else:
          line += 'L'
    print(line)
  print()

def sumNeighbors1(y, x, seatState, _):
  result = 0
  for j in range(y - 1, y + 2):
    if 0 <= j < len(seatState):
      for i in range(x - 1, x + 2):
        if 0 <= i < len(seatState[j]):
          if (i, j) != (x, y):
            result += seatState[j][i]
  return result

def sumNeighbors2(y, x, seatState, seatLayout):
  result = 0
  for j in range(-1, 2):
      for i in range(-1, 2):
        if (i, j) != (0, 0):
          step = 1
          while True:
            y_ = y + step*j
            x_ = x + step*i
            if 0 <= x_ < len(seatState[0]) and 0 <= y_ < len(seatState):
              if seatLayout[y_][x_]:
                result += seatState[y_][x_]
                break
              else:
                step += 1
            else:
              break
  return result

def generation(seatLayout, seatState, sumFunction = sumNeighbors1, leaveThreshold = 4):
  newState = list(list(line) for line in seatState)
  for y in range(len(seatLayout)):
    for x in range(len(seatLayout[y])):
      if seatLayout[y][x]:
        count = sumFunction(y, x, seatState, seatLayout)
        state = seatState[y][x]
        if not state and count == 0:
          newState[y][x] = 1
        elif state and count >= leaveThreshold:
          newState[y][x] = 0
  return tuple(tuple(line) for line in newState)

def firstStar(input):
  seatLayout = input
  seatState = tuple((0, )*len(input[0]) for _ in range(len(input)))
  hashState = hash(seatState)
  while True:
    seatState = generation(seatLayout, seatState)
    newHashState = hash(seatState)
    if newHashState == hashState:
      return sum(sum(line) for line in seatState)
    else:
      hashState = newHashState

def secondStar(input):
  seatLayout = input
  seatState = tuple((0, )*len(input[0]) for _ in range(len(input)))
  hashState = hash(seatState)
  while True:
    seatState = generation(seatLayout, seatState, sumNeighbors2, 5)
    newHashState = hash(seatState)
    if newHashState == hashState:
      return sum(sum(line) for line in seatState)
    else:
      hashState = newHashState

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2126

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1914
