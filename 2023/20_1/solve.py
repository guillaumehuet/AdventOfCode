from pathlib import Path

def readInput(file):
  modules = dict()
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    name, destinations = line.split(' -> ')
    destinations = tuple(destinations.split(', '))
    if name[0] in '%&':
      modules[name[1:]] = (name[0], destinations)
    else:
      modules[name] = (name, destinations)
  return modules

def conjuctionInputs(modules):
  result = dict()
  for m in modules:
    if modules[m][0] == '&':
      result[m] = []
      for m2 in modules:
        if m in modules[m2][1]:
          result[m].append(m2)
      result[m] = {key : False for key in result[m]}
  return result

def runOnce(modules, states, conjuction):
  pulses = [('broadcaster', False, 'button')]
  resultLow = 0
  resultHigh = 0
  while pulses:
    mod, value, origin = pulses.pop(0)
    # if mod == 'rx' and not value: # TODO : Reverse Engineer the code, brute force doesn't work
    #   exit('That happened !!')
    if value:
      resultHigh += 1
    else:
      resultLow += 1
    # printPulse(mod, value, origin)
    if mod not in modules:
      # print('{} is now {}'.format(mod, value))
      pass
    elif modules[mod][0] == '%':
      if not value:
        nextValue = not(states[mod])
        states[mod] = nextValue
        for dest in modules[mod][1]:
          pulses.append((dest, nextValue, mod))
    elif modules[mod][0] == '&':
      conjuction[mod][origin] = value
      nextValue = not all(conjuction[mod].values())
      for dest in modules[mod][1]:
        pulses.append((dest, nextValue, mod))
    else:
      for dest in modules[mod][1]:
        pulses.append((dest, value, mod))
  return resultLow, resultHigh

def printPulse(mod, value, origin):
  value = 'high' if value else 'low'
  print("{} -{}-> {}".format(origin, value, mod))

def firstStar(input):
  states = {key : False for key in input}
  conjuction = conjuctionInputs(input)
  resultLow = 0
  resultHigh = 0
  for _ in range(1000):
    addLow, addHigh = runOnce(input, states, conjuction)
    resultLow += addLow
    resultHigh += addHigh
  return resultLow*resultHigh

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 980457412

print("The second star is : {}".format(secondStar(input)))
# The second star is :
