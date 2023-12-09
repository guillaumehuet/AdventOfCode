from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append(tuple(int(n) for n in line.split()))
  return tuple(result)

def differentiate(l):
  result = []
  for v1, v2 in zip(l[:-1], l[1:]):
    result.append(v2 - v1)
  return tuple(result)

def integrate(diffs):
  return sum(d[-1] for d in diffs)

def integrateBefore(diffs):
  result = 0
  for d in reversed(diffs):
    result = d[0] - result
  return result

def firstStar(input):
  result = 0
  for line in input:
    diffLevel = 0
    diffs = []
    currDiff = line
    while any(currDiff):
      diffLevel += 1
      diffs.append(currDiff)
      currDiff = differentiate(currDiff)
    result += integrate(diffs)
  return result

def secondStar(input):
  result = 0
  for line in input:
    diffLevel = 0
    diffs = []
    currDiff = line
    while any(currDiff):
      diffLevel += 1
      diffs.append(currDiff)
      currDiff = differentiate(currDiff)
    result += integrateBefore(diffs)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1696140818

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1152
