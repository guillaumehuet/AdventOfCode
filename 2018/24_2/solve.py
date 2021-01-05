from copy import deepcopy

def readInput(file):
  armies = [[], []]
  attackOrder = []
  for line in open(file).read().splitlines():
    if line == "":
      continue
    if line == "Immune System:":
      key = 0
    elif line == "Infection:":
      key = 1
    else:
      words = line.split()
      nUnits = int(words[0])
      hitPoints = int(words[4])
      attackDamage = int(words[-6])
      attackType = words[-5]
      initiative = int(words[-1])
      immuneTo = set()
      weakTo = set()
      if '(' in line:
        for modifType in line.split('(')[1].split(')')[0].split(';'):
          modifs = modifType.split()
          modSet = set([m.replace(',','') for m in modifs[2:]])
          if modifs[0] == 'immune':
            immuneTo |= modSet
          else:
            weakTo |= modSet
      attackOrder.append((initiative, key, len(armies[key])))
      armies[key].append({'nUnits':nUnits, 'hitPoints':hitPoints, 'attackDamage':attackDamage, 'initiative':initiative, 'attackType':attackType, 'immuneTo':immuneTo, 'weakTo':weakTo})
  attackOrder.sort(reverse=True)
  attackOrder = tuple([t[1:] for t in attackOrder])
  return armies, attackOrder

def getSelectionOrder(armies):
  selectionOrder = []
  for i, army in enumerate(armies):
    for j, group in enumerate(army):
      effectivePower = group['attackDamage']*group['nUnits']
      initiative = group['initiative']
      selectionOrder.append((effectivePower, initiative, i, j))
  selectionOrder.sort(reverse=True)
  selectionOrder = tuple([t[2:] for t in selectionOrder])
  return selectionOrder

def targetSelection(armies, selectionOrder, verbose=False):
  selected = dict()
  for t in selectionOrder:
    army = t[0]
    group = t[1]
    attacker = armies[army][group]
    if attacker['nUnits'] == 0:
      continue
    effectivePower = attacker['attackDamage']*attacker['nUnits']
    ennemy = 0 if army else 1
    bestTarget = (-1, -1)
    bestDamage = 0
    bestEffectivePower = 0
    bestInitiative = 0
    for i, target in enumerate(armies[ennemy]):
      if target['nUnits'] == 0:
        continue
      if (ennemy, i) in selected.values():
        continue
      if attacker['attackType'] in target['immuneTo']:
        continue
      damage = effectivePower
      if attacker['attackType'] in target['weakTo']:
        damage *= 2
      if damage < bestDamage:
        continue
      targetEffectivePower = target['attackDamage']*target['nUnits']
      if damage == bestDamage:
        if targetEffectivePower < bestEffectivePower:
          continue
        if targetEffectivePower == bestEffectivePower:
          if target['initiative'] < bestInitiative:
            continue
      bestTarget = (ennemy, i)
      bestDamage = damage
      bestEffectivePower = targetEffectivePower
      bestInitiative = target['initiative']
      if verbose:
        armyName = "Infection" if army else "Immune System"
        sentence = armyName + " group " + str(group + 1) + " would deal defending group " + str(i + 1) + " " + str(bestDamage) + " damage"
        print(sentence)
    if bestTarget != (-1, -1):
      selected[(army, group)] = bestTarget
  if verbose:
    print()
  return selected

def attack(armies, attackOrder, selectionList, verbose=False):
  totalUnitsLost = 0
  for attackerId in attackOrder:
    if attackerId in selectionList:
      targetId = selectionList[attackerId]
      attackerArmy = attackerId[0]
      attackerGroup = attackerId[1]
      targetArmy = targetId[0]
      targetGroup = targetId[1]
      attacker = armies[attackerArmy][attackerGroup]
      target = armies[targetArmy][targetGroup]
      damage = attacker['attackDamage']*attacker['nUnits']
      if attacker['attackType'] in target['weakTo']:
          damage *= 2
      killedUnits = min(damage // target['hitPoints'], target['nUnits'])
      target['nUnits'] -= killedUnits
      totalUnitsLost += killedUnits
      if verbose:
        armyName = "Infection" if attackerArmy else "Immune System"
        sentence = armyName + " group " + str(attackerGroup + 1) + " attacks defending group " + str(targetGroup + 1) + ", killing " + str(killedUnits) + " units"
        print(sentence)
  if verbose:
    print()
  return totalUnitsLost

def turn(armies, attackOrder, verbose=False):
  if verbose:
    headers = ['Immune System:', 'Infection:']
    for army in range(2):
      print(headers[army])
      remainingGroups = False
      for (i, group) in enumerate(armies[army]):
        if group['nUnits'] > 0:
          sentence = "Group " + str(i + 1) + " contains " + str(group['nUnits']) + " units"
          print(sentence)
          remainingGroups = True
      if not remainingGroups:
        print("No groups remain.")
    print()
  selectionOrder = getSelectionOrder(armies)
  selectionList = targetSelection(armies, selectionOrder, verbose)
  totalUnitsLost = attack(armies, attackOrder, selectionList, verbose)
  return totalUnitsLost

def immuneSystemWinning(armies):
  for group in armies[1]:
    if group['nUnits'] > 0:
      return False
  return True

def unitsLeft(armies):
  result = 0
  for army in armies:
    for group in army:
      result += group['nUnits']
  return result

def firstStar(input):
  armies, attackOrder = input
  armies = deepcopy(armies)
  while turn(armies, attackOrder) > 0:
    pass
  return unitsLeft(armies)

def secondStar(input):
  armies, attackOrder = input
  boost = 0
  while True:
    boost += 1
    boostedArmies = deepcopy(armies)
    for group in boostedArmies[0]:
      group['attackDamage'] += boost
    while turn(boostedArmies, attackOrder) > 0:
      pass
    if immuneSystemWinning(boostedArmies):
      return unitsLeft(boostedArmies)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 24009

print("The second star is : {}".format(secondStar(input)))
# The second star is : 379
