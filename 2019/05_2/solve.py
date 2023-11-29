from pathlib import Path

def readInput(file):
  return [int(op) for op in Path(__file__).with_name(file).open('r').read().split(',')]

def runProgram(input, program):
  output = ""
  pc = 0
  instr = program[pc]
  op = instr % 100
  while True:
    if op == 99:                            # Halt
      return output

    elif op in (1, 2):                      # Valid Operations
      if (instr // 100) % 10:                 # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is mem
        a = program[program[pc + 1]]
      if (instr // 1000) % 10:                # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is imm
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
        program[program[pc + 1]] = input
      else:                                   # Ouput
        output = a
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
  return runProgram(1, input[:])

def secondStar(input):
  return runProgram(5, input[:])

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 9654885

print("The second star is : {}".format(secondStar(input)))
# The second star is : 7079459
