def readInput(file):
  tests = []
  instructions = []
  isTest = False
  for line in open(file).read().splitlines():
    if len(line) == 0:
      continue
    elif line[0] == 'B':
      isTest = True
      tests.append([[int(c) for c in line.replace(' ','').split(':')[1][1:-1].split(',')]])
    elif line[0] == 'A':
      isTest = False
      tests[-1].append([int(c) for c in line.replace(' ','').split(':')[1][1:-1].split(',')])
    elif isTest:
      tests[-1].append([int(c) for c in line.split()])
    else:
      instructions.append([int(c) for c in line.split()])
  return tests, instructions

def firstStar(input):
  result = 0
  for test in input[0]:
    if len(testInstruction(test[0], test[1], test[2])) >= 3:
      result += 1
  return result

def secondStar(input):
  correspondingOpcodes = findCorrespondingOpcodes(input[0])
  registers = [0, 0, 0, 0]
  for i in input[1]:
    opCodes[correspondingOpcodes[i[0]]](i[1], i[2], i[3], registers)
  
  return registers[0]

# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
def addr(A, B, C, registers):
  registers[C] = registers[A] + registers[B]
# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(A, B, C, registers):
  registers[C] = registers[A] + B

# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(A, B, C, registers):
  registers[C] = registers[A] * registers[B]
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(A, B, C, registers):
  registers[C] = registers[A] * B

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(A, B, C, registers):
  registers[C] = registers[A] & registers[B]
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(A, B, C, registers):
  registers[C] = registers[A] & B

# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(A, B, C, registers):
  registers[C] = registers[A] | registers[B]
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(A, B, C, registers):
  registers[C] = registers[A] | B

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(A, B, C, registers):
  registers[C] = registers[A]
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(A, B, C, registers):
  registers[C] = A

# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(A, B, C, registers):
  if A > registers[B]:
    registers[C] = 1
  else:
    registers[C] = 0
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(A, B, C, registers):
  if registers[A] > B:
    registers[C] = 1
  else:
    registers[C] = 0
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(A, B, C, registers):
  if registers[A] > registers[B]:
    registers[C] = 1
  else:
    registers[C] = 0

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(A, B, C, registers):
  if A == registers[B]:
    registers[C] = 1
  else:
    registers[C] = 0
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(A, B, C, registers):
  if registers[A] == B:
    registers[C] = 1
  else:
    registers[C] = 0
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(A, B, C, registers):
  if registers[A] == registers[B]:
    registers[C] = 1
  else:
    registers[C] = 0

opCodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def testInstruction(before, instruction, after):
  possibleOpCodes = []
  for i in range(16):
    registers = before.copy()
    opCodes[i](instruction[1], instruction[2], instruction[3], registers)
    if registers == after:
      possibleOpCodes.append(i)
  return possibleOpCodes

def findCorrespondingOpcodes(tests):
  correspondingOpcodesSet = [set(range(16)) for _ in range(16)]
  for t in tests:
    opCode = t[1][0]
    correspondingOpcodesSet[opCode] &= set(testInstruction(t[0], t[1], t[2]))
  
  correspondingOpcodes = [-1 for _ in range(16)]
  while -1 in correspondingOpcodes:
    for i in range(len(correspondingOpcodesSet)):
      if len(correspondingOpcodesSet[i]) == 1:
        correspondingOpcodes[i] = correspondingOpcodesSet[i].pop()
        for corr in correspondingOpcodesSet:
          corr.discard(correspondingOpcodes[i])
  return correspondingOpcodes

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 509

print("The second star is : {}".format(secondStar(input)))
# The second star is : 496
