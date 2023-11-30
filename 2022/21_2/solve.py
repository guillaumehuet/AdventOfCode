def readInput(file):
  result = dict()
  for line in open(file).read().splitlines():
    line = line.split()
    name = line[0][:-1]
    if line[1].isnumeric():
      result[name] = int(line[1])
    else:
      result[name] = tuple(line[1:])
  return result

def firstStar(input):
  equation = input.copy()
  defined = [e for e in equation if isinstance(equation[e], int)]
  while not isinstance(equation['root'], int):
    newDefined = []
    for d in defined:
      for e in equation:
        if isinstance(equation[e], int):
          continue
        filled = False
        if equation[e][0] == d:
          equation[e] = (equation[d], ) + equation[e][1:]
          if isinstance(equation[e][2], int):
            filled = True
        if equation[e][2] == d:
          equation[e] = equation[e][:2] + (equation[d], )
          if isinstance(equation[e][0], int):
            filled = True
        if filled:
          if equation[e][1] == '+':
            equation[e] = equation[e][0] + equation[e][2]
          elif equation[e][1] == '-':
            equation[e] = equation[e][0] - equation[e][2]
          elif equation[e][1] == '*':
            equation[e] = equation[e][0] * equation[e][2]
          elif equation[e][1] == '/':
            equation[e] = equation[e][0] // equation[e][2]
          newDefined.append(e)
    defined = newDefined
  return equation['root']

def secondStar(input):
  equation = input.copy()
  equation['root'] = (equation['root'][0], '==', equation['root'][2])
  defined = [e for e in equation if isinstance(equation[e], int)]
  defined.remove('humn')
  while defined:
    newDefined = []
    for d in defined:
      for e in equation:
        if isinstance(equation[e], int):
          continue
        filled = False
        if equation[e][0] == d:
          equation[e] = (equation[d], ) + equation[e][1:]
          if isinstance(equation[e][2], int):
            filled = True
        if equation[e][2] == d:
          equation[e] = equation[e][:2] + (equation[d], )
          if isinstance(equation[e][0], int):
            filled = True
        if filled:
          if equation[e][1] == '+':
            equation[e] = equation[e][0] + equation[e][2]
          elif equation[e][1] == '-':
            equation[e] = equation[e][0] - equation[e][2]
          elif equation[e][1] == '*':
            equation[e] = equation[e][0] * equation[e][2]
          elif equation[e][1] == '/':
            equation[e] = equation[e][0] // equation[e][2]
          newDefined.append(e)
    defined = newDefined
  currMonkey = 'root'
  result = 0
  while currMonkey != 'humn':
    if isinstance(equation[currMonkey][2], int):
      operator = equation[currMonkey][1]
      operand = equation[currMonkey][2]
      if operator == '==':
        result = operand
      elif operator == '+':
        result -= operand
      elif operator == '-':
        result += operand
      elif operator == '*':
        result //= operand
      elif operator == '/':
        result *= operand
      currMonkey = equation[currMonkey][0]
    elif isinstance(equation[currMonkey][0], int):
      operator = equation[currMonkey][1]
      operand = equation[currMonkey][0]
      if operator == '==':
        result = operand
      elif operator == '+':
        result -= operand
      elif operator == '-':
        result = operand - result
      elif operator == '*':
        result //= operand
      elif operator == '/':
        result = operand // result
      currMonkey = equation[currMonkey][2]
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 63119856257960

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3006709232464
