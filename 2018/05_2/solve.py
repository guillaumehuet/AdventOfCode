def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  polymer = list(input[0])
  reactive = True
  while reactive:
    reactive, polymer = react(polymer)
  return len(polymer)
  

def react(polymer):
  for i in range(len(polymer) - 1):
    if polymer[i] != polymer[i + 1] and polymer[i].lower() == polymer[i + 1].lower():
      return True, polymer[:i] + polymer[i + 2:]
  return False, polymer

def secondStar(input):
  shortest = len(input[0])
  for c in (chr(i + ord('a')) for i in range(26)):
    smallerInput = list(input[0])
    lowercase = c
    uppercase = chr(ord(c) - ord('a') + ord('A'))
    while lowercase in smallerInput:
      smallerInput.remove(lowercase)
    while uppercase in smallerInput:
      smallerInput.remove(uppercase)
    length = firstStar(["".join(smallerInput)])
    if length < shortest:
      shortest = length
  return shortest

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 10496

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5774
