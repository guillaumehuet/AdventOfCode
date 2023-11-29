from pathlib import Path

def readInput(file):
  return [int(c) for c in Path(__file__).with_name(file).open('r').read().splitlines()[0].split()]

def firstStar(input):
  return nestedSum(processChild(input, 0)[1])

def processChild(input, ptr):
  childCount = input[ptr]
  ptr += 1
  metadataCount = input[ptr]
  ptr += 1
  childrenMetadata = []
  metadata = []
  for child in range(childCount):
    ptr, childrenMetadata = processChild(input, ptr)
    metadata.append(childrenMetadata)
  for i in range(metadataCount):
    metadata.append(input[ptr])
    ptr += 1
  return ptr, metadata

def nestedSum(metadata):
  result = 0
  for item in metadata:
    if type(item) is list:
      result += nestedSum(item)
    else:
      result += item
  return result

def secondStar(input):
  return indexSum(processChild(input, 0)[1])

def indexSum(metadata):
  if type(metadata) is not list:
    return 0
  
  hasChildren = False
  
  for item in metadata:
    if type(item) is list:
      hasChildren = True
      break
  
  if hasChildren:
    result = 0
    for item in metadata:
      if type(item) is not list:
        try:
          result += indexSum(metadata[item - 1])
        except IndexError:
          pass
    return result
  else:
    return sum(metadata)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 42196

print("The second star is : {}".format(secondStar(input)))
# The second star is : 33649
