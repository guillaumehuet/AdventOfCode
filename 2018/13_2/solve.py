cardinal = [
  ( 0, -1), # North
  ( 1,  0), # East
  ( 0,  1), # South
  (-1,  0), # West
]

rotation = [
  -1, # Left
   0, # Straight
   1  # Right
]

class cart:
  def __init__(self, x, y, c, map):
    self.x = x
    self.y = y
    self.map = map
    
    if c == '^':
      self.card = 0
    elif c == '>':
      self.card = 1
    elif c == 'v':
      self.card = 2
    elif c == '<':
      self.card = 3
    else:
      raise Exception('Unknown cart direction symbol : ' + c)
    
    self.rot = 0
  
  def intersection(self):
    self.card += rotation[self.rot]
    self.card %= 4
    self.rot += 1
    self.rot %= 3
  
  def step(self):
    addX, addY = cardinal[self.card]
    self.x += addX
    self.y += addY
    c = self.map[self.y][self.x]
    if c in '-|': # Continue on track
      pass
    elif c == '+': # Change track depening on current rotation policy
      self.intersection()
    elif c == '/': # Turn left if going east or west, turn right if going north or south
      if self.card%2:
        self.card -= 1
        self.card %= 4
      else:
        self.card += 1
        self.card %= 4
    elif c == '\\': # Turn right if going east or west, turn left if going north or south
      if self.card%2:
        self.card += 1
        self.card %= 4
      else:
        self.card -= 1
        self.card %= 4
    else:
      raise Exception('Unknown map symbol : ' + c)
  
  def __lt__(self, other):
    return self.pos() < other.pos()
  
  def pos(self):
    return self.y, self.x
  
  def toChar(self):
    if self.card == 0:
      return '^'
    elif self.card == 1:
      return '>'
    elif self.card == 2:
      return 'v'
    elif self.card == 3:
      return '<'

def readInput(file):
  map = []
  carts = []
  y = 0
  for line in open(file).read().splitlines():
    x = 0
    map.append([])
    for c in line:
      if c in '<>^v':
        carts.append(cart(x, y, c, map))
        if c in '<>':
          c = '-'
        else:
          c = '|'
      map[y].append(c)
      x += 1
    y += 1
  return carts

def stepSim(carts):
  carts.sort()
  for cart in carts:
    cartPos = [cart.pos() for cart in carts]
    cart.step()
    if cart.pos() in cartPos:
      return cart.pos()
  return False

def stepSimSecondStar(carts):
  carts.sort()
  i = 0
  while i < len(carts): # !!!!!!!!!!!!!!!!!!!!!!!!!!! Do not modify references while removing elements
    cartPos = [cart.pos() for cart in carts]
    carts[i].step()
    posToRemove = carts[i].pos()
    if posToRemove in cartPos:
      cartsToRemove = [j for j in range(len(carts)) if carts[j].pos() == carts[i].pos()]
      for j in sorted(cartsToRemove, reverse = True):
        if j <= i:
          i -= 1
        del carts[j]
    i += 1

def printMap(map):
  for l in map:
    print("".join(l))

def printMapWithCarts(carts):
  map = carts[0].map
  cartPos = dict()
  for i in range(len(carts)):
    cartPos[carts[i].pos()] = i
  for y in range(len(map)):
    for x in range(len(map[y])):
      if (y, x) in cartPos:
        c = carts[cartPos[(y, x)]].toChar()
      else:
        c = map[y][x]
      print(c, end = '')
    print()
  print()

def firstStar(input):
  collision = False
  while not collision:
    collision = stepSim(input)
  return str(collision[::-1])[1:-1].replace(' ','')

def secondStar(input):
  while len(input) > 1:
    stepSimSecondStar(input)
  return str(input[0].pos()[::-1])[1:-1].replace(' ','')

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 116,91

input = readInput('input')

print("The second star is : {}".format(secondStar(input)))
# The second star is : 8,23
