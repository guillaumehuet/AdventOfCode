from pathlib import Path
import re

from pyparsing import line

def readInput(file):
  return Path(__file__).with_name(file).open('r').read()

def firstStar(input):
  total = 0
  matches = re.findall("mul\((\d+),(\d+)\)", input)
  for x, y in matches:
    total += int(x) * int(y)
  return total

def secondStar(input):
  total = 0
  start = re.search(".*", input)
  stopValue = 0
  while start != None:
    startValue = start.start() + stopValue
    stop = re.search("don\'t\(\)", input[startValue:])
    stopValue = stop.start() + startValue if stop != None else len(input)
    matches = re.findall("mul\((\d+),(\d+)\)", input[startValue:stopValue])
    for x, y in matches:
      total += int(x) * int(y)
    start = re.search("do\(\)", input[stopValue:])
  return total

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 191183308

print("The second star is : {}".format(secondStar(input)))
# The second star is : 92082041
