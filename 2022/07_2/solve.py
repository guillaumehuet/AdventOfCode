def readInput(file):
  return open(file).read().splitlines()

def inputToTree(input):
  tree = dict()
  cwd = tree
  path = []
  inLs = False
  for line in input:
    command = line.split()
    if command[0] == "$":
      inLs = False
      if command[1] == "cd":
        if command[2] == "/":
          cwd = tree
          path = []
        elif command[2] == "..":
          path.pop()
          cwd = tree
          for dir in path:
            cwd = cwd[dir]
        else:
          dir = command[2]
          path.append(dir)
          cwd = cwd[dir]
      elif command[1] == "ls":
        inLs = True
    else:
      if inLs:
        size, file = line.split()
        if size == "dir":
          cwd[file] = dict()
        else:
          cwd[file] = int(size)
  return tree

def sizeDir(tree):
  result = 0
  subdir = []
  for file in tree.values():
    if type(file) is dict:
      size, subsubdir = sizeDir(file)
      result += size
      subdir += subsubdir
    else:
      result += file
  subdir.append(result)
  return result, subdir

def firstStar(input):
  tree = inputToTree(input)
  result = 0
  for size in sizeDir(tree)[1]:
    if size <= 100_000:
      result += size
  return result

def secondStar(input):
  tree = inputToTree(input)
  result = 0
  sizes = sizeDir(tree)[1]
  sizes.sort()
  total = sizes[-1]
  needed = 30_000_000 - (70_000_000 - total)
  for size in sizes:
    if size > needed:
      return size

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1555642

print("The second star is : {}".format(secondStar(input)))
# The second star is : 5974547
