def readInput(file):
  return open(file).read().splitlines()[0]

def product(values):
  result = 1
  for v in values:
    result *= v
  return result

def bitStream(hex):
  result = []
  for c in hex:
    n = int(c, 16)
    for i in range(3, -1, -1):
      bit = n // (2**i)
      n = n % (2**i)
      result.append(True if bit else False)
  return result

def toNumber(stream):
  result = 0
  for c in stream:
    result *= 2
    if c:
      result += 1
  return result

def decodePacket(stream, cursor = 0):
  version = toNumber(stream[cursor:cursor + 3])
  cursor += 3
  typeID = toNumber(stream[cursor:cursor + 3])
  cursor += 3
  if typeID == 4:
    # Literal value
    result = 0
    last = False
    while not last:
      result *= 16
      if not stream[cursor]:
        last = True
      cursor += 1
      result += toNumber(stream[cursor:cursor + 4])
      cursor += 4
    return result, version, cursor
  else:
    # Operator
    lengthTypeID = stream[cursor]
    cursor += 1
    values = []
    if lengthTypeID:
      numSubPackets = toNumber(stream[cursor:cursor + 11])
      cursor += 11
      for _ in range(numSubPackets):
        value, subVersion, cursor = decodePacket(stream, cursor)
        version += subVersion
        values.append(value)
    else:
      cursorEnd = toNumber(stream[cursor:cursor + 15]) + cursor + 15
      cursor += 15
      while cursor < cursorEnd:
        value, subVersion, cursor = decodePacket(stream, cursor)
        version += subVersion
        values.append(value)
    if typeID == 0:
      value = sum(values)
    elif typeID == 1:
      value = product(values)
    elif typeID == 2:
      value = min(values)
    elif typeID == 3:
      value = max(values)
    elif typeID == 5:
      value = 1 if values[0] > values[1] else 0
    elif typeID == 6:
      value = 1 if values[0] < values[1] else 0
    elif typeID == 7:
      value = 1 if values[0] == values[1] else 0
    return value, version, cursor
      

def firstStar(input):
  stream = bitStream(input)
  _, version, _ = decodePacket(stream)
  return version

def secondStar(input):
  stream = bitStream(input)
  value, _, _ = decodePacket(stream)
  return value

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 897

print("The second star is : {}".format(secondStar(input)))
# The second star is : 9485076995911
