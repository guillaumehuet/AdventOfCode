from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  pass

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 33

print("The second star is : {}".format(secondStar(input)))
# The second star is : 57
