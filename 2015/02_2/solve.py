from pathlib import Path

def readInput(file):
  return tuple(tuple(sorted(int(n) for n in line.split('x'))) for line in Path(__file__).with_name(file).open('r').read().splitlines())

def neededPaper(w, h, l):
  return 3*w*h + 2*w*l + 2*h*l

def neededRibbon(w, h, l):
  return 2*w + 2*h + w*h*l

def firstStar(input):
  result = 0
  for (w, h, l) in input:
    result += neededPaper(w, h, l)
  return result

def secondStar(input):
  result = 0
  for (w, h, l) in input:
    result += neededRibbon(w, h, l)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1598415

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3812909
