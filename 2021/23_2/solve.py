from pathlib import Path
from bisect import insort

def readInput(file):
  result = [set(), set(), set(), set()]
  for j, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    for i, c in enumerate(line):
      if c in 'ABCD':
        result[ord(c) - ord('A')].add((i - 1, j - 1), )
  for i in range(len(result)):
    result[i] = frozenset(result[i])
  return tuple(result)

def readFoldedInput(file):
  result = [set(), set(), set(), set()]
  added = ["  #D#C#B#A#", "  #D#B#A#C#"]
  lines = Path(__file__).with_name(file).open('r').read().splitlines()
  lines = lines[:3] + added + lines[3:]
  for j, line in enumerate(lines):
    for i, c in enumerate(line):
      if c in 'ABCD':
        result[ord(c) - ord('A')].add((i - 1, j - 1), )
  for i in range(len(result)):
    result[i] = frozenset(result[i])
  return tuple(result)

def heuristic(position, roomDepth = 2):
  result = 0
  for c, pos in enumerate(position):
    targetRoom = 2*c + 2
    for p in pos:
      if p[1] == 0 or p[0] != targetRoom:
        result += (abs(p[0] - targetRoom) + 1 + p[1])*10**c
      else:
        needToMove = False
        moveDistance = 1
        for d in range(roomDepth, p[1], -1):
          if (targetRoom, d) not in pos:
            needToMove = True
          elif needToMove:
            moveDistance += 1
        if needToMove:
          result += 2*(p[1] + moveDistance)*10**c
    for d in range(roomDepth, 1, -1):
      if (targetRoom, d) not in pos:
        result += (d-1)*10**c
  return result

def neighboors(state, roomDepth = 2):
  energy, position = state[2:]
  result = []
  obstacles = frozenset(item for sublist in position for item in sublist)
  for c, pos in enumerate(position):
    targetRoom = 2*c + 2
    for p in pos:
      if p[1] == 0:
        canStack = True
        for d in range(roomDepth, 0, -1):
          if (targetRoom, d) not in obstacles:
            break
          if (targetRoom, d) not in pos:
            canStack = False
            break
        if canStack:
          minCheck = min(p[0] + 1, targetRoom)
          maxCheck = max(p[0] - 1, targetRoom) + 1
          for i in range(minCheck, maxCheck):
            if (i, 0) in obstacles:
              break
          else:
            newEnergy = energy + (abs(p[0] - targetRoom) + d + p[1])*10**c
            newPosition = position[:c] + (pos - {p} | {(targetRoom, d)}, ) + position[c + 1:]
            newHeuristic = heuristic(newPosition, roomDepth)
            result.append((newEnergy + newHeuristic, newHeuristic, newEnergy, newPosition))
      else:
        needToMove = True
        if p[0] == targetRoom:
          needToMove = False
          for d in range(roomDepth, p[1], -1):
            if (targetRoom, d) not in pos:
              needToMove = True
              break
        if needToMove:
          for d in range(p[1] - 1, -1, -1):
            if (p[0], d) in obstacles:
              break
          else:
            minCheck = p[0]
            while (minCheck, 0) not in obstacles and minCheck >= 0:
              minCheck -= 1
            maxCheck = p[0]
            while (maxCheck, 0) not in obstacles and maxCheck <= 10:
              maxCheck += 1
            for x in range(minCheck + 1, maxCheck):
              if x not in (2, 4, 6, 8):
                newEnergy = energy + (abs(p[0] - x) + p[1])*10**c
                newPosition = position[:c] + (pos - {p} | {(x, 0)}, ) + position[c + 1:]
                newHeuristic = heuristic(newPosition, roomDepth)
                result.append((newEnergy + newHeuristic, newHeuristic, newEnergy, newPosition))
  return result

def firstStar(input):
  boundary = [(heuristic(input), heuristic(input), 0, input)]
  visited = set()
  while boundary:
    state = boundary.pop(0)
    visited.add(state[3])
    for n in neighboors(state):
      if n[1] == 0:
        return n[0]
      if n[3] not in visited:
        insort(boundary, n)
        visited.add(n[3])

def secondStar(foldedInput):
  boundary = [(heuristic(foldedInput, 4), heuristic(foldedInput, 4), 0, foldedInput)]
  visited = set()
  while boundary:
    state = boundary.pop(0)
    visited.add(state[3])
    for n in neighboors(state, 4):
      if n[1] == 0:
        return n[0]
      if n[3] not in visited:
        insort(boundary, n)
        visited.add(n[3])

input = readInput('input')
foldedInput = readFoldedInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 11536

print("The second star is : {}".format(secondStar(foldedInput)))
# The second star is : 55136
