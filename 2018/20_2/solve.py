from pathlib import Path

def move(pos, dir):
  directions = {'N' : (0, -1), 'S' : (0, 1), 'W' : (-1, 0), 'E' : (1, 0)}
  return (pos[0] + directions[dir][0], pos[1] + directions[dir][1])

def goThrough(regex, origDistance = 0, origin = (0, 0), visited = None, distances = None):
  visited = visited or set()
  distances = distances or dict()
  pos = origin
  distance = origDistance
  visited.add(pos)
  distances[pos] = distance
  c = 0
  while c < len(regex):
    direction = regex[c]
    if direction in ('N', 'S', 'W', 'E'):
      pos = move(pos, direction)
      if pos in visited:
        distance = distances[pos]
      else:
        distance += 1
        distances[pos] = distance
        visited.add(pos)
    elif direction == '|':
      pos = origin
      distance = origDistance
    elif direction == '(':
      subRegexStart = c
      subRegexEnd = subRegexStart
      depth = 1
      while depth > 0:
        subRegexEnd += 1
        if regex[subRegexEnd] == '(':
          depth += 1
        elif regex[subRegexEnd] == ')':
          depth -= 1
      goThrough(regex[subRegexStart + 1:subRegexEnd], distance, pos, visited, distances)
      c = subRegexEnd
    c += 1
  return distances

def readInput(file):
  return goThrough(Path(__file__).with_name(file).open('r').read().splitlines()[0][1:-1])

def firstStar(input):
  return max(input.values())

def secondStar(input):
  return len([v for v in input.values() if v >= 1000])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3512

print("The second star is : {}".format(secondStar(input)))
# The second star is : 8660
