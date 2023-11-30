def readInput(file):
  return tuple((line.split()[0], int(line.split()[1])) for line in open(file).read().splitlines())

def dirDecode(dir):
  if dir == 'L':
    return (-1, 0)
  if dir == 'R':
    return (1, 0)
  if dir == 'U':
    return (0, -1)
  if dir == 'D':
    return (0, 1)

def printRope(rope):
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0
  for x, y in rope:
    minX = min(x, minX)
    maxX = max(x, maxX)
    minY = min(y, minY)
    maxY = max(y, maxY)
  for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
      if (x, y) in rope:
        num = rope.index((x, y))
        if num == 0:
          num = 'H'
        print(num,end='')
      else:
        print('.',end='')
    print()
  print()

def firstStar(input):
  visited = set()
  head = (0, 0)
  tail = (0, 0)
  visited.add(tail)
  for curr in input:
    dir = curr[0]
    dir = dirDecode(dir)
    num = curr[1]
    for _ in range(num):
      newHead = (head[0] + dir[0], head[1] + dir[1])
      if abs(newHead[0] - tail[0]) > 1 or abs(newHead[1] - tail[1]) > 1:
        tail = head
      head = newHead
      visited.add(tail)
  return len(visited)

def secondStar(input):
  visited = set()
  knots = 10
  rope = [(0, 0) for _ in range(knots)]
  visited.add(rope[-1])
  for curr in input:
    dir = curr[0]
    dir = dirDecode(dir)
    num = curr[1]
    for _ in range(num):
      newRope = rope.copy()
      newRope[0] = (rope[0][0] + dir[0], rope[0][1] + dir[1])
      for k in range(1, knots):
        if abs(newRope[k - 1][0] - rope[k][0]) > 1 or abs(newRope[k - 1][1] - rope[k][1]) > 1:
          # The current know must move
          if (abs(newRope[k - 1][0] - rope[k - 1][0]) + abs(newRope[k - 1][1] - rope[k - 1][1])) > 1:
            # Special case : Diagonal movement of the previous knot
            diagDir = (newRope[k - 1][0] - rope[k - 1][0], newRope[k - 1][1] - rope[k - 1][1])
            if rope[k][0] == newRope[k - 1][0]:
              # Move only along y
              newRope[k] = (rope[k][0], rope[k][1] + diagDir[1])
            elif rope[k][1] == newRope[k - 1][1]:
              # Move only along x
              newRope[k] = (rope[k][0] + diagDir[0], rope[k][1])
            else:
              # Move along diagDir
              newRope[k] = (rope[k][0] + diagDir[0], rope[k][1] + diagDir[1])
          else:
            newRope[k] = rope[k - 1]
      rope = newRope
      visited.add(rope[-1])
  return len(visited)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 6311

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2482
