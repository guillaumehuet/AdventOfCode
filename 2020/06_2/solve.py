from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  result = 0
  group = [set()]
  for line in input:
    if line == '':
      result += len(group[-1])
      group.append(set())
    else:
      group[-1] |= set(line)
  result += len(group[-1])
  return result


def secondStar(input):
  full = 'abcdefghijklmnopqrstuvwxyz'
  result = 0
  group = [set(full)]
  for line in input:
    if line == '':
      result += len(group[-1])
      group.append(set(full))
    else:
      group[-1] &= set(line)
  result += len(group[-1])
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 6521

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3305
