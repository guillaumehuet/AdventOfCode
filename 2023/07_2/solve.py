from pathlib import Path
from bisect import insort

def readInput(file):
  result = []
  cardsValues = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    hand, bid = line.split()
    numericalHand = []
    for card in hand:
      if card.isdigit():
        numericalHand.append(int(card))
      else:
        numericalHand.append(cardsValues[card])
    bid = int(bid)
    result.append((tuple(numericalHand), bid))
  return tuple(result)

def replaceJacksWithJokers(hands):
  result = []
  for hand in hands:
    newHand = []
    for card in hand[0]:
      if card != 11:
        newHand.append(card)
      else:
        newHand.append(1)
    result.append((tuple(newHand), hand[1]))
  return tuple(result)

def highestCardCount(hand):
  if len(hand) == 0:
    return 0, 0
  sortedHand = sorted(hand)
  bestCard = sortedHand[0]
  bestCount = 1
  currCard = sortedHand[0]
  count = 1
  for card in sortedHand[1:]:
    if card == currCard:
      count += 1
    else:
      currCard = card
      count = 1
    if count > bestCount:
      bestCount = count
      bestCard = card
  return bestCount, bestCard

def highestCardCountExludingJokers(hand):
  bestCount, bestCard = highestCardCount([card for card in hand if card != 1])
  return bestCount, bestCard

def highestCardCountIncludingJokers(hand):
  jokerCount = hand.count(1)
  bestCount, bestCard = highestCardCountExludingJokers(hand)
  bestCount += jokerCount
  return bestCount, bestCard

def score(hands):
  types = [[], [], [], [], [], [], []]
  for hand in hands:
    bestCount, bestCard = highestCardCountIncludingJokers(hand[0])
    if bestCount == 5:
      insort(types[6], hand)
    elif bestCount == 4:
      insort(types[5], hand)
    elif bestCount == 3:
      secondCount, _ = highestCardCountExludingJokers([card for card in hand[0] if card != bestCard])
      if secondCount == 2:
        insort(types[4], hand)
      else:
        insort(types[3], hand)
    elif bestCount == 2:
      secondCount, _ = highestCardCountExludingJokers([card for card in hand[0] if card != bestCard])
      if secondCount == 2:
        insort(types[2], hand)
      else:
        insort(types[1], hand)
    else:
      insort(types[0], hand)
  types = [hand for t in types for hand in t]
  result = 0
  for rank, hand in enumerate(types):
    result += (rank + 1)*hand[1]
  return result

def firstStar(input):
  return score(input)

def secondStar(input):
  hands = replaceJacksWithJokers(input)
  return score(hands)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 252656917

print("The second star is : {}".format(secondStar(input)))
# The second star is : 253499763
