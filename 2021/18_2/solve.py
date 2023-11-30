from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def format(number):
  result = []
  isNumber = False
  n = 0
  for c in number:
    if c in '[]':
      if isNumber:
        result.append(n)
        isNumber = False
        n = 0
      result.append(c)
    elif c == ',':
      if isNumber:
        result.append(n)
        isNumber = False
        n = 0
    elif c.isdigit():
      n *= 10
      n += int(c)
      isNumber = True
  return result

def prettyPrint(number):
  prev = '['
  for n in number:
    if n != ']' and prev != '[':
      print(',', end='')
    prev = n
    print(n, end='')
  print()
  
def addSNum(left, right):
  return ['['] + left + right + [']']

def split(number, index):
  n = number[index]
  left = n //2
  right = n - left
  number = number[:index] + ['[', left, right, ']'] + number[index+1:]
  return number

def explode(number, index):
  leftValue = number[index + 1]
  righttValue = number[index + 2]
  previousIndex = index - 1
  nextIndex = index + 3
  while previousIndex > 0 and type(number[previousIndex]) is not int:
    previousIndex -= 1
  while nextIndex < len(number) and type(number[nextIndex]) is not int:
    nextIndex += 1
  if previousIndex > 0:
    previousValue = number[previousIndex]
    number = number[:previousIndex] + [leftValue + previousValue] + number[previousIndex + 1:]
  if nextIndex < len(number):
    nextValue = number[nextIndex]
    number = number[:nextIndex] + [righttValue + nextValue] + number[nextIndex + 1:]
  number = number[:index] + [0] + number[index + 4:]
  return number

def reduce(number):
  nest = 0
  for i, c in enumerate(number):
    if c == '[':
      nest += 1
      if nest > 4:
        number = explode(number, i)
        return reduce(number)
    elif c == ']':
      nest -= 1
  for i, c in enumerate(number):
    if type(c) is int:
      if c >= 10:
        number = split(number, i)
        return reduce(number)
  return number

def magnitude(number):
  if len(number) == 1:
    return number[0]
  depth = 0
  limits = []
  for i, c in enumerate(number):
    if c == '[':
      depth += 1
    elif c == ']':
      depth -= 1
    if depth == 1:
      limits.append(i)
  left = number[limits[0] + 1:limits[1] + 1]
  right = number[limits[1] + 1:limits[2] + 1]
  return 3*magnitude(left) + 2*magnitude(right)

def firstStar(input):
  result = format(input[0])
  for n in input[1:]:
    n = format(n)
    result = addSNum(result, n)
    result = reduce(result)
  return magnitude(result)

def secondStar(input):
  maxMag = 0
  for i in range(len(input)):
    for j in range(len(input)):
      if i != j:
        a = format(input[i])
        b = format(input[j])
        result = addSNum(a, b)
        result = reduce(result)
        maxMag = max(maxMag, magnitude(result))
  return maxMag

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 4235

print("The second star is : {}".format(secondStar(input)))
# The second star is : 4659
