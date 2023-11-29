from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def execInstruction(program, acc, ip):
  instr = program[ip]
  op, arg = instr.split(' ')
  if op == 'nop':
    return acc, ip + 1
  elif op == 'jmp':
    return acc, ip + int(arg)
  elif op == 'acc':
    return acc + int(arg), ip + 1

def generateAllPrograms(program):
  result = [program]
  for ip in range(len(program)):
    op, arg = program[ip].split(' ')
    if op in ('jmp', 'nop'):
      newProgram = program.copy()
      if op == 'jmp':
        newOp = 'nop'
      else:
        newOp = 'jmp'
      newInstr = ' '.join([newOp, arg])
      newProgram[ip] = newInstr
      result.append(newProgram)
  return result

def firstStar(input):
  program = input
  ip = 0
  acc = 0
  executed = set()
  while ip not in executed:
    executed.add(ip)
    acc, ip = execInstruction(program, acc, ip)
  return acc

def secondStar(input):
  terminate = len(input)
  for program in generateAllPrograms(input):
    ip = 0
    acc = 0
    executed = set()
    while ip not in executed:
      if ip == terminate:
        return acc
      if ip > terminate:
        break
      executed.add(ip)
      acc, ip = execInstruction(program, acc, ip)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1134

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1205
