from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  result = 0
  for line in input:
    middle = len(line) // 2
    first = line[:middle]
    second = line[middle:]
    for c in first:
      if c in second:
        result += priority(c)
        break
  return result

def priority(c):
  if c.islower():
    return ord(c) - ord('a') + 1
  else:
    return ord(c) - ord('A') + 27

def secondStar(input):
  result = 0
  nGroups = len(input) // 3
  for nGroup in range(nGroups):
    group = input[3*nGroup: 3*(nGroup + 1)]
    for c in group[0]:
      if c in group[1] and c in group[2]:
        result += priority(c)
        break
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 7980

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2881
