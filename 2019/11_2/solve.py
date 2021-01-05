from collections import defaultdict

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

def turnRobot(robotDir, turn):
  # 0 means turn left
  # 1 means turn right
  if robotDir[0] == 0: # up or down
    if robotDir[1] + 2*turn == 1: # up + turn right or down + turn left
      return (1, 0) # right
    else:
      return (-1, 0) # left
  else: # left or right
    if robotDir[0] + 2*turn == 1: # left + turn right or right + turn left
      return (0, -1) # up
    else:
      return (0, 1) # down

def moveRobot(robotPos, robotDir):
  return (robotPos[0] + robotDir[0], robotPos[1] + robotDir[1])

def paintGrid(input, startPannelColor = 0):
  gridDict = defaultdict(lambda: 0)
  robotDir = (0, -1)
  robotPos = (0, 0)
  gridDict[robotPos] = startPannelColor
  errCode, output, pc, relBase, errString = runProgram([gridDict[robotPos]], input)
  while errCode == 3:
    gridDict[robotPos] = output[0]
    robotDir = turnRobot(robotDir, output[1])
    robotPos = moveRobot(robotPos, robotDir)
    errCode, output, pc, relBase, errString = runProgram([gridDict[robotPos]], input, pc, relBase)
  if errCode == -1:
    return errString
  return gridDict

def printGrid(grid):
  oneGrid = defaultdict(lambda: 0)
  for coord in grid:
    if grid[coord]:
      oneGrid[coord] = 1
  minX = min(oneGrid, key=lambda x: x[0])[0]
  maxX = max(oneGrid, key=lambda x: x[0])[0]
  minY = min(oneGrid, key=lambda x: x[1])[1]
  maxY = max(oneGrid, key=lambda x: x[1])[1]
  output = ""
  for y in range(minY, maxY + 1):
    output += "\n"
    for x in range(minX, maxX + 1):
      if oneGrid[x, y]:
        output += "#"
      else:
        output += " "
  return output

def firstStar(input):
  input = readInput('input')
  return len(paintGrid(input))

def secondStar(input):
  input = readInput('input')
  return printGrid(paintGrid(input, 1))

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1771

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
#  #  ##  #### #  #   ## #  # #  # ####
#  # #  # #    #  #    # #  # #  #    #
#### #    ###  ####    # #### #  #   #
#  # # ## #    #  #    # #  # #  #  #
#  # #  # #    #  # #  # #  # #  # #
#  #  ### #### #  #  ##  #  #  ##  ####
