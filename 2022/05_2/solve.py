def readInput(file):
  header = []
  procedure = []
  inProcedures = False
  for line in open(file).read().splitlines():
    if not inProcedures:
      if line:
        header.append(line)
      else:
        nStacks = int(header[-1].split()[-1])
        header = list(reversed(header[:-1]))
        stacks = [[] for _ in range(nStacks)]
        for row in header:
          for stack in range(nStacks):
            crate = row[4*stack + 1]
            if crate.isupper():
              stacks[stack].append(crate)
        for stack in range(nStacks):
          stacks[stack] = tuple(stacks[stack])
        stacks = tuple(stacks)
        inProcedures = True
    else:
      line = line.split()
      number = int(line[1])
      fromStack = int(line[3])
      toStack = int(line[5])
      procedure.append((number, fromStack, toStack))
  procedure = tuple(procedure)
  return stacks, procedure

def firstStar(input):
  stacks = list(input[0])
  procedure = input[1]
  nStacks = len(stacks)
  for stack in range(nStacks):
    stacks[stack] = list(stacks[stack])
  for p in procedure:
    for _ in range(p[0]):
      stacks[p[2] - 1].append(stacks[p[1] - 1][-1])
      del(stacks[p[1] - 1][-1])
  result = ""
  for stack in stacks:
    result += stack[-1]
  return result

def secondStar(input):
  stacks = list(input[0])
  procedure = input[1]
  nStacks = len(stacks)
  for stack in range(nStacks):
    stacks[stack] = list(stacks[stack])
  for p in procedure:
    stacks[p[2] - 1] += stacks[p[1] - 1][-p[0]:]
    del(stacks[p[1] - 1][-p[0]:])
  result = ""
  for stack in stacks:
    result += stack[-1]
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : VRWBSFZWM

print("The second star is : {}".format(secondStar(input)))
# The second star is : RBTWJWMCF
