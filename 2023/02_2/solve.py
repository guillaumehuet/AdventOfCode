from pathlib import Path

colorIndex = {'red' : 0, 'green' : 1, 'blue' : 2}

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    game, revealed = line.split(':')
    game = int(game.split()[1])
    reveals = []
    for reveal in revealed.split(';'):
      newReveal = [0, 0, 0]
      for colorDraw in reveal.split(','):
        count, color = colorDraw.split()
        newReveal[colorIndex[color]] = int(count)
      reveals.append(tuple(newReveal))
    result.append((game, tuple(reveals)))
  return tuple(result)

def firstStar(input):
  result = 0
  for game, reveals in input:
    possible = True
    for reveal in reveals:
      if reveal[0] > 12 or reveal[1] > 13 or reveal[2] > 14:
        possible = False
        break
    if possible:
      result += game
  return result

def secondStar(input):
  result = 0
  for game, reveals in input:
    maxRed, maxGreen, maxBlue = 0, 0, 0
    for reveal in reveals:
      maxRed = max(maxRed, reveal[0])
      maxGreen = max(maxGreen, reveal[1])
      maxBlue = max(maxBlue, reveal[2])
    result += maxRed*maxGreen*maxBlue
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2377

print("The second star is : {}".format(secondStar(input)))
# The second star is : 71220
