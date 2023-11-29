from pathlib import Path

def readInput(file):
  return [int(n) for n in Path(__file__).with_name(file).open('r').read().splitlines()[0].split('-')]

def hasDoubleDigits(digits):
  for d in range(len(digits) - 1):
    if digits[d] == digits[d + 1]:
      return True
  return False

def hasNoMoreThanDoubleDigits(digits):
  for d in range(len(digits) - 1):
    if digits[d] == digits[d + 1]:
      if (d == 0 or digits[d - 1] != digits[d]) and (d == len(digits) - 2 or digits[d + 2] != digits[d]):
        return True
  return False

def generateAll(min, max, discriminator):
  result = 0
  for d0 in range(0, 10):
    for d1 in range(d0, 10):
      for d2 in range(d1, 10):
        for d3 in range(d2, 10):
          for d4 in range(d3, 10):
            for d5 in range(d4, 10):
              n = 10*(10*(10*(10*(10*d0 + d1) + d2) + d3) + d4) + d5
              if n < min or n > max:
                continue
              if discriminator([d0, d1, d2, d3, d4, d5]):
                result += 1
  return result

def firstStar(input):
  return generateAll(input[0], input[1], hasDoubleDigits)

def secondStar(input):
  return generateAll(input[0], input[1], hasNoMoreThanDoubleDigits)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 475

print("The second star is : {}".format(secondStar(input)))
# The second star is : 297
