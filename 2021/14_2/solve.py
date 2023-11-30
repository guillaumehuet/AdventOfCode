from pathlib import Path

def readInput(file):
  lines = Path(__file__).with_name(file).open('r').read().splitlines()
  template = lines[0]
  rules = dict()
  for l in lines[2:]:
    pair, insertion = l.split(' -> ')
    rules[pair] = insertion
  return template, rules

def step(polymer, rules):
  result = polymer[0]
  for i in range(len(polymer) - 1):
    insertion = rules[polymer[i:i + 2]]
    result += insertion + polymer[i + 1]
  return result

def countDoubles(polymer):
  doubles = dict()
  for i in range(len(polymer) - 1):
    index = polymer[i:i + 2]
    if index in doubles:
      doubles[index] += 1
    else:
      doubles[index] = 1
  return doubles

def stepDoubles(doubles, rules):
  result = dict()
  for double in doubles:
    insertion = rules[double]
    first = double[0] + insertion
    second = insertion + double[1]
    if first in result:
      result[first] += doubles[double]
    else:
      result[first] = doubles[double]
    if second in result:
      result[second] += doubles[double]
    else:
      result[second] = doubles[double]
  return result

def countSingles(doubles, template):
  result = {template[-1] : 1}
  for double in doubles:
    first = double[0]
    if first in result:
      result[first] += doubles[double]
    else:
      result[first] = doubles[double]
  return result

def minMaxElement(polymer):
  counts = dict()
  for element in polymer:
    if element in counts:
      counts[element] += 1
    else:
      counts[element] = 1
  return max(counts.values()) - min(counts.values())

def firstStar(input):
  polymer, rules = input
  generations = 10
  for s in range(generations):
    polymer = step(polymer, rules)
  return minMaxElement(polymer)

def secondStar(input):
  template, rules = input
  doubles = countDoubles(template)
  generations = 40
  for s in range(generations):
    doubles = stepDoubles(doubles, rules)
  singles = countSingles(doubles, template)
  return max(singles.values()) - min(singles.values())

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2360

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2967977072188
