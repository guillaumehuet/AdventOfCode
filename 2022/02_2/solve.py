from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    opp, strat = line.split()
    opp = ord(opp) - ord('A') + 1
    strat = ord(strat) - ord('X') + 1
    result.append((opp, strat))
  return result

def firstStar(input):
  score = 0
  for opp, strat in input:
    # `win` is 0 for lost, 1 for draw, 2 for win
    win = ((strat - opp + 1) % 3)
    score += 3*win + strat
  return score

def secondStar(input):
  score = 0
  for opp, win in input:
    win -= 1
    # `win` is 0 for lost, 1 for draw, 2 for win
    strat = ((opp + win - 2) % 3) + 1
    score += 3*win + strat
  return score

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 11603

print("The second star is : {}".format(secondStar(input)))
# The second star is : 12725
