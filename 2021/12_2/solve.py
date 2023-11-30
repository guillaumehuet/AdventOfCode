from string import ascii_lowercase
def readInput(file):
  paths = dict()
  for line in open(file).read().splitlines():
    a, b = line.split('-')
    if a in paths:
      paths[a].append(b)
    else:
      paths[a] = [b]
    if b in paths:
      paths[b].append(a)
    else:
      paths[b] = [a]
  return paths

def bfs(graph):
  paths = {('start', )}
  fullPaths = set()
  while paths:
    currPath = paths.pop()
    if currPath[-1] == 'end':
      fullPaths.add(currPath)
    else:
      for neighboor in graph[currPath[-1]]:
        if neighboor[0] not in ascii_lowercase or neighboor not in currPath:
          paths.add(currPath + (neighboor, ))
  return fullPaths

def bfs2(graph):
  paths = {(False, 'start')}
  fullPaths = set()
  while paths:
    currPath = paths.pop()
    if currPath[-1] == 'end':
      fullPaths.add(currPath)
    else:
      for neighboor in graph[currPath[-1]]:
        if neighboor[0] not in ascii_lowercase or neighboor not in currPath:
          paths.add(currPath + (neighboor, ))
        elif currPath[0] == False and neighboor not in ('start', 'end'):
          paths.add((True, ) + currPath[1:] + (neighboor, ))
  return fullPaths

def firstStar(input):
  return len(bfs(input))

def secondStar(input):
  return len(bfs2(input))

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4411

print("The second star is : {}".format(secondStar(input)))
# The second star is : 136767
