from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()[0]

def firstRule(password):
  for index in range(len(password) - 2):
    if ord(password[index + 1]) - ord(password[index]) == 1 and ord(password[index + 2]) - ord(password[index + 1]) == 1:
      return True
  return False

def secondRule(password):
  return not ("i" in password or "o" in password or "l" in password)

def thirdRule(password):
  foundPairs = 0
  index = 0
  while index < len(password) - 1:
    if password[index + 1] == password[index]:
      foundPairs += 1
      index += 1
      if foundPairs == 2:
        return True
    index += 1
  return False

def step(password):
  if password[-1] != 'z':
    return password[:-1] + chr(ord(password[-1]) + 1)
  else:
    return step(password[:-1]) + 'a'

def firstStar(input):
  password = input
  while not (firstRule(password) and secondRule(password) and thirdRule(password)):
    password = step(password)
  return password

def secondStar(input):
  password = step(firstStar(input))
  while not (firstRule(password) and secondRule(password) and thirdRule(password)):
    password = step(password)
  return password

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : cqjxxyzz

print("The second star is : {}".format(secondStar(input)))
# The second star is : cqkaabcc
