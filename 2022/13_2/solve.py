from pathlib import Path
from json import loads
from itertools import zip_longest

class packet(list):
  def __le__(self, other):
    for (i, j) in zip_longest(self, other):
      if isinstance(i, list):
        i = packet(i)
      if isinstance(j, list):
        j = packet(j)
      if isinstance(i, int) and isinstance(j, int):
        if i > j:
          return False
        if i < j:
          return True
      elif isinstance(i, packet) and isinstance(j, packet):
        if i > j:
          return False
        if i < j:
          return True
      else:
        if i is None:
          return True
        if j is None:
          return False
        if isinstance(i, int):
          i = packet([i])
        else:
          j = packet([j])
        if i > j:
          return False
        if i < j:
          return True
    return True
  
  def __ge__(self, other):
    return other <= self
  
  def __eq__(self, other):
    return self <= other and other <= self

  def __lt__(self, other):
    return not other <= self
  
  def __gt__(self, other):
    return not self <= other

def readInput(file):
  result = [[]]
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      result.append([])
    else:
      result[-1].append(loads(line))
  return result

def firstStar(input):
  result = 0
  pair = 1
  for left, right in input:
    left = packet(left)
    right = packet(right)
    if left < right:
      result += pair
    pair += 1
  return result

def secondStar(input):
  firstDivider = packet([[2]])
  secondDivider = packet([[6]])
  packets = packet()
  packets.append(firstDivider)
  packets.append(secondDivider)
  for left, right in input:
    packets.append(packet(left))
    packets.append(packet(right))
  packets.sort()
  result = packets.index(firstDivider) + 1
  result *= packets.index(secondDivider) + 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 5340

print("The second star is : {}".format(secondStar(input)))
# The second star is : 21276
