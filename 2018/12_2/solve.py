from itertools import product

def readInput(file):
  lines = open(file).read().splitlines()
  initial = lines[0][15:]
  initial = tuple(True if c == '#' else False for c in initial)
  
  rules = dict(tuple(tuple(True if c == '#' else False for c in r.replace(' ','')) for r in l.split('=>')) for l in lines[2:])
  
  for r in product((True, False), repeat = 5):
    if r not in rules:
      rules[r] = False
    else:
      rules[r] = rules[r][0]
  
  return initial, rules

def firstStar(input):
  return evolveRounds(input, 20)

def evolve(pots, rules):
  pots = [False]*4 + pots + [False]*4
  newPots = [rules[tuple(pots[i + j] for j in range(5))] for i in range(len(pots) - 4)]
  return newPots

def evolveRounds(input, rounds):
  offset = 0
  pots = list(input[0])
  rules = input[1]
  for r in range(rounds):
    newPots = evolve(pots, rules)
    oldOffset = offset
    offset += 2
    i = 0
    while True:
      if newPots[i] != False:
        break
      i += 1
    j = -1
    while True:
      if newPots[j] != False:
        break
      j -= 1
    offset -= i
    newPots = newPots[i:len(newPots) + j + 1]
    if hash(tuple(pots)) == hash(tuple(newPots)):
      return potsToScore(pots, oldOffset + (rounds - r)*(offset - oldOffset))
    pots = newPots
  return potsToScore(pots, offset)

def potsToScore(pots, offset):
  result = 0
  for i, k in enumerate(pots):
    if k:
      result += i - offset
  return result

def secondStar(input):
  return evolveRounds(input, 50000000000)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3421

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2550000001195
