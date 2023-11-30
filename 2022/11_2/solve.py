from pathlib import Path
from copy import deepcopy
from math import lcm

def operation(old, operator, operand):
  if operator == '+':
    return old + operand
  elif operator == '*':
    return old * operand
  else:
    raise Exception('Unknown operation :', operator)

def readInput(file):
  input = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if not line:
      continue
    key, value = line.split(':')
    key = key.strip()
    key = key.split(' ')
    if key[0] == 'Monkey':
      input.append(dict())
    elif key[0] == 'Starting':
      items = [int(item) for item in value.split(',')]
      input[-1]['items'] = items
    elif key[0] == 'Operation':
      operation = value.split()
      input[-1]['operation'] = (operation[-2], operation[-1])
    elif key[0] == 'Test':
      input[-1]['test'] = int(value.split()[-1])
    elif key[0] == 'If':
      if key[1] == 'true':
        input[-1]['throwTrue'] = int(value.split()[-1])
      elif key[1] == 'false':
        input[-1]['throwFalse'] = int(value.split()[-1])
      else:
        raise Exception('Unknown key :', key)
    else:
      raise Exception('Unknown key :', key)
  return input

def firstStar(input):
  inspections = [0] * len(input)
  monkeys = deepcopy(input)
  for round in range(20):
    for i, monkey in enumerate(monkeys):
      for item in monkey['items']:
        inspections[i] += 1
        operator, operand = monkey['operation']
        if operand == 'old':
          value = operation(item, operator, item)
        else:
          value = operation(item, operator, int(operand))
        value = value // 3
        if value % monkey['test']:
          monkeys[monkey['throwFalse']]['items'].append(value)
        else:
          monkeys[monkey['throwTrue']]['items'].append(value)
      monkey['items'] = []
  inspections.sort()
  return inspections[-1]*inspections[-2]

def secondStar(input):
  modulo = 1
  for m in input:
    modulo = lcm(modulo, m['test'])
  inspections = [0] * len(input)
  monkeys = deepcopy(input)
  for round in range(10000):
    for i, monkey in enumerate(monkeys):
      for item in monkey['items']:
        inspections[i] += 1
        operator, operand = monkey['operation']
        if operand == 'old':
          value = operation(item, operator, item)
        else:
          value = operation(item, operator, int(operand))
        value = value % modulo
        if value % monkey['test']:
          monkeys[monkey['throwFalse']]['items'].append(value)
        else:
          monkeys[monkey['throwTrue']]['items'].append(value)
      monkey['items'] = []
  inspections.sort()
  return inspections[-1]*inspections[-2]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 119715

print("The second star is : {}".format(secondStar(input)))
# The second star is : 18085004878
