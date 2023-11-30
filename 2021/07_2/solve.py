from pathlib import Path
from statistics import mean, median
from math import floor, ceil

def readInput(file):
  return tuple(int(n) for n in Path(__file__).with_name(file).open('r').read().splitlines()[0].split(','))

def firstStar(input):
  med =  int(median(input))
  result = sum(abs(i - med) for i in input)
  return result

def distance(input, m):
  return sum(abs(i - m)*(abs(i - m) + 1)//2 for i in input)

def secondStar(input):
  xmin = min(input)
  xmax = max(input)
  ymin = distance(input, xmin)
  ymax = distance(input, xmax)
  while xmax != xmin:
    if ymin > ymax:
      xmin = ceil((xmin + xmax) / 2)
      ymin = distance(input, xmin)
    else:
      xmax = floor((xmin + xmax) / 2)
      ymax = distance(input, xmax)
  return distance(input, xmin)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 336701

print("The second star is : {}".format(secondStar(input)))
# The second star is : 95167302
