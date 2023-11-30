def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    line = line.split()
    if line[0] == "turn":
      line = line[1:]
    action = line[0]
    start = tuple(int(n) for n in line[1].split(','))
    end = tuple(int(n) for n in line[3].split(','))
    result.append((action, start, end))
  return tuple(result)

def firstStar(input):
  grid = [[False for _ in range(1000)] for _ in range(1000)]
  for line in input:
    for i in range(line[1][0], line[2][0] + 1):
      for j in range(line[1][1], line[2][1] + 1):
        if line[0] == "off":
          grid[j][i] = False
        elif line[0] == "on":
          grid[j][i] = True
        else:
          grid[j][i] = not grid[j][i]
  return sum(sum(line) for line in grid)

def secondStar(input):
  grid = [[0 for _ in range(1000)] for _ in range(1000)]
  for line in input:
    for i in range(line[1][0], line[2][0] + 1):
      for j in range(line[1][1], line[2][1] + 1):
        if line[0] == "off":
          if grid[j][i] > 0:
            grid[j][i] -= 1
        elif line[0] == "on":
          grid[j][i] += 1
        else:
          grid[j][i] += 2
  return sum(sum(line) for line in grid)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 400410

print("The second star is : {}".format(secondStar(input)))
# The second star is : 15343601
