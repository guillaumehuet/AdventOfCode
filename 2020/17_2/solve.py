from collections import defaultdict

def readInput(file):
  state = defaultdict(lambda: False)
  x = 0
  y = 0
  z = 0
  w = 0
  for line in open(file).read().splitlines():
    x = 0
    for c in line:
      if c == '#':
        state[(x, y, z, w)] = True
      x += 1
    y += 1
  
  return {'state' : state, 'lowBound' : [0, 0, 0, 0], 'highBound' : [x - 1 , y - 1, z, w]}

def step(state, lowBound, highBound, fourthDimension = False):
  newState = state.copy()
  newLowBound = lowBound.copy()
  newHighBound = highBound.copy()
  if fourthDimension:
    wLowBound = lowBound[3] - 1
    wHighBound = highBound[3] + 1
    lDelta = 1
  else:
    wLowBound = 0
    wHighBound = 0
    lDelta = 0
  for x in range(lowBound[0] - 1, highBound[0] + 2):
    for y in range(lowBound[1] - 1, highBound[1] + 2):
      for z in range(lowBound[2] - 1, highBound[2] + 2):
        for w in range(wLowBound, wHighBound + 1):
          neighbors = 0
          for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
              for k in range(z - 1, z + 2):
                for l in range(w - lDelta, w + lDelta + 1):
                  neighbors += state[(i, j, k, l)]
          if state[(x, y, z, w)] and (not (3 <= neighbors <= 4)):
            # NB : if (x, y, z, w) is active, it is counted in the neighbors, 2-3, becomes 3-4
            newState[(x, y, z, w)] = False
          elif (not state[(x, y, z, w)]) and (neighbors == 3):
            newState[(x, y, z, w)] = True
            if x < lowBound[0] :
              newLowBound[0] = lowBound[0] - 1
            elif x > highBound[0]:
              newHighBound[0] = highBound[0] + 1
            if y < lowBound[1] :
              newLowBound[1] = lowBound[1] - 1
            elif y > highBound[1]:
              newHighBound[1] = highBound[1] + 1
            if z < lowBound[2] :
              newLowBound[2] = lowBound[2] - 1
            elif z > highBound[2]:
              newHighBound[2] = highBound[2] + 1
            if fourthDimension:
              if w < lowBound[3] :
                newLowBound[3] = lowBound[3] - 1
              elif w > highBound[3]:
                newHighBound[3] = highBound[3] + 1
  
  currBounded = False
  while not currBounded:
    x = newLowBound[0]
    currBounded = False
    for w in range(newLowBound[3], newHighBound[3] + 1):
      if currBounded == True:
        break
      for y in range(newLowBound[1], newHighBound[1] + 1):
        if currBounded == True:
          break
        for z in range(newLowBound[2], newHighBound[2] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newLowBound[0] += 1
  
  currBounded = False
  while not currBounded:
    x = newHighBound[0]
    currBounded = False
    for w in range(newLowBound[3], newHighBound[3] + 1):
      if currBounded == True:
        break
      for y in range(newLowBound[1], newHighBound[1] + 1):
        if currBounded == True:
          break
        for z in range(newLowBound[2], newHighBound[2] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newHighBound[0] -= 1
  
  currBounded = False
  while not currBounded:
    y = newLowBound[1]
    currBounded = False
    for x in range(newLowBound[0], newHighBound[0] + 1):
      if currBounded == True:
        break
      for w in range(newLowBound[3], newHighBound[3] + 1):
        if currBounded == True:
          break
        for z in range(newLowBound[2], newHighBound[2] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newLowBound[1] += 1
  
  currBounded = False
  while not currBounded:
    y = newHighBound[1]
    currBounded = False
    for x in range(newLowBound[0], newHighBound[0] + 1):
      if currBounded == True:
        break
      for w in range(newLowBound[3], newHighBound[3] + 1):
        if currBounded == True:
          break
        for z in range(newLowBound[2], newHighBound[2] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newHighBound[1] -= 1
  
  currBounded = False
  while not currBounded:
    z = newLowBound[2]
    currBounded = False
    for x in range(newLowBound[0], newHighBound[0] + 1):
      if currBounded == True:
        break
      for y in range(newLowBound[1], newHighBound[1] + 1):
        if currBounded == True:
          break
        for w in range(newLowBound[3], newHighBound[3] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newLowBound[2] += 1
  
  currBounded = False
  while not currBounded:
    z = newHighBound[2]
    currBounded = False
    for x in range(newLowBound[0], newHighBound[0] + 1):
      if currBounded == True:
        break
      for y in range(newLowBound[1], newHighBound[1] + 1):
        if currBounded == True:
          break
        for w in range(newLowBound[3], newHighBound[3] + 1):
          if newState[(x, y, z, w)]:
            currBounded = True
            break
    if not currBounded:
      newHighBound[2] -= 1

  if fourthDimension:
    currBounded = False
    while not currBounded:
      w = newLowBound[3]
      currBounded = False
      for x in range(newLowBound[0], newHighBound[0] + 1):
        if currBounded == True:
          break
        for y in range(newLowBound[1], newHighBound[1] + 1):
          if currBounded == True:
            break
          for z in range(newLowBound[2], newHighBound[2] + 1):
            if newState[(x, y, z, w)]:
              currBounded = True
              break
      if not currBounded:
        newLowBound[3] += 1
    
    currBounded = False
    while not currBounded:
      w = newHighBound[3]
      currBounded = False
      for x in range(newLowBound[0], newHighBound[0] + 1):
        if currBounded == True:
          break
        for y in range(newLowBound[1], newHighBound[1] + 1):
          if currBounded == True:
            break
          for z in range(newLowBound[2], newHighBound[2] + 1):
            if newState[(x, y, z, w)]:
              currBounded = True
              break
      if not currBounded:
        newHighBound[3] -= 1

  return newState, newLowBound, newHighBound

def printState(state, lowBound, highBound, fourthDimension = False):
  for w in range(lowBound[3], highBound[3] + 1):
    for z in range(lowBound[2], highBound[2] + 1):
      line = 'z=' + str(z)
      if fourthDimension:
        line += ', w=' + str(w)
      print(line)
      for y in range(lowBound[1], highBound[1] + 1):
        line = ''
        for x in range(lowBound[0], highBound[0] + 1):
          if state[(x, y, z, w)]:
            line += '#'
          else:
            line += '.'
        print(line)
      print()
  print()

def firstStar(input):
  state = input['state']
  lowBound = input['lowBound']
  highBound = input['highBound']
  for _ in range(6):
    state, lowBound, highBound = step(state, lowBound, highBound)
  return(sum(state.values()))

def secondStar(input):
  state = input['state']
  lowBound = input['lowBound']
  highBound = input['highBound']
  for _ in range(6):
    state, lowBound, highBound = step(state, lowBound, highBound, True)
  return(sum(state.values()))

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 353

print("The second star is : {}".format(secondStar(input)))
# The second star is : 2472
