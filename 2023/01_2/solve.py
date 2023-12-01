from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def lineToNumber(line):
  result = 0
  for c in line:
    if c.isdigit():
      result += 10*int(c)
      break
  for c in reversed(line):
    if c.isdigit():
      result += int(c)
      break
  return result

def lineToNumberAlpha(line):
  result = 0
  alphaNum = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
  bestIndex = len(line) + 1
  bestDigit = 0
  for n in range(10):
    index = line.find(str(n))
    if index != -1 and index < bestIndex:
      bestIndex = index
      bestDigit = n
  for alpha in alphaNum:
    index = line.find(alpha)
    if index != -1 and index < bestIndex:
      bestIndex = index
      bestDigit = alphaNum[alpha]
  result = 10*bestDigit
  bestIndex = -1
  bestDigit = 0
  for n in range(10):
    index = line.rfind(str(n))
    if index > bestIndex:
      bestIndex = index
      bestDigit = n
  for alpha in alphaNum:
    index = line.rfind(alpha)
    if index > bestIndex:
      bestIndex = index
      bestDigit = alphaNum[alpha]
  result += bestDigit
  return result

def firstStar(input):
  return sum(lineToNumber(line) for line in input)

def secondStar(input):
  return sum(lineToNumberAlpha(line) for line in input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 55488

print("The second star is : {}".format(secondStar(input)))
# The second star is : 55614
