def readInput(file):
  grids = []
  for line in open(file).read().splitlines():
    if ',' in line:
      order = tuple(int(n) for n in line.split(','))
    elif line:
      grids[-1].append(tuple(int(n) for n in line.split()))
    else:
      if len(grids):
        grids[-1] = tuple(grids[-1])
      grids.append([])
  grids[-1] = tuple(grids[-1])
  grids = tuple(grids)
  return order, grids

def firstStar(input):
  order, grids = input
  bingos = [[[False for _ in range(len(grids[0][0]))] for _ in range(len(grids[0]))] for _ in range(len(grids))]
  for n in order:
    for g, grid in enumerate(grids):
      for l, line in enumerate(grid):
        for c, number in enumerate(line):
          if number == n:
            bingos[g][l][c] = True
    for b, bingo in enumerate(bingos):
      for l, line in enumerate(bingo):
        if all(line):
          grid = grids[b]
          result = 0
          for l, line in enumerate(bingo):
            for c, state in enumerate(line):
              if not state:
                result += grid[l][c]
          return result*n
      for j in range(len(bingo[0])):
        if all(bingo[i][j] for i in range(len(bingo))):
          grid = grids[b]
          result = 0
          for l, line in enumerate(bingo):
            for c, state in enumerate(line):
              if not state:
                result += grid[l][c]
          return result*n
          
def secondStar(input):
  order, grids = input
  bingos = [[[False for _ in range(len(grids[0][0]))] for _ in range(len(grids[0]))] for _ in range(len(grids))]
  winners = set()
  for n in order:
    for g, grid in enumerate(grids):
      if g not in winners:
        for l, line in enumerate(grid):
          for c, number in enumerate(line):
            if number == n:
              bingos[g][l][c] = True
    for b, bingo in enumerate(bingos):
      if b not in winners:
        for l, line in enumerate(bingo):
          if all(line):
            winners.add(b)
            if len(winners) == len(grids):
              grid = grids[b]
              result = 0
              for l, line in enumerate(bingo):
                for c, state in enumerate(line):
                  if not state:
                    result += grid[l][c]
              return result*n
        for j in range(len(bingo[0])):
          if all(bingo[i][j] for i in range(len(bingo))):
            winners.add(b)
            if len(winners) == len(grids):
              grid = grids[b]
              result = 0
              for l, line in enumerate(bingo):
                for c, state in enumerate(line):
                  if not state:
                    result += grid[l][c]
              return result*n

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 10680

print("The second star is : {}".format(secondStar(input)))
# The second star is : 31892
