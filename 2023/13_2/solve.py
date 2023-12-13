from pathlib import Path

def readInput(file):
  result = []
  currPattern = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      result.append(tuple(currPattern))
      currPattern = []
    else:
      currPattern.append(tuple(c == '#' for c in line))
  result.append(tuple(currPattern))
  return tuple(result)

def printPattern(pattern):
  for line in pattern:
    for c in line:
      if c:
        print('#', end='')
      else:
        print('.', end='')
    print()

def transpose(pattern):
  result = []
  for i in range(len(pattern[0])):
    result.append([])
    for j in range(len(pattern)):
      result [-1].append(pattern[j][i])
    result[-1] = tuple(result[-1])
  return tuple(result)

def checkVertical(pattern, symPlane):
  for i in range(min(symPlane, len(pattern) - symPlane)):
    if pattern[symPlane - 1 - i] != pattern[symPlane + i]:
      return False
  return True

def score(pattern, skip=0):
  for symPlane in range(1, len(pattern)):
    if checkVertical(pattern, symPlane):
      if 100*symPlane != skip:
        return 100*symPlane
  pattern = transpose(pattern)
  for symPlane in range(1, len(pattern)):
    if checkVertical(pattern, symPlane):
      if symPlane != skip:
        return symPlane
  return 0

def smudge(pattern, i, j):
  return pattern[:i] + ((pattern[i][:j] + (not(pattern[i][j]), ) + pattern[i][j + 1:]), ) + pattern[i + 1:]

def smudgeScore(pattern):
  baseScore = score(pattern)
  for i in range(len(pattern)):
    for j in range(len(pattern[0])):
      newScore = score(smudge(pattern, i, j), skip = baseScore)
      if newScore != 0 and newScore != baseScore:
        return newScore

def firstStar(input):
  result = 0
  for pattern in input:
    result += score(pattern)
  return result

def secondStar(input):
  result = 0
  for pattern in input:
    result += smudgeScore(pattern)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 32723

print("The second star is : {}".format(secondStar(input)))
# The second star is : 34536
