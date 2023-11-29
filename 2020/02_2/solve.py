from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    repeats, letter, password = line.split()
    repeats = [int(n) for n in repeats.split('-')]
    letter = letter[0]
    result.append([repeats, letter, password])
  return result

def firstStar(input):
  result = 0
  for repeats, letter, password in input:
    if repeats[0] <= password.count(letter) <= repeats[1]:
      result += 1
  return result

def secondStar(input):
  result = 0
  for repeats, letter, password in input:
    if (password[repeats[0] - 1] == letter) ^ (password[repeats[1] - 1] == letter):
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 548

print("The second star is : {}".format(secondStar(input)))
# The second star is : 502
