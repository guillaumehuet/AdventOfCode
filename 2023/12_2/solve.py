from pathlib import Path
from functools import cache

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    (springs, check) = line.split()
    result.append((springs, tuple(int(n) for n in check.split(','))))
  return tuple(result)

@cache
def countSprings(springs, check):
  if len(check) == 0:
    if '#' in springs:
      return 0
    else:
      return 1
  miniLength = sum(check) + len(check) - 1
  actualLength = len(springs)
  dof = actualLength - miniLength
  if dof == 0:
    for k, v in enumerate(check):
      if '.' in springs[sum(check[:k]) + k:sum(check[:k + 1]) + k]:
        return 0
      if '#' in springs[sum(check[:k + 1]) + k:sum(check[:k + 1]) + k + 1]:
        return 0
    return 1
  result = 0
  for i in range(dof + 1):
    if '#' not in springs[:i] and '.' not in springs[i:i + check[0]] and (len(springs) <= i + check[0] or springs[i + check[0]] != '#'):
      result += countSprings(springs[i + check[0] + 1:], check[1:])
  return result

def unfold(springs, check):
  return (5*(springs + '?'))[:-1], 5*check

def firstStar(input):
  result = 0
  for i, (springs, check) in enumerate(input):
    result += countSprings(springs, check)
  return result

def secondStar(input):
  result = 0
  for i, (springs, check) in enumerate(input):
    springs, check = unfold(springs, check)
    result += countSprings(springs, check)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 8419

print("The second star is : {}".format(secondStar(input)))
# The second star is : 160500973317706
