def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def readInput(file):
  timestamp, buses = open(file).read().splitlines()
  timestamp = int(timestamp)
  buses = tuple(int(b) if b != 'x' else 0 for b in buses.split(','))
  return timestamp, buses

def firstStar(input):
  timestamp = input[0]
  buses = input[1]
  minWait = buses[0] - timestamp % buses[0]
  bestBus = buses[0]
  for b in buses[1:]:
    if b != 0:
      wait = b - timestamp % b
      if wait < minWait:
        minWait = wait
        bestBus = b
  return minWait*bestBus

def secondStar(input):
  buses = input[1]
  modProd = 1
  t = 0
  for b in buses:
    if b != 0:
      modProd *= b
  for i in range(len(buses)):
    b = buses[i]
    if b != 0:
      rem = (b - i - 1) % b # To avoid the t % b = 0 case for the first bus, we calculate t - 1 and then add 1 at the end
      partialProd = modProd // b
      t += rem*partialProd*modinv(partialProd, b)
  return (t + 1)%modProd

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 3966

print("The second star is : {}".format(secondStar(input)))
# The second star is : 800177252346225
