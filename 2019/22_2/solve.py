def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def readInput(file):
  shuffleSteps = []
  for line in open(file).read().splitlines():
    step = line.split()
    if step[0] == "cut":
      shuffleSteps.append(('c', int(step[1])))
    elif step[1] == "into":
      shuffleSteps.append(('r',))
    elif step[1] == "with":
      shuffleSteps.append(('i', int(step[-1])))
    else:
      return "Did not understand line :" + line
  return shuffleSteps

def process(shuffleSteps, deckSize = 10007):
  a = 1
  b = 0
  for step in shuffleSteps:
    if step[0] == 'r':
      a *= -1
      b *= -1
      b -= 1
    elif step[0] == 'c':
      b -= step[1]
    else:
      a *= step[1]
      b *= step[1]
  a %= deckSize
  b %= deckSize
  return a, b

def processIndex(shuffleSteps, deckSize = 119315717514047):
  a = 1
  b = 0
  for step in reversed(shuffleSteps):
    if step[0] == 'r':
      a *= -1
      b *= -1
      b -= 1
    elif step[0] == 'c':
      b += step[1]
    else:
      inv = modinv(step[1], deckSize)
      a *= inv
      b *= inv
  a %= deckSize
  b %= deckSize
  return a, b

def firstStar(input):
  deckSize = 10007
  searchedCard = 2019
  a, b = process(input, deckSize)
  return (a*searchedCard + b) % deckSize

def secondStar(input):
  deckSize = 119315717514047
  searchedIndex = 2020
  rounds = 101741582076661
  a, b = processIndex(input, deckSize)
  result = searchedIndex
  totalA = pow(a, rounds, deckSize)
  totalB = b * (totalA - 1) * modinv(a - 1, deckSize)
  return (totalA*result + totalB) % deckSize

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2519

print("The second star is : {}".format(secondStar(input)))
# The second star is : 58966729050483
