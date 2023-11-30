from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    digits, displays = line.split(' | ')
    digits = tuple(digits.split(' '))
    displays = tuple(displays.split(' '))
    result.append((digits, displays))
  return tuple(result)

def firstStar(input):
  result = 0
  for line in input:
    for display in line[1]:
      if len(display) in (2, 3, 4, 7):
        result += 1
  return result

def decode(digits):
  total = "".join(digits)
  result = {c: total.count(c) for c in 'abcdefg'}
  for d in digits:
    if len(d) == 2:
      one = d
    elif len(d) == 4:
      four = d
  for k in result:
    v = result[k]
    if v == 4:
      v = 'e'
    elif v == 6:
      v = 'b'
    elif v == 7:
      if k in four:
        v = 'd'
      else:
        v = 'g'
    elif v == 8:
      if k in one:
        v = 'c'
      else:
        v = 'a'
    else:
      v = 'f'
    result[k] = v
  return result

def toDigits(displays, code):
  result = 0
  for d in displays:
    result *= 10
    if len(d) == 2:
      result += 1
    elif len(d) == 3:
      result += 7
    elif len(d) == 4:
      result += 4
    elif len(d) == 5:
      for c in d:
        if code[c] == 'e':
          result += 2
          break
        elif code[c] == 'b':
          result += 5
          break
      else:
        result += 3
    elif len(d) == 6:
      for c in d:
        if code[c] == 'd':
          for c in d:
            if code[c] == 'e':
              result += 6
              break
          else:
            result += 9
          break
    elif len(d) == 7:
      result += 8
  return result


def secondStar(input):
  result = 0
  for digits, displays in input:
    code = decode(digits)
    display = toDigits(displays, code)
    result += display
  return result


input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 381

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1023686
