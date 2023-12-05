from pathlib import Path

def readInput(file):
  currDepth = 0
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if line == "":
      currDepth += 1
    elif currDepth == 0:
      result.append(tuple(int(n) for n in line.split(':')[1].split()))
    elif line == "":
      currDepth += 1
    elif ":" in line:
      result[-1] = tuple(result[-1])
      result.append([])
    else:
      result[-1].append(tuple(int(n) for n in line.split()))
  result[-1] = tuple(result[-1])
  return tuple(result)

def almanacToRangeDelta(alamanac):
  result = []
  for d in alamanac[1:]:
    result.append([])
    for r in d:
      minRange = r[1]
      maxRange = r[1] + r[2] - 1
      delta = r[0] - r[1]
      result[-1].append((minRange, maxRange, delta))
    result[-1].sort()
    previousMax = result[-1][0][0] - 1
    for r in result[-1].copy():
      if r[0] - 1 != previousMax:
        result[-1].append((previousMax + 1, r[0] - 1, 0))
      previousMax = r[1]
    result[-1].sort()
    result[-1] = tuple(result[-1])
  return tuple(result)

def goDeeper(state, rangeDeltaDepth):
  result = []
  for s in state:
    for r in rangeDeltaDepth:
      if r[0] <= s <= r[1]:
        s += r[2]
        break
    result.append(s)
  result.sort()
  return tuple(result)

def goDeeperRange(state, rangeDeltaDepth):
  result = []
  for s in state:
    newS = []
    if s[0] < rangeDeltaDepth[0][0]:
      newS.append((s[0], min(s[1], rangeDeltaDepth[0][0] - 1)))
    for r in rangeDeltaDepth:
      if r[1] < s[0]:
        continue
      if s[1] < r[0]:
        break
      newS.append((max(s[0], r[0]) + r[2], min(s[1], r[1]) + r[2]))
    if s[1] > rangeDeltaDepth[-1][1]:
      newS.append((max(s[0], rangeDeltaDepth[-1][1] + 1), s[1]))
    result += newS
  result.sort()
  return tuple(result)

def firstStar(input):
  almanac = input
  state = almanac[0]
  rangeDelta = almanacToRangeDelta(almanac)
  for depth in range(len(rangeDelta)):
    state = goDeeper(state, rangeDelta[depth])
  return min(state)

def secondStar(input):
  almanac = input
  state = []
  for i in range(int(len(almanac[0]) / 2)):
    state.append((almanac[0][2*i],  almanac[0][2*i] + almanac[0][2*i+1] - 1))
  state.sort()
  state = tuple(state)
  rangeDelta = almanacToRangeDelta(almanac)
  for depth in range(len(rangeDelta)):
    state = goDeeperRange(state, rangeDelta[depth])
  return min(state)[0]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 84470622

print("The second star is : {}".format(secondStar(input)))
# The second star is : 26714516
