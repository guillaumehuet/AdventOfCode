from pathlib import Path

def readInput(file):
  return [int(c) for c in Path(__file__).with_name(file).open('r').read().splitlines()[0]]

def prettyPrint(layer):
  result = ""
  for line in layer:
    result += "\n" + "".join("#" if i else " " for i in line)
  return result

def layerize(input, width, height):
  layers = []
  layerCount = len(input) // (width * height)
  for l in range(layerCount):
    layers.append([])
    for i in range(height):
      start = (l * height + i) * width
      end = start + width
      layers[l].append(input[start:end])
  return layers

def firstStar(input):
  width = 25
  height = 6
  layers = layerize(input, width, height)
  minZeros = height * width
  twosTimesOnes = 0
  for l in layers:
    zeros = 0
    ones = 0
    twos = 0
    for i in range(height):
      for j in range(width):
        x = l[i][j]
        if x == 0:
          zeros += 1
        elif x == 1:
          ones += 1
        elif x == 2:
          twos += 1
        else:
          print('Error : {}'.format(x))
    if zeros < minZeros:
      twosTimesOnes = twos * ones
      minZeros = zeros
  return twosTimesOnes

def secondStar(input):
  width = 25
  height = 6
  layers = layerize(input, width, height)
  endImage = [[2]*width for _ in range(height)]
  for l in layers:
    for i in range(height):
      for j in range(width):
        if endImage[i][j] == 2:
          endImage[i][j] = l[i][j]
  return(prettyPrint(endImage))

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1920

print("The second star is : {}".format(secondStar(input)))
# The second star is :
###   ##  #  # #     ##
#  # #  # #  # #    #  #
#  # #    #  # #    #  #
###  #    #  # #    ####
#    #  # #  # #    #  #
#     ##   ##  #### #  #