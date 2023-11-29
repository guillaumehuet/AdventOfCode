from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()[0]

def initRecipes():
  # [recipesList, firstElfPtr, secondElfPtr]
  return [[3, 7], 0, 1]

def stepRecipes(recipes):
  recipesList = recipes[0]
  firstElfPtr = recipes[1]
  secondElfPtr = recipes[2]
  
  firstElfRecipe = recipesList[firstElfPtr]
  secondElfRecipe = recipesList[secondElfPtr]
  
  sumOfRecipes = firstElfRecipe + secondElfRecipe
  
  if sumOfRecipes > 9:
    recipesList.append(1)
  recipesList.append(sumOfRecipes%10)
  
  recipesLength = len(recipesList)
  
  recipes[1] += firstElfRecipe + 1
  recipes[1] %= recipesLength
  
  recipes[2] += secondElfRecipe + 1
  recipes[2] %= recipesLength

def firstStar(input):
  numRecipes = int(input)
  recipes = initRecipes()
  while len(recipes[0]) < numRecipes + 10:
    stepRecipes(recipes)
  return "".join(str(i) for i in recipes[0][numRecipes:numRecipes + 10])

def secondStar(input):
  lenRecipes = len(input)
  recipes = initRecipes()
  lastRecipes = ["", ""]
  i = 0
  while input not in lastRecipes:
    i += 1
    stepRecipes(recipes)
    lastRecipes = ["".join(str(i) for i in recipes[0][-lenRecipes:]), "".join(str(i) for i in recipes[0][-lenRecipes - 1: -1])]
  if lastRecipes[0] == input:
    return len(recipes[0]) - lenRecipes
  return len(recipes[0]) - lenRecipes - 1

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 9211134315

print("The second star is : {}".format(secondStar(input)))
# The second star is : 20357548
