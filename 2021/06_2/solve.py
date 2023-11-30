from pathlib import Path

def readInput(file):
  return [int(n) for n in Path(__file__).with_name(file).open('r').read().splitlines()[0].split(',')]

def generations(input, n):
  count = [0]*9
  for fish in input:
    count[fish] += 1
  for _ in range(n):
    count = count[1:] + count[:1]
    count[6] += count[8]
  return sum(count)

def firstStar(input):
  return generations(input, 80)

def secondStar(input):
  return generations(input, 256)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 380758

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1710623015163
