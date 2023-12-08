from pathlib import Path
from math import lcm

def readInput(file):
  dirs = {'L' : 0, 'R' : 1}
  lines = Path(__file__).with_name(file).open('r').read().splitlines()
  sequence = tuple(dirs[dirLetter] for dirLetter in lines[0])
  graph = dict()
  for line in lines[2:]:
    node, _, left, right = line.split()
    left = left[1:-1]
    right = right[:-1]
    graph[node] = (left, right)
  return sequence, graph

def findNextZorANode(node, sequence, graph, startIndex = 0):
  i = startIndex
  m = len(sequence)
  while node[-1] not in 'AZ':
    node = graph[node][sequence[i%m]]
    i += 1
  return i, node

def firstStar(input):
  sequence, graph = input
  i = 0
  m = len(sequence)
  node = 'AAA'
  while node != 'ZZZ':
    node = graph[node][sequence[i%m]]
    i += 1
  return i

def secondStar(input):
  sequence, graph = input
  nodes = [node for node in graph if node[-1] == 'A']
  cycleLengths = []
  cycleStarts = []
  m = len(sequence)
  startNodes = tuple(nodes)
  for node in nodes:
    node = graph[node][sequence[0%m]]
    i, node  = findNextZorANode(node, sequence, graph, 1)
    firstReach = i
    firstReachNode = node
    cycleStarts.append(firstReach)
    if firstReachNode[-1] != 'Z':
      return 'Case with interlinked cycles not implemented'
    node = graph[node][sequence[i%m]]
    i, node  = findNextZorANode(node, sequence, graph, i + 1)
    if node != firstReachNode:
      return 'Case with interlinked cycles not implemented'
    cycleLengths.append(i - firstReach)
  if cycleLengths != cycleStarts:
    return 'Offset in modular arithmetics not implemented'
  result = 1
  for cycle in cycleLengths:
    result = lcm(result, cycle)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 22357

print("The second star is : {}".format(secondStar(input)))
# The second star is : 10371555451871
