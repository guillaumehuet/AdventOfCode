from collections import deque

def readInput(file):
  return [int(c) for c in open(file).read().splitlines()[0].split() if c.isdigit()]

def firstStar(input):
  numPlayers = input[0]
  numMarbles = input[1]
  marbles = deque([0])
  scores = [0 for _ in range(numPlayers)]
  for i in range(1, numMarbles + 1):
    if i%23:
      marbles.rotate(-1)
      marbles.append(i)
    else:
      marbles.rotate(7)
      scores[i%numPlayers] += marbles.pop() + i
      marbles.rotate(-1)
  return max(scores)

def secondStar(input):
  newInput = [input[0], 100*input[1]]
  return firstStar(newInput)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 398371

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3212830280
