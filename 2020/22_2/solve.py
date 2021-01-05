from collections import deque
from itertools import islice

def readInput(file):
  deck1 = deque()
  deck2 = deque()
  currDeck = deck1
  for line in open(file).read().splitlines():
    if 'Player 2' in line:
      currDeck = deck2
    elif line.isnumeric():
      currDeck.append(int(line))
  return (deck1, deck2)

def round(deck1, deck2):
  p1 = deck1.popleft()
  p2 = deck2.popleft()
  winner = deck1 if p1 > p2 else deck2
  winner.append(max(p1, p2))
  winner.append(min(p1, p2))

def recursivePlay(deck1, deck2):
  seenConfigurations = set()
  while True:
    if (tuple(deck1), tuple(deck2)) in seenConfigurations:
      return 1
    else:
      seenConfigurations.add((tuple(deck1), tuple(deck2)))
      if len(deck1) > deck1[0] and len(deck2) > deck2[0]:
        # Recursive play
        p1 = deck1.popleft()
        p2 = deck2.popleft()
        winner = recursivePlay(deque(islice(deck1, 0, p1)), deque(islice(deck2, 0, p2)))
        if winner == 1:
          deck1.append(p1)
          deck1.append(p2)
        else:
          deck2.append(p2)
          deck2.append(p1)
      else:
        round(deck1, deck2)
        if len(deck1) == 0:
          return 2
        elif len(deck2) == 0:
          return 1

def score(deck):
  result = 0
  a = 1
  for card in reversed(deck):
    result += a*card
    a += 1
  return result

def firstStar(input):
  deck1 = input[0].copy()
  deck2 = input[1].copy()
  while (len(deck1) > 0 and len(deck2) > 0):
    round(deck1, deck2)
  return max(score(deck1), score(deck2))

def secondStar(input):
  deck1 = input[0].copy()
  deck2 = input[1].copy()
  winner = recursivePlay(deck1, deck2)
  return max(score(deck1), score(deck2))

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 32472

print("The second star is : {}".format(secondStar(input)))
# The second star is : 36463
