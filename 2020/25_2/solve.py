from pathlib import Path

def readInput(file):
  return [int(line) for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def findHandshake(cardTarget, doorTarget):
  targetRounds = 0
  rounds = 0
  subject = 7
  value = 1
  while targetRounds == 0:
    rounds += 1
    value *= subject
    value %= 20201227
    if value == cardTarget:
      targetRounds = rounds
      subject = doorTarget
      break
    if value == doorTarget:
      targetRounds = rounds
      subject = cardTarget
      break
  value = 1
  for rounds in range(targetRounds):
    value *= subject
    value %= 20201227
  return value

def firstStar(input):
  return findHandshake(input[0], input[1])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1890859
