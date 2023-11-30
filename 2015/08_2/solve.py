from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def decodeLen(strings):
  result = 0
  for s in strings:
    result += 2
    escaped = False
    hexEsc = 0
    for c in s[1:-1]:
      if not escaped and c == '\\':
        result += 1
        escaped = True
      elif escaped:
        if c in '\\"':
          escaped = False
        else:
          hexEsc += 1
          if hexEsc == 3:
            result += 2
            hexEsc = 0
            escaped = False
  return result

def encodeLen(strings):
  result = 0
  for s in strings:
    result += 2
    for c in s:
      if c in '\\"':
        result += 1
  return result

def firstStar(input):
  return decodeLen(input)

def secondStar(input):
  return encodeLen(input)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1371

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2117
