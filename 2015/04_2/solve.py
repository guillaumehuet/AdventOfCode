from hashlib import md5

def readInput(file):
  return open(file).read().splitlines()[0]

def findHashWithNZeroes(key, n):
  i = 0
  md5hash = md5((key + str(i)).encode()).hexdigest()
  while md5hash[:n] != '0'*n:
    i += 1
    md5hash = md5((key + str(i)).encode()).hexdigest()
  return i

def firstStar(input):
  return findHashWithNZeroes(input, 5)

def secondStar(input):
  return findHashWithNZeroes(input, 6)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 254575

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1038736
