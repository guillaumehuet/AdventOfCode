from pathlib import Path
from collections import Counter

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  n2 = 0
  n3 = 0

  for line in input:
    c = Counter(line).values()
    if 2 in c:
      n2 += 1
    if 3 in c:
      n3 += 1

  return n2*n3

def secondStar(input):
  for i in range(len(input)):
    for j in range(i + 1, len(input)):
      if areClose(input[i], input[j]):
        return common(input[i], input[j])

def areClose(str1, str2):
  diff = 0
  n = len(str1)
  if n != len(str2):
    return False
  for i in range(n):
    if str1[i] != str2[i]:
      diff += 1
      if diff > 1:
        return False
  if diff == 1:
    return True
  return False

def common(str1, str2):
  n = len(str1)
  result = ""
  for i in range(n):
    c = str1[i]
    if c == str2[i]:
      result += c
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 7221

print("The second star is : {}".format(secondStar(input)))
# The second star is : mkcdflathzwsvjxrevymbdpoq
