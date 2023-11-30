def readInput(file):
  return tuple(int(line) for line in open(file).read().splitlines())

def firstStar(input):
  result = 0
  for i in range(len(input) - 1):
    if input[i + 1] > input[i]:
      result += 1
  return result

def secondStar(input):
  threeMeasurementWindow = []
  for i in range(len(input) -2):
    threeMeasurementWindow.append(input[i] + input[i + 1] + input[i + 2])
  result = 0
  for i in range(len(threeMeasurementWindow) - 1):
    if threeMeasurementWindow[i + 1] > threeMeasurementWindow[i]:
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1696

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1737
