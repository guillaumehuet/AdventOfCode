def readInput(file):
  return open(file).read().splitlines()[0]

def firstStar(input):
  floor = 0
  for c in input:
    if c == '(':
      floor += 1
    elif c == ')':
      floor -= 1
  return floor

def secondStar(input):
  floor = 0
  for i, c in enumerate(input):
    if c == '(':
      floor += 1
    elif c == ')':
      floor -= 1
      if floor == -1:
        return i + 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 232

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1783
