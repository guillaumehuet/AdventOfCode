from pathlib import Path

def readInput(file):
  return tuple(tuple(int(i) for i in line) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def firstStar(input):
  result = 0
  width = len(input[0])
  height = len(input)
  for i in range(width):
    for j in range(height):
      value = input[j][i]
      visible = False
      for dir in (-1, 0), (0, 1), (1, 0), (0, -1):
        curr = (i, j)
        while True:
          curr = (curr[0] + dir[0], curr[1] + dir[1])
          if curr[0] < 0 or curr[0] >= width or curr[1] < 0 or curr[1] >= height:
            result += 1
            visible = True
            break
          if input[curr[1]][curr[0]] >= value:
            break
        if visible:
          break
  return result

def secondStar(input):
  bestCoords = (0, 0)
  bestScore = 0
  width = len(input[0])
  height = len(input)
  for i in range(width):
    for j in range(height):
      value = input[j][i]
      score = 1
      for dir in (-1, 0), (0, 1), (1, 0), (0, -1):
        dirScore = 0
        curr = (i, j)
        while True:
          curr = (curr[0] + dir[0], curr[1] + dir[1])
          if curr[0] < 0 or curr[0] >= width or curr[1] < 0 or curr[1] >= height:
            break
          if input[curr[1]][curr[0]] >= value:
            dirScore += 1
            break
          else:
            dirScore += 1
        score *= dirScore
      if score > bestScore:
        bestScore = score
  return bestScore

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1820

print("The second star is : {}".format(secondStar(input)))
# The second star is : 385112
