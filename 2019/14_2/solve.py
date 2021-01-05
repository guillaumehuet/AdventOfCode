from math import ceil
from collections import defaultdict

remaining = defaultdict(lambda : 0)

def tryInt(string):
  try:
    return int(string)
  except:
    return string

def readInput(file):
  result = dict()
  for line in  open(file).read().splitlines():
    reaction = line.split("=>")
    inputChems = tuple(tuple(tryInt(s) for s in c.split(' ') if s) for c in reaction[0].split(','))
    outputChem = tuple(tryInt(s) for s in reaction[1].split(' ') if s)
    result[outputChem[1]] = (outputChem[0], inputChems)
  return result

def branchTree(dictionnary, leaf = 'FUEL', quantity = 1):
  global remaining
  if leaf == 'ORE':
    return quantity
  reaction = dictionnary[leaf]
  quantity = quantity - remaining[leaf]
  if quantity < 0:
    remaining[leaf] = -quantity
    return 0
  else:
    reactionNumber = ceil(quantity/reaction[0])
    remaining[leaf] = reaction[0]*reactionNumber - quantity
    return sum(branchTree(dictionnary, newLeaf[1], reactionNumber*newLeaf[0]) for newLeaf in reaction[1])

def firstStar(input):
  global remaining
  remaining = defaultdict(lambda : 0)
  return branchTree(input)

def secondStar(input):
  global remaining
  remaining = defaultdict(lambda : 0)
  maxFuel = 1
  while branchTree(input, 'FUEL', maxFuel) - 1000000000000 < 0:
    maxFuel *= 10
    remaining = defaultdict(lambda : 0)
  minFuel = maxFuel // 10
  while maxFuel - minFuel > 1:
    avgFuel = (maxFuel + minFuel) // 2
    if branchTree(input, 'FUEL', avgFuel) - 1000000000000 < 0:
      minFuel = avgFuel
    else:
      maxFuel = avgFuel
  return minFuel

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 319014

print("The second star is : {}".format(secondStar(input)))
# The second star is : 4076490
