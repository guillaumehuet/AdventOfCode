from pathlib import Path

encodeVariables = {'x' : 0, 'm' : 1, 'a' : 2, 's' : 3}

def readInput(file):
  workflows = dict()
  parts = set()
  endOfWorkflows = False
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      endOfWorkflows = True
      continue
    if endOfWorkflows:
      currPart = []
      for stats in line[1:-1].split(','):
        currPart.append(int(stats.split('=')[1]))
      parts.add(tuple(currPart))
    else:
      currWorkFlow = []
      name, workflow = line.split('{')
      for rule in workflow[:-1].split(','):
        if ':' in rule:
          check, dest = rule.split(':')
          var = encodeVariables[check[0]]
          operator = check[1]
          value = int(check[2:])
          currWorkFlow.append(((var, operator, value), dest))
        else:
          currWorkFlow.append(rule)
      workflows[name] = tuple(currWorkFlow)
  return workflows, parts

def flow(part, workflow):
  for rule in workflow:
    if type(rule) is str:
      return rule
    var, operator, value = rule[0]
    if operator == '<':
      if part[var] < value:
        return rule[1]
    elif operator == '>':
      if part[var] > value:
        return rule[1]

def product(list):
  result = 1
  for elem in list:
    result *= elem
  return result

def countInBranch(conditions):
  minMax = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
  for rule in conditions:
    if rule[0] != 'not':
      var, operator, value = rule
      if operator == '>':
        minMax[var][0] = max(minMax[var][0], value + 1)
      elif operator == '<':
        minMax[var][1] = min(minMax[var][1], value - 1)
    else:
      var, operator, value = rule[1]
      if operator == '>': # <=
        minMax[var][1] = min(minMax[var][1], value)
      elif operator == '<': # >=
        minMax[var][0] = max(minMax[var][0], value)
  return product(var[1] - var[0] + 1 for var in minMax)

def branch(workflows, w = 'in', conditions = tuple()):
  newConditions = conditions
  for rule in workflows[w]:
    if type(rule) is str:
      if rule == 'R':
        pass
      elif rule == 'A':
        yield countInBranch(newConditions)
      else:
        yield from branch(workflows, rule, newConditions)
    else:
      currConditions = newConditions + (rule[0], )
      if rule[1] == 'R':
        pass
      elif rule[1] == 'A':
        yield countInBranch(currConditions)
      else:
        yield from branch(workflows, rule[1], currConditions)
      newConditions = newConditions + (('not', rule[0]), )

def sort(part, workflows):
  w = 'in'
  while w not in 'AR':
    w = flow(part, workflows[w])
  return w == 'A'

def firstStar(input):
  workflows, parts = input
  result = 0
  for part in parts:
    if sort(part, workflows):
      result += sum(part)
  return result

def secondStar(input):
  workflows = input[0]
  return sum(c for c in branch(workflows))

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 406934

print("The second star is : {}".format(secondStar(input)))
# The second star is : 131192538505367
