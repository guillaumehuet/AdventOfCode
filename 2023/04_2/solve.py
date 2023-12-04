from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append([])
    winning, have = line.split(':')[1].split('|')
    result[-1].append(tuple(int(n) for n in winning.split()))
    result[-1].append(tuple(int(n) for n in have.split()))
    result[-1] = tuple(result[-1])
  return tuple(result)

def winningNumbers(ticket):
  winning, have = ticket
  result = 0
  for n in have:
    if n in winning:
      result += 1
  return result

def firstStar(input):
  result = 0
  for ticket in input:
    wins = winningNumbers(ticket)
    if wins > 0:
      result += 2**(wins-1)
  return result

def secondStar(input):
  result = 0
  ticketsWin = []
  for ticket in input[::-1]:
    wins = winningNumbers(ticket)
    added = 1 + sum(ticketsWin[-i] for i in range(1, wins + 1))
    result += added
    ticketsWin.append(added)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 22674

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5747443
