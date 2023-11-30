from pathlib import Path
from collections import defaultdict
from math import inf
from os import system

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

def printKnownMap(mapDict, position):
  xMin = position[0]
  xMax = position[0]
  yMin = position[1]
  yMax = position[1]
  sprites = ['.', ' ', '#', 'O']
  for (x, y) in mapDict:
    xMin = min(x, xMin)
    xMax = max(x, xMax)
    yMin = min(y, yMin)
    yMax = max(y, yMax)
  system('cls')
  print("+" + "-"*(xMax - xMin + 1) + "+")
  for y in range(yMin, yMax + 1):
    line = "|"
    for x in range(xMin, xMax + 1):
      if [x, y] == position:
        line += 'X'
      else:
        line += sprites[mapDict[(x, y)]]
    line += "|"
    print(line)
  print("+" + "-"*(xMax - xMin + 1) + "+")

def firstStar(input):
  program = readInput('input')
  mapDict = defaultdict(lambda:0)
  distDict = defaultdict(lambda:-1)
  firstStarResult = -1
  mapDict[(0, 0)] = 1
  distDict[(0, 0)] = 0
  position = [0, 0]
  pc = 0
  relBase = 0
  triedDirections = []
  totalDirections = (1, 3, 2, 4)
  origin = 1
  while True:
    #printKnownMap(mapDict, position)
    for i in range(4):
      direction = totalDirections[(totalDirections.index(origin) + i) % 4]
      if direction not in triedDirections:
        triedDirections.append(direction)
        break
    else: # Dead end, reverse
      direction = origin
    errCode, output, pc, relBase, errString =  runProgram([direction], program, pc, relBase)
    if errCode == 0:
      return "Ended"
    elif errCode == 3:
      if output[0] == 0: # We hit a wall
        if direction == 1:
          mapDict[(position[0], position[1] - 1)] = 2
        elif direction == 2:
          mapDict[(position[0], position[1] + 1)] = 2
        elif direction == 3:
          mapDict[(position[0] - 1, position[1])] = 2
        elif direction == 4:
          mapDict[(position[0] + 1, position[1])] = 2
      elif output[0] in (1, 2): # The position is cleared and we moved to it
        prevDist = distDict[tuple(position)]
        if direction == 1:
          position[1] -= 1
          origin = 2
        elif direction == 2:
          position[1] += 1
          origin = 1
        elif direction == 3:
          position[0] -= 1
          origin = 4
        elif direction == 4:
          position[0] += 1
          origin = 3
        triedDirections = [origin] # Set the origin direction in the triedDirection in order not to backtrack
        if output[0] == 2:  # We found the oxygen tank
          mapDict[tuple(position)] = 3
          if firstStarResult == -1:
            firstStarResult = prevDist + 1
            distDict = defaultdict(lambda:-1)
            distDict[tuple(position)] = 0
          else:
            return firstStarResult, max(distDict.values())
        else:
          mapDict[tuple(position)] = 1
          if distDict[tuple(position)] == -1:
            distDict[tuple(position)] = prevDist + 1

results = firstStar(input)

print("The first star is : {}".format(results[0]))
# The first star is : 224

print("The second star is : {}".format(results[1]))
# The second star is : 284
