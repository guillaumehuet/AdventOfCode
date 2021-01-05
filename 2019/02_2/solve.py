def readInput(file):
  return [int(op) for op in open(file).read().split(',')]

def runProgram(noun, verb, program):
  program[1] = noun
  program[2] = verb
  pc = 0
  op = program[pc]
  while op in (1, 2, 99):
    if op == 99:
      return program[0]
    elif op == 1:
      program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
    else:
      program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
    pc += 4
    op = program[pc]
  return "There was an error!"

def firstStar(input):
  return runProgram(12, 2, input[:])

def secondStar(input):
  for noun in range(100):
    for verb in range(100):
      if runProgram(noun, verb, input[:]) == 19690720:
        return 100*noun + verb

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3085697

print("The second star is : {}".format(secondStar(input)))
# The second star is : 9425
