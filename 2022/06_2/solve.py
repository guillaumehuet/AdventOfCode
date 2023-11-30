def readInput(file):
  return open(file).read().splitlines()[0]

def firstStar(input):
  for i in range(len(input) - 3):
    curr = input[i:i+4]
    duplicate = False
    for j, c1 in enumerate(curr):
      for c2 in curr[j + 1:]:
        if c1 == c2:
          duplicate = True
          break
      if duplicate:
        break
    else:
      return i + 4

def secondStar(input):
  for i in range(len(input) - 13):
    curr = input[i:i+14]
    duplicate = False
    for j, c1 in enumerate(curr):
      for c2 in curr[j + 1:]:
        if c1 == c2:
          duplicate = True
          break
      if duplicate:
        break
    else:
      return i + 14

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1623

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3774
