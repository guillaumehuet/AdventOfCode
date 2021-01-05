from itertools import cycle

def readInput(file):
  return [int(n) for n in open(file).read().splitlines()]

def firstStar(input):
  return sum(input)

def secondStar(input):
  freqs = {0}
  freq = 0

  for f in cycle(input):
    freq += f
    if freq in freqs:
      return freq
    freqs.add(freq)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 425

print("The second star is : {}".format(secondStar(input)))
# The second star is : 57538
