from pathlib import Path

def readInput(file):
  categories = dict()
  tickets = []
  lines = iter(Path(__file__).with_name(file).open('r').read().splitlines())
  for line in lines:
    if line == '':
      break
    label, intervals = line.split(': ')
    intervals = intervals.split(' or ')
    for i, v in enumerate(intervals):
      intervals[i] = tuple(int(n) for n in v.split('-'))
    intervals = tuple(intervals)
    categories[label] = intervals
  
  next(lines) # Consumes "your ticket:"
  myTicket = tuple(int(n) for n in next(lines).split(','))
  
  next(lines) # Consumes empty line
  next(lines) # Consumes "nearby tickets:"
  for line in lines:
    tickets.append(tuple(int(n) for n in line.split(',')))
  tickets = tuple(tickets)

  return {"categories" : categories, "myTicket" : myTicket, "tickets" : tickets}

def firstStar(input):
  intervals = tuple(i for cat in input['categories'].values() for i in cat)
  result = 0
  for ticket in input["tickets"]:
    for n in ticket:
      for i in intervals:
        if i[0] <= n <= i[1]:
          break
      else:
        result += n
  return result

def secondStar(input):
  intervals = tuple(i for cat in input['categories'].values() for i in cat)
  validTickets = []
  for ticket in input["tickets"]:
    isValid = True
    for n in ticket:
      for i in intervals:
        if i[0] <= n <= i[1]:
          break
      else:
        isValid = False
    if(isValid):
      validTickets.append(ticket)
  validTickets = tuple(validTickets)

  catCandidates = dict()
  allCandidates = list(range(len(input['myTicket'])))
  for cat in input['categories']:
    catCandidates[cat] = allCandidates.copy()

  for ticket in validTickets:
    for i, v in enumerate(ticket):
      for k, v2 in input['categories'].items():
        if i in catCandidates[k]:
          for interval in v2:
            if interval[0] <= v <= interval[1]:
              break
          else:
            catCandidates[k].remove(i)

  definedCats = dict()
  newFound = True
  while newFound:
    newFound = False
    for k, v in catCandidates.items():
      if len(v) == 1:
        newFound = True
        foundValue = v[0]
        definedCats[k] = foundValue
        for c in catCandidates.values():
          if foundValue in c:
            c.remove(foundValue)
  
  result = 1
  for k, v in definedCats.items():
    if 'departure' in k:
      result *= input['myTicket'][v]

  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 21071

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3429967441937
