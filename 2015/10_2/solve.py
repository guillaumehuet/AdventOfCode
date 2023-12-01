from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()[0]

def step(line):
  result = ""
  index = 0
  while index < len(line):
    char = line[index]
    count = 1
    while index + 1 < len(line) and line[index + 1] == char:
      index += 1
      count += 1
    result += str(count) + char
    index += 1
  return result

def firstStar(input):
  result = input
  for _ in range(40):
    result = step(result)
  return len(result)

def secondStar(input):
  result = input
  for _ in range(50):
    result = step(result)
  return len(result)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 329356

print("The second star is : {}".format(secondStar(input)))
# The second star is : 4666278
