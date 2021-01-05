def readInput(file):
  return open(file).read().splitlines()

def calculate(line):
  result = 0
  op = '+'
  i = 0
  length = len(line)
  while i < length:
    c = line[i]
    if c.isnumeric():
      if op == '+':
        result += int(c)
      else:
        result *= int(c)
    elif c in '+*':
      op = c
    elif c == '(':
      parentheseCount = 1
      for j in range(i + 1, len(line)):
        if line[j] == '(':
          parentheseCount += 1
        elif line[j] == ')':
          parentheseCount -= 1
        if parentheseCount == 0:
          if op == '+':
            result += calculate(line[i + 1:j])
          else:
            result *= calculate(line[i + 1:j])
          i = j
          break
    i += 1
  return result

def calculateWithAdditionPrecedence(line):
  partialResult = 0
  multiplications = []
  op = '+'
  i = 0
  length = len(line)
  while i < length:
    c = line[i]
    if c.isnumeric():
      if op == '+':
        partialResult += int(c)
      else:
        multiplications.append(partialResult)
        partialResult = int(c)
    elif c in '+*':
      op = c
    elif c == '(':
      parentheseCount = 1
      for j in range(i + 1, len(line)):
        if line[j] == '(':
          parentheseCount += 1
        elif line[j] == ')':
          parentheseCount -= 1
        if parentheseCount == 0:
          if op == '+':
            partialResult += calculateWithAdditionPrecedence(line[i + 1:j])
          else:
            multiplications.append(partialResult)
            partialResult = calculateWithAdditionPrecedence(line[i + 1:j])
          i = j
          break
    i += 1
  
  multiplications.append(partialResult)
  result = 1
  for n in multiplications:
    result *= n
  return result

def firstStar(input):
  result = 0
  for line in input:
    result += calculate(line)
  return result

def secondStar(input):
  result = 0
  for line in input:
    result += calculateWithAdditionPrecedence(line)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1402255785165

print("The second star is : {}".format(secondStar(input)))
# The second star is : 119224703255966
