def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    first, second = line.split(',')
    first = tuple(int(i) for i in first.split('-'))
    second = tuple(int(i) for i in second.split('-'))
    result.append((first, second))
  return tuple(result)

def firstStar(input):
  result = 0
  for first, second in input:
    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
      result += 1
  return result

def secondStar(input):
  result = 0
  for first, second in input:
    if not ((first[1] < second[0]) or (second[1] < first[0])):
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 483

print("The second star is : {}".format(secondStar(input)))
# The second star is : 874
