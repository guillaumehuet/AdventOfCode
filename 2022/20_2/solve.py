from pathlib import Path

def readInput(file):
  return tuple((i, int(line)) for i, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()))

def firstStar(input):
  inputList = list(input)
  size = len(input)
  for elem in input:
    index = inputList.index(elem)
    newIndex = (index + elem[1]) % (size - 1)
    del inputList[index]
    inputList.insert(newIndex, elem)
  for i, elem in enumerate(inputList):
    if elem[1] == 0:
      indexOfZero = i
      break
  result = 0
  for n in (1000, 2000, 3000):
    result += inputList[(n + indexOfZero) % size][1]
  return result

def secondStar(input):
  decryptionKey = 811589153
  decryptedInput = tuple((e[0], e[1]*decryptionKey) for e in input)
  inputList = list(decryptedInput)
  size = len(decryptedInput)
  for _ in range(10):
    for elem in decryptedInput:
      index = inputList.index(elem)
      newIndex = (index + elem[1]) % (size - 1)
      del inputList[index]
      inputList.insert(newIndex, elem)
    for i, elem in enumerate(inputList):
      if elem[1] == 0:
        indexOfZero = i
        break
  result = 0
  for n in (1000, 2000, 3000):
    result += inputList[(n + indexOfZero) % size][1]
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 988

print("The second star is : {}".format(secondStar(input)))
# The second star is : 7768531372516
