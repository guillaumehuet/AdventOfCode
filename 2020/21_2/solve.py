def readInput(file):
  result = []
  for line in open(file).read().splitlines():
    ingredients, allergens = line.split(' (contains ')
    ingredients = tuple(ingredients.split())
    allergens = tuple(allergens[:-1].split(', '))
    result.append((ingredients, allergens))
  return tuple(result)

def identifyAllergens(ingredientList):
  allergens = set()
  ingredients = set()
  allergensCandidates = dict()
  for i in ingredientList:
    allergens |= set(i[1])
    ingredients |= set(i[0])

  for a in allergens:
    allergensCandidates[a] = ingredients.copy()
    for i in ingredientList:
      if a in i[1]:
        allergensCandidates[a] &= set(i[0])

  allergenOrigin = dict()
  removedCandidate = True
  while removedCandidate:
    removedCandidate = False
    for a in allergens:
      if len(allergensCandidates[a]) == 1:
        removedCandidate = True
        i = allergensCandidates[a].pop()
        allergenOrigin[a] = i
        for a2 in allergens:
          allergensCandidates[a2].discard(i)
  
  return allergenOrigin

def firstStar(input):
  allergenOrigin = identifyAllergens(input)
  allergenicIngredients = set(allergenOrigin.values())
  result = 0
  for ingredientList in input:
    for ingredient in ingredientList[0]:
      if ingredient not in allergenicIngredients:
        result += 1
  return result

def secondStar(input):
  allergenOrigin = identifyAllergens(input)
  result = ''
  for a in sorted(allergenOrigin):
    result += allergenOrigin[a] + ','
  result = result[:-1]
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2779

print("The second star is : {}".format(secondStar(input)))
# The second star is : lkv,lfcppl,jhsrjlj,jrhvk,zkls,qjltjd,xslr,rfpbpn
