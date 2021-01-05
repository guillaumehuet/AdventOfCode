def readInput(file):
  return open(file).read().splitlines()

def getMask(maskString):
  maskOfMask = 0
  mask = 0
  for c in maskString:
    maskOfMask <<= 1
    mask <<= 1
    if c in '01':
      maskOfMask += 1
      if c == '1':
        mask += 1
  return mask, maskOfMask

def maskedValue(value, mask, maskOfMask):
  return (~maskOfMask & value) | (maskOfMask & mask)

def maskedAddresses(address, mask, maskOfMask):
  result = [0]
  for i in range(36):
    newResult = []
    if maskOfMask & 1:
      bits = [(mask & 1) | (address & 1)]
    else:
      bits = [0, 1]
    for r in result:
      for b in bits:
        newResult.append((r) | b << i)
    mask >>= 1
    maskOfMask >>= 1
    address >>= 1
    result = newResult
  return result

def firstStar(input):
  memory = dict()
  mask = 0
  maskOfMask = 0
  for line in input:
    action, value = line.split(' = ')
    if action == 'mask':
      mask, maskOfMask = getMask(value)
    else:
      address = int(action.split('[')[-1][:-1])
      value = int(value)
      memory[address] = maskedValue(value, mask, maskOfMask)
  return sum(memory.values())

def secondStar(input):
  memory = dict()
  mask = 0
  maskOfMask = 0
  for line in input:
    action, value = line.split(' = ')
    if action == 'mask':
      mask, maskOfMask = getMask(value)
    else:
      address = int(action.split('[')[-1][:-1])
      value = int(value)
      addresses = maskedAddresses(address, mask, maskOfMask)
      for address in addresses:
        memory[address] = value
  return sum(memory.values())

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 7477696999511

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3687727854171
