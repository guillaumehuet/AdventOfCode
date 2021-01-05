def readInput(file):
  return [int(n) for n in open(file).read().splitlines()[0].split(',')]

def findNthTerm(starting, nth):
  seenNumbers = dict()
  for i, n in enumerate(input[:-1]):
    seenNumbers[n] = i + 1
  n = starting[-1]
  n_1 = starting[-2]
  for i in range(len(starting), nth):
    if n in seenNumbers:
      nextN = i - seenNumbers[n]
    else:
      nextN = 0
    n_1 = n
    n = nextN
    seenNumbers[n_1] = i
  return n

def firstStar(input):
  return findNthTerm(input, 2020)

def secondStar(input):
  return findNthTerm(input, 30000000)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 447

print("The second star is : {}".format(secondStar(input)))
# The second star is : 11721679
