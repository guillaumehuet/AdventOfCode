from pathlib import Path
from itertools import permutations

def readInput(file):
  return [int(op) for op in Path(__file__).with_name(file).open('r').read().split(',')]

def runProgram(inputs, program, pc = 0):
  inputN = 0
  instr = program[pc]
  op = instr % 100
  while True:
    if op == 99:                            # Halt
      return "EOF", -1

    elif op in (1, 2):                      # Valid Operations
      if (instr // 100) % 10:                 # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is mem
        a = program[program[pc + 1]]
      if (instr // 1000) % 10:                # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is mem
        b = program[program[pc + 2]]

      if op == 1:                             # Add
        program[program[pc + 3]] = a + b
      else:                                   # Multiply
        program[program[pc + 3]] = a * b
      pc += 4

    elif op in (3, 4):                      # Valid IO
      if (instr // 100) % 10:                 # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is mem
        a = program[program[pc + 1]]

      if op == 3:                             # Input
        program[program[pc + 1]] = inputs[inputN]
        inputN += 1
      else:                                   # Ouput
        return a, pc + 2
      pc += 2
    
    elif op in (5, 6):                      # Valid jumps
      if (instr // 100) % 10:                 # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is mem
        a = program[program[pc + 1]]
      if (instr // 1000) % 10:                # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is mem
        b = program[program[pc + 2]]
      
      if op == 5:                             # Jump if true
        if a:
          pc = b
        else:
          pc += 3
      else:                                   # Jump if false
        if not a:
          pc = b
        else:
          pc += 3
    
    elif op in (7, 8):                      # Valid comparisons
      if (instr // 100) % 10:                 # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is mem
        a = program[program[pc + 1]]
      if (instr // 1000) % 10:                # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is mem
        b = program[program[pc + 2]]

      if op == 7:                             # Less than
        if a < b:
          program[program[pc + 3]] = 1
        else:
          program[program[pc + 3]] = 0
      else:                                   # Equal
        if a == b:
          program[program[pc + 3]] = 1
        else:
          program[program[pc + 3]] = 0
      
      pc += 4
    
    else:                                   # Invalid opcode
      return "Intcode Error! : {} @ {}".format(op, pc)

    instr = program[pc]
    op = instr % 100
  
  
def firstStar(input):
  result = 0
  phaseSettings = permutations(range(5))
  for phases in phaseSettings:
    output = 0
    for progNum in range(5):
      output, _ = runProgram([phases[progNum], output], input[:])
    result = max(output, result)
  return result

def secondStar(input):
  result = 0
  phaseSettings = permutations(range(5, 10))
  for phases in phaseSettings:
    programs = [input[:] for _ in range(5)]
    pcList = [0]*5
    output = 0
    tempResult = 0
    for progNum in range(5):
      output, pcList[progNum] = runProgram([phases[progNum], output], programs[progNum])
    while output != 'EOF':
      for progNum in range(5):
        output, pcList[progNum] = runProgram([output], programs[progNum], pcList[progNum])
        if output != 'EOF':
          tempResult = output
    result = max(tempResult, result)
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 880726

print("The second star is : {}".format(secondStar(input)))
# The second star is : 4931744
