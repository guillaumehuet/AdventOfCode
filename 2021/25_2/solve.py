from pathlib import Path

direction = {'v' : (1, 0), '>' : (0, 1)}

def readInput(file):
  seaCucumbers = {'v': [], '>' : []}
  height = 0
  for l, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    width = len(line)
    height += 1
    for c, cell in enumerate(line):
      if cell in seaCucumbers:
        seaCucumbers[cell].append((l, c))
  return seaCucumbers, width, height

def step(seaCucumber, type, width, height):
  step = direction[type]
  result = dict()
  if type == '>':
    result['v'] = seaCucumber['v'].copy()
    result['>'] = []
  else:
    result['>'] = seaCucumber['>'].copy()
    result['v'] = []
  for i, s in enumerate(seaCucumber[type]):
    if ((s[0] + step[0]) % height, (s[1] + step[1]) % width) not in seaCucumber['>'] + seaCucumber['v']:
      result[type].append(((s[0] + step[0]) % height, (s[1] + step[1]) % width))
    else:
      result[type].append(s)
  return result

def printSeafloor(seaCucumber, width, height):
  for l in range(height):
    for c in range(width):
      if (l, c) in seaCucumber['>']:
        print('>', end='')
      elif (l, c) in seaCucumber['v']:
        print('v', end='')
      else:
        print('.', end='')
    print()


def firstStar(input):
  seaCucumber, width, height = input
  config = None
  newConfig = seaCucumber
  steps = 0
  while newConfig != config:
    config = newConfig
    newConfig = step(config, '>', width, height)
    newConfig = step(newConfig, 'v', width, height)
    steps += 1
  return steps

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 530
