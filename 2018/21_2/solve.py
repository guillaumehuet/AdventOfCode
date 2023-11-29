from pathlib import Path

def reversedFunction():
  d = 0
  x = 4591209
  y = 65899
  y2 = y**2 % 2**24
  y3 = y**3 % 2**24
  while True:
    d = (x*y3 + (d % 2**8)*y3 + ((d >> 8) % 2**8)*y2 + (((d >> 16) | 1) % 2**8)*y) % 2**24
    yield d

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  return next(reversedFunction())

def secondStar(input):
  generator = reversedFunction()
  result = set()
  prevValue = 0
  nextValue = next(generator)
  while nextValue not in result:
    prevValue = nextValue
    result.add(nextValue)
    nextValue = next(generator)
  return prevValue

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 12446070

print("The second star is : {}".format(secondStar(input)))
# The second star is : 13928239
