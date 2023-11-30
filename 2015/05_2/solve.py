def readInput(file):
  return open(file).read().splitlines()

def threeVowels(input):
  result = 0
  for c in input:
    if c in 'aeiou':
      result += 1
    if result >= 3:
      return True
  return False

def letterTwiceInARow(input):
  prev = ''
  for c in input:
    if c == prev:
      return True
    prev = c
  return False

def noForbiddenString(input):
  if 'ab' in input or 'cd' in input or 'pq' in input or 'xy' in input:
    return False
  return True

def twoLettersTwice(input):
  prev = input[0]
  for i, c in enumerate(input[1:]):
    pair = prev + c
    prev = c
    if pair in input[i + 2:]:
      return True
  return False

def repeatingLetterSandwich(input):
  for i, c in enumerate(input[:-2]):
    if input[i + 2] == c:
      return True
  return False

def firstStar(input):
  result = 0
  for line in input:
    if noForbiddenString(line) and threeVowels(line) and letterTwiceInARow(line):
      result += 1
  return result

def secondStar(input):
  result = 0
  for line in input:
    if repeatingLetterSandwich(line) and twoLettersTwice(line):
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 255

print("The second star is : {}".format(secondStar(input)))
# The second star is : 55
