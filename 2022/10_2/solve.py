def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  result = 0
  cycle = 0
  nextCheck = 20
  x = 1
  for line in input:
    op = line.split()
    if op[0] == 'noop':
      cycle += 1
      if cycle >= nextCheck:
        result += nextCheck*x
        nextCheck += 40
    elif op[0] == 'addx':
      cycle += 2
      if cycle >= nextCheck:
        result += nextCheck*x
        nextCheck += 40
      x += int(op[1])
  return result

def secondStar(input):
  result = '\n'
  cycle = 0
  x = 1
  beamX = 0
  for line in input:
    op = line.split()
    if op[0] == 'noop':
      cycle += 1
      if x - 1 <= beamX <= x + 1:
        result += '#'
      else:
        result += '.'
      beamX += 1
      if beamX >= 40:
        result += '\n'
        beamX = 0
    elif op[0] == 'addx':
      cycle += 2
      if x - 1 <= beamX <= x + 1:
        result += '#'
      else:
        result += '.'
      beamX += 1
      if beamX >= 40:
        result += '\n'
        beamX = 0
      if x - 1 <= beamX <= x + 1:
        result += '#'
      else:
        result += '.'
      beamX += 1
      if beamX >= 40:
        result += '\n'
        beamX = 0
      x += int(op[1])
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 14340

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
###...##..###....##..##..###..#..#.###..
#..#.#..#.#..#....#.#..#.#..#.#..#.#..#.
#..#.#..#.#..#....#.#....###..####.#..#.
###..####.###.....#.#....#..#.#..#.###..
#....#..#.#....#..#.#..#.#..#.#..#.#....
#....#..#.#.....##...##..###..#..#.#....
