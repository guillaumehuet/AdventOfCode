from pathlib import Path

class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx
    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())
    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)
    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)

def readInput(file):
  result = defaultlist(lambda: 0)
  result += [int(op) for op in Path(__file__).with_name(file).open('r').read().split(',')]
  return result

def runProgram(inputs, program, pc = 0, relBase = 0):
  # Output : errCode, output, pc, relBase, errString
  # errCode :
  #   0 : Program Halted
  #   1 : Input Required
  #  -1 : Intcode Error! : {op} @ {pc}
  inputN = 0
  output = []
  instr = program[pc]
  op = instr % 100
  while True:
    if op == 99:                            # Halt
      return 0, output, pc, relBase, "Program Halted"

    elif op in (1, 2):                      # Valid Operations
      if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem
        a = program[program[pc + 1]]
      elif ((instr // 100) % 10) == 1:        # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is rel
        a = program[program[pc + 1] + relBase]
      if ((instr // 1000) % 10) == 0:         # 2nd parameter mode is mem
        b = program[program[pc + 2]]
      elif ((instr // 1000) % 10) == 1:       # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is rel
        b = program[program[pc + 2] + relBase]

      if op == 1:                             # Add
        result = a + b
      else:                                   # Multiply
        result = a * b

      if ((instr // 10000) % 10) == 0:        # 3rd parameter mode is mem
        program[program[pc + 3]] = result
      else:                                   # 3rd parameter mode is rel
        program[program[pc + 3] + relBase] = result
      pc += 4

    elif op in (3, 4):                      # Valid IO
      if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem
        a = program[program[pc + 1]]
      elif ((instr // 100) % 10) == 1:        # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is rel
        a = program[program[pc + 1] + relBase]

      if op == 3:                             # Input
        if inputN + 1 > len(inputs):
          return 3, output, pc, relBase, "Input Required"
        else:
          result = inputs[inputN]
        inputN += 1
        if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem (special case)
          program[program[pc + 1]] = result
        else:                                   # 1st parameter mode is rel (special case)
          program[program[pc + 1] + relBase] = result
      else:                                   # Ouput
        output.append(a)
      pc += 2
    
    elif op in (5, 6):                      # Valid jumps
      if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem
        a = program[program[pc + 1]]
      elif ((instr // 100) % 10) == 1:        # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is rel
        a = program[program[pc + 1] + relBase]
      if ((instr // 1000) % 10) == 0:         # 2nd parameter mode is mem
        b = program[program[pc + 2]]
      elif ((instr // 1000) % 10) == 1:       # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is rel
        b = program[program[pc + 2] + relBase]
      
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
      if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem
        a = program[program[pc + 1]]
      elif ((instr // 100) % 10) == 1:        # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is rel
        a = program[program[pc + 1] + relBase]
      if ((instr // 1000) % 10) == 0:         # 2nd parameter mode is mem
        b = program[program[pc + 2]]
      elif ((instr // 1000) % 10) == 1:       # 2nd parameter mode is imm
        b = program[pc + 2]
      else:                                   # 2nd parameter mode is rel
        b = program[program[pc + 2] + relBase]

      if op == 7:                             # Less than
        if a < b:
          result = 1
        else:
          result = 0
      else:                                   # Equal
        if a == b:
          result = 1
        else:
          result = 0

      if ((instr // 10000) % 10) == 0:        # 3rd parameter mode is mem
        program[program[pc + 3]] = result
      else:                                   # 3rd parameter mode is rel
        program[program[pc + 3] + relBase] = result
      pc += 4
    
    elif op == 9:                           # Valid relative base adjust
      if ((instr // 100) % 10) == 0:          # 1st parameter mode is mem
        a = program[program[pc + 1]]
      elif ((instr // 100) % 10) == 1:        # 1st parameter mode is imm
        a = program[pc + 1]
      else:                                   # 1st parameter mode is rel
        a = program[program[pc + 1] + relBase]   
      relBase += a
      pc += 2
    
    else:                                   # Invalid opcode
      return -1, output, pc, relBase, "Intcode Error! : {} @ {}".format(op, pc)

    instr = program[pc]
    op = instr % 100

def firstStar():
  program = readInput('input')
  cameraFeed = runProgram([], program)[1]
  cameraView = "".join(chr(n) for n in cameraFeed)
  cameraMap = []
  for line in cameraView.splitlines():
    cameraMap.append([0 if c == '.' else 1 for c in line])
  cameraMap.pop()
  result = 0
  for x in range(1, len(cameraMap[0]) - 1):
    for y in range(1, len(cameraMap) - 1):
      if cameraMap[y][x] and cameraMap[y - 1][x] and cameraMap[y + 1][x] and cameraMap[y][x - 1] and cameraMap[y][x + 1]:
        result += x*y
  return result

def secondStar():
  # A,C,A,C,B,B,C,A,C,B

  # A = L,8,R,12,R,12,R,10
  # B = L,10,R,10,L,6
  # C = R,10,R,12,R,10
  program = readInput('input')
  prgInput = [ord(c) for c in "A,C,A,C,B,B,C,A,C,B\nL,8,R,12,R,12,R,10\nL,10,R,10,L,6\nR,10,R,12,R,10\nn\n"]
  program[0] = 2
  errCode, output, pc, relBase, errString = runProgram(prgInput, program)
  result = output[-1]
  return result

print("The first star is : {}".format(firstStar()))
# The first star is : 4372

print("The second star is : {}".format(secondStar()))
# The second star is : 945911
