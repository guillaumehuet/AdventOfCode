from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()[0].split(',')

def HASH(string):
  result = 0
  for c in string:
    result += ord(c)
    result *= 17
    result %= 256
  return result

def firstStar(input):
  result = 0
  for string in input:
    result += HASH(string)
  return result

def secondStar(input):
  boxes = [[] for _ in range(256)]
  for instruction in input:
    if instruction[-1] == '-':
      lens = instruction[:-1]
      box = HASH(lens)
      for l in boxes[box]:
        if l[0] == lens:
          boxes[box].remove(l)
          break
    else:
      lens, focal = instruction.split('=')
      box = HASH(lens)
      inserted = False
      for i, l in enumerate(boxes[box]):
        if l[0] == lens:
          boxes[box][i] = (lens, int(focal))
          inserted = True
          break
      if not inserted:
        boxes[box].append((lens, int(focal)))
  result = 0
  for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
      result += (i + 1)*(j + 1)*(lens[1])
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 515974

print("The second star is : {}".format(secondStar(input)))
# The second star is : 265894
