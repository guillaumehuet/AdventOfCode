from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

snafuDigits = {'=' : -2, '-' : -1, '0' : 0, '1' : 1, '2' : 2}

def snafuToDecimal(snafu):
  result = 0
  for c in snafu:
    result *= 5
    result += snafuDigits[c]
  return result

def decimalToSnafu(decimal):
  inverseSnafuDigits = {v: k for k, v in snafuDigits.items()}
  result = ''
  while decimal:
    rem = decimal % 5
    if rem > 2:
      rem -= 5
    result = inverseSnafuDigits[rem] + result
    decimal -= rem
    decimal //= 5
  return result

def firstStar(input):
  result = 0
  for snafu in input:
    result += snafuToDecimal(snafu)
  return decimalToSnafu(result)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2==0=0===02--210---1
