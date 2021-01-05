def readInput(file):
  return sorted([int(n) for n in open(file).read().splitlines()])

def firstStar(input):
  diff1 = 0
  diff3 = 0
  prev = 0
  for curr in input:
    diff = curr - prev
    if diff == 1:
      diff1 += 1
    elif diff == 3:
      diff3 += 1
    prev = curr
  diff3 += 1
  return diff1*diff3

def secondStar(input):
  adapters = list(reversed(input)) + [0]
  chainCount = {max(adapters) + 3 : 1}
  for curr in adapters:
    count = 0
    for i in range(1, 4):
      if curr + i in chainCount:
        count += chainCount[curr + i]
    chainCount[curr] = count
  return chainCount[0]


input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1836

print("The second star is : {}".format(secondStar(input)))
# The second star is : 43406276662336
