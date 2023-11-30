from pathlib import Path

def readInput(file):
  result = dict()
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    operation, variable = line.split(' -> ')
    if operation.isnumeric():
      result[variable] = int(operation)
    else:
      operands = operation.split(' ')
      for i, v in enumerate(operands):
        if v.isnumeric():
          operands[i] = int(v)
      result[variable] = tuple(operands)
  return result

def compute(gates, bvalue = None):
  gates = gates.copy()
  if bvalue:
    gates['b'] = bvalue
  knownvalues = dict()
  while 'a' not in knownvalues:
    for g in gates:
      if g not in knownvalues:
        v = gates[g]
        if type(v) is int:
          knownvalues[g] = v
        elif len(v) == 1:
          v0 = v[0]
          if v0 in knownvalues:
            knownvalues[g] = knownvalues[v[0]]
        elif v[0] == 'NOT':
          v1 = False
          if type(v[1]) is int:
            v1 = v[1]
          elif v[1] in knownvalues:
            v1 = knownvalues[v[1]]
          if type(v1) is int:
            knownvalues[g] = (~v1 & 0xFFFF)
        else:
          operator = v[1]
          v0 = False
          if type(v[0]) is int:
            v0 = v[0]
          elif v[0] in knownvalues:
            v0 = knownvalues[v[0]]
          v2 = False
          if type(v[2]) is int:
            v2 = v[2]
          elif v[2] in knownvalues:
            v2 = knownvalues[v[2]]
          if type(v0) is int and type(v2) is int:
            if operator == 'AND':
              knownvalues[g] = v0 & v2
            elif operator == 'OR':
              knownvalues[g] = v0 | v2
            elif operator == 'LSHIFT':
              knownvalues[g] = v0 << v2
            elif operator == 'RSHIFT':
              knownvalues[g] = v0 >> v2
  return knownvalues['a']



def firstStar(input):
  return compute(input)

def secondStar(input):
  bvalue = compute(input)
  return compute(input, bvalue)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3176

print("The second star is : {}".format(secondStar(input)))
# The second star is : 14710
