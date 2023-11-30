from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  commonBits = [0]*len(input[0])
  for line in input:
    for i, bit in enumerate(line):
      if bit == '1':
        commonBits[i] += 1
      else:
        commonBits[i] -= 1
  commonBits = [1 if b >= 0 else 0 for b in commonBits]
  gamma = sum(b*2**n for n, b in enumerate(reversed(commonBits)))
  epsilon = sum((1 - b)*2**n for n, b in enumerate(reversed(commonBits)))
  return gamma*epsilon

def rating(input, CO2 = False):
  input = input.copy()
  i = 0
  while len(input) > 1:
    commonBit = 0
    for line in input:
      if line[i] == '1':
        commonBit += 1
      else:
        commonBit -= 1
    if commonBit >= 0:
      commonBit = 1
    else:
      commonBit = 0
    if CO2:
      commonBit = 1 - commonBit
    commonBit = str(commonBit)
    input = [line for line in input if line[i] == commonBit]
    i += 1
  return input[0]


def secondStar(input):
  oxygen = rating(input)
  oxygen = sum(int(b)*2**n for n, b in enumerate(reversed(oxygen)))
  CO2 = rating(input, True)
  CO2 = sum(int(b)*2**n for n, b in enumerate(reversed(CO2)))
  return oxygen*CO2

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4160394

print("The second star is : {}".format(secondStar(input)))
# The second star is : 4125600
