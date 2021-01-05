from collections import defaultdict
from math import inf

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

def sign(value):
  if value == 0:
    return 0
  if value < 0:
    return -1
  return 1

def readInput(file):
  result = defaultlist(lambda: 0)
  result += [int(op) for op in open(file).read().split(',')]
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

drawDict = defaultdict(lambda : 0)

def drawScreen(screen):
  if len(drawDict) > 0:
    xMax = max(drawDict, key=lambda x: x[0])[0]
    yMax = max(drawDict, key=lambda x: x[1])[1]
  else:
    xMax = 0
    yMax = 0
  
  sprites = [' ', '#', '=', '_', 'o']

  xPaddle = -1
  xBall = -1
  score = -1
  remainingBlocks = 0

  for i in range(len(screen)//3):
    x = screen[3*i]
    y = screen[3*i + 1]
    sprite = screen[3*i + 2]
    drawDict[x, y] = sprite
    xMax = max(x, xMax)
    yMax = max(y, yMax)
  display = ""
  score = drawDict[-1, 0]
  for y in range(yMax + 1):
    display += "\n"
    for x in range(xMax + 1):
      sprite = drawDict[x, y]
      if sprite == 2:
        remainingBlocks += 1
      elif sprite == 3:
        xPaddle = x
      elif sprite == 4:
        xBall = x
      display += sprites[sprite]
  return display, score, remainingBlocks, xPaddle, xBall

def firstStar(input):
  program = readInput('input')
  errCode, output, pc, relBase, errString = runProgram([], program)
  if errCode == 0:
    result = 0
    for i in range(len(output)//3):
      if output[3*i + 2] == 2:
        result += 1
    return result
  else:
    return errString

def secondStar(input):
  program = readInput('input')
  program[0] = 2
  pc = 0
  relBase = 0
  userInput = []
  while True:
    errCode, output, pc, relBase, errString = runProgram(userInput, program, pc, relBase)
    if errCode == 0:
      display, score, remainingBlocks, xPaddle, xBall = drawScreen(output)
      return score
    else:
      display, score, remainingBlocks, xPaddle, xBall = drawScreen(output)
      userInput = [sign(xBall - xPaddle)]

print("The first star is : {}".format(firstStar(input)))
# The first star is : 420

print("The second star is : {}".format(secondStar(input)))
# The second star is : 21651
