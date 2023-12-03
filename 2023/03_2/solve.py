from pathlib import Path
from math import log10
from collections import defaultdict

def readInput(file):
  numbers = set()
  parts = set()
  gears = []
  for i, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    number = 0
    for j, c in enumerate(line):
      if c.isdigit():
        number *= 10
        number += int(c)
      else:
        if number > 0:
          numbers.add(((i, j - 1), number))
          number = 0
        if c != '.':
          parts.add((i, j))
          if c == '*':
            gears.append((i, j))
    if number > 0:
      numbers.add(((i, len(line) - 1), number))
      number = 0
  return parts, numbers, gears

def isPart(number, parts):
  (l, c), n = number
  length = int(log10(n)) + 1
  for i in (l - 1, l + 1):
    for j in range(c - length, c + 2):
      if (i, j) in parts:
        return True
  for j in (c - length, c + 1):
    if (l, j) in parts:
      return True
  return False

def isGearRatio(number, gears):
  (l, c), n = number
  length = int(log10(n)) + 1
  for i in (l - 1, l + 1):
    for j in range(c - length, c + 2):
      if (i, j) in gears:
        return (i, j)
  for j in (c - length, c + 1):
    if (l, j) in gears:
      return (l, j)
  return False

def firstStar(input):
  result = 0
  parts, numbers, _ = input
  for number in numbers:
    if isPart(number, parts):
      result += number[1]
  return result

def secondStar(input):
  result = 0
  _, numbers, gears = input
  gearsRatio = defaultdict(list)
  for number in numbers:
    gearToMultiply = isGearRatio(number, gears)
    if gearToMultiply:
      gearsRatio[gearToMultiply].append(number[1])
  for gear in gearsRatio.values():
    if len(gear) == 2:
      result += gear[0]*gear[1]
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 531932

print("The second star is : {}".format(secondStar(input)))
# The second star is : 73646890
