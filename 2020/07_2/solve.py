from pathlib import Path
import heapq

def readInput(file):
  result = dict()
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    color, content = line.split(' bags contain ')
    result[color] = set()
    if content != 'no other bags.':
      for item in content[:-1].split(', '):
        itemCount, itemColorShade, itemColor, _ = item.split(' ')
        itemCount = int(itemCount)
        itemColor = itemColorShade + ' ' + itemColor
        result[color].add((itemCount, itemColor))
  return result

def numBagsIn(color, input):
  result = 1
  for n, color in input[color]:
    result += n*numBagsIn(color, input)
  return result

def firstStar(input):
  colorSet = set()
  q = ['shiny gold']
  while q:
    currColor = heapq.heappop(q)
    for color in input:
      for content in input[color]:
        if content[1] == currColor:
          if color not in colorSet:
            heapq.heappush(q, color)
            colorSet.add(color)
  return len(colorSet)

def secondStar(input):
  return numBagsIn('shiny gold', input) - 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 355

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5312
