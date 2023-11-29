from pathlib import Path

def readInput(file):
  return [int(line) for line in Path(__file__).with_name(file).open('r').read().splitlines()]

def firstStar(input):
  for i in range(len(input)):
    for j in range(i + 1, len(input)):
      if input[i] + input[j] == 2020:
        return input[i]*input[j]

def secondStar(input):
  for i in range(len(input)):
    for j in range(i + 1, len(input)):
      for k in range(j + 1, len(input)):
        if input[i] + input[j] + input[k] == 2020:
          return input[i]*input[j]*input[k]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1006176

print("The second star is : {}".format(secondStar(input)))
# The second star is : 199132160
