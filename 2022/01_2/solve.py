from pathlib import Path

def readInput(file):
  result = [[]]
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if line == '':
      result.append([])
    else:
      result[-1].append(int(line))
  return result


def firstStar(input):
  result = 0
  for elf in input:
    calories = sum(elf)
    result = max(result, calories)
  return result

def secondStar(input):
  calories = []
  for elf in input:
    calories.append(sum(elf))
  calories.sort(reverse=True)
  return sum(calories[:3])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 69177

print("The second star is : {}".format(secondStar(input)))
# The second star is : 207456
