from pathlib import Path

def readInput(file):
  return [int(c) for c in Path(__file__).with_name(file).open('r').read().splitlines()[0]]

def singleDigit(n):
  return abs(n) % 10

def FFTSecondHalfDirect(message, rounds, repeats):
  messageSize = len(message)
  totalMessageSize = messageSize*repeats
  offset = int("".join(str(c) for c in message[0:7]))
  if offset > (totalMessageSize):
    return "Offset too long for message"
  if offset < (totalMessageSize // 2):
    return "Offset too short for method"
  message = message*repeats
  for _ in range(rounds):
    for i in range(len(message) - 2, offset - 1, -1):
      message[i] = (message[i] + message[i + 1]) % 10
  return "".join(str(c) for c in message[offset:offset + 8])

def FFT(message, rounds):
  result = message.copy()
  for _ in range(rounds):
    for n in range(0, len(result)):
      add = sum(result[i] for i in range(len(result)) if i%(4*(n + 1)) in range(n, 2*n + 1))
      sub = sum(result[i] for i in range(len(result)) if i%(4*(n + 1)) in range(3*n + 2, 4*n + 3))
      result[n] = singleDigit(add - sub)
  return "".join(str(c) for c in result[0:8])

def firstStar(input):
  return FFT(input, 100)

def secondStar(input):
  return FFTSecondHalfDirect(input, 100, 10000)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 76795888

print("The second star is : {}".format(secondStar(input)))
# The second star is : 84024125
