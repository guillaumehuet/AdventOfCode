from pathlib import Path

def readInput(file):
  list1 = []
  list2 = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)
  return list1, list2

def firstStar(input):
  list1, list2 = input
  return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

def secondStar(input):
  list1, list2 = input
  return sum(a * list2.count(a) for a in list1)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1660292

print("The second star is : {}".format(secondStar(input)))
# The second star is : 22776016
