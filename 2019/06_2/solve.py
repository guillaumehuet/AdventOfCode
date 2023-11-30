from pathlib import Path

def readInput(file):
  return sorted([tuple(orbit.split(')')) for orbit in Path(__file__).with_name(file).open('r').read().splitlines()])

def processNode(node, count, orbitDict):
  if node in orbitDict:
    return count + sum(processNode(leaf, count + 1, orbitDict) for leaf in orbitDict[node])
  return count

def pathToCOM(node, invOrbitDict):
  result = [node]
  while node != 'COM':
    node = invOrbitDict[node]
    result.append(node)
  return result


def firstStar(input):
  orbitDict = dict()
  prevA = None
  for (a, b) in input:
    if a == prevA:
      orbitDict[a].append(b)
    else:
      orbitDict[a] = [b]
    prevA = a
  return processNode('COM', 0, orbitDict)

def secondStar(input):
  invOrbitDict = dict()
  for (a, b) in input:
    invOrbitDict[b] = a
  youPath = pathToCOM('YOU', invOrbitDict)
  sanPath = pathToCOM('SAN', invOrbitDict)
  jumps = 0
  for node in youPath:
    if node in sanPath:
      break
    jumps += 1
  
  for node in sanPath:
    if node in youPath:
      break
    jumps += 1
  
  return jumps - 2


input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 150150

print("The second star is : {}".format(secondStar(input)))
# The second star is : 352
