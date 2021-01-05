from itertools import chain

class Node:
  def __init__(self, value, nextNode = None):
    self.value = value
    self.nextNode = nextNode

  def __repr__(self):
    return str(self.value)

class LinkedList():
  def __init__(self, content):
    iterable = iter(content)
    prevNode = Node(next(iterable))
    self.head = prevNode
    self.index = dict()
    self.index[prevNode.value] = prevNode
    self.len = 1
    for item in iterable:
      newNode = Node(item)
      prevNode.nextNode = newNode
      prevNode = newNode
      self.index[prevNode.value] = prevNode
      self.len += 1
    prevNode.nextNode = self.head

  def __repr__(self):
    result = [self.head]
    currNode = self.head.nextNode
    while currNode != self.head:
      result.append(currNode.value)
      currNode = currNode.nextNode
    return str(result)

  def rotate(self, n = 1):
    for _ in range(n):
      self.head = self.head.nextNode

  def __getitem__(self, value):
    return self.index[value]

  def round(self):
    cup0 = self.head
    cup1 = cup0.nextNode
    cup2 = cup1.nextNode
    cup3 = cup2.nextNode
    cup4 = cup3.nextNode
    cupsValues = (cup1.value, cup2.value, cup3.value)
    cupValue = cup0.value - 1
    if cupValue == 0:
      cupValue = self.len
    while cupValue in cupsValues:
      cupValue -= 1
      if cupValue == 0:
        cupValue = self.len
      
    destination = self[cupValue]
    cup0.nextNode = cup4
    cup3.nextNode = destination.nextNode
    destination.nextNode = cup1
    self.rotate()
  
  def stringFrom(self, n = 1):
    origin = self[n]
    result = ""
    currNode = origin.nextNode
    while currNode != origin:
      result += str(currNode)
      currNode = currNode.nextNode
    return result

def readInput(file):
  return tuple(int(n) for n in open(file).read().splitlines()[0])

def firstStar(input):
  circle = LinkedList(input)
  for _ in range(100):
    circle.round()
  return circle.stringFrom(1)

def secondStar(input):
  nMax = 1000000
  circle = LinkedList(chain(input, range(10, nMax + 1)))
  for _ in range(10 * nMax):
    circle.round()
  indexOf1 =  circle[1]
  firstNumber = indexOf1.nextNode
  secondNumber = firstNumber.nextNode
  return firstNumber.value*secondNumber.value

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 32658947

print("The second star is : {}".format(secondStar(input)))
# The second star is : 683486010900
