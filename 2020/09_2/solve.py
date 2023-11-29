from pathlib import Path

def readInput(file):
  return [int(n) for n in Path(__file__).with_name(file).open('r').read().splitlines()]

def firstErrNumber(nList, preambleLen):
  for i in range(preambleLen, len(nList)):
    found = False
    for j in range(1, preambleLen):
      for k in range(j + 1, preambleLen + 1):
        if nList[i - j] + nList[i - k] == nList[i]:
          found = True
          break
      if found == True:
        break
    if not found:
      return nList[i]

def firstStar(input):
  return firstErrNumber(input, 25)

def secondStar(input):
  target = firstStar(input)
  for i in range(len(input)):
    j = 0
    currSum = input[i]
    while currSum < target:
      j += 1
      currSum += input[i + j]
    if currSum == target:
      return min(input[i:i + j + 1]) + max(input[i:i + j + 1])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 10884537

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1261309
