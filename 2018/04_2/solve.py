def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  shifts = splitShifts(input)
  guardShifts = dict()
  guardPerfs = dict()
  for shift in shifts:
    processedShift = processShift(shift)
    guard = processedShift[0]
    if guard in guardShifts:
      guardShifts[guard] += processedShift[1:]
    else:
      guardShifts[guard] = processedShift[1:]
  for guard in guardShifts:
    guardPerfs[guard] = processGuardShift(guardShifts[guard])
  bestGuard = findBestGuard(guardPerfs, 0)
  return bestGuard*guardPerfs[bestGuard][1]

def splitShifts(log):
  shifts = []
  for l in sorted(input):
    if 'Guard' in l:
      shifts.append([])
    shifts[-1].append(l)
  return shifts

def processShift(shift):
  guard = int(shift[0].split()[3][1:])
  asleep = False
  result = [guard]
  for l in shift[1:]:
    minute = int(l.split()[1].split(':')[1][:-1])
    asleep = not asleep
    if asleep:
      minAsleep = minute
    else:
      result.append([minAsleep, minute])
  return result

def processGuardShift(shift):
  total = 0
  minState = [0 for _ in range(60)]
  for sleep in shift:
    total += sleep[1] - sleep[0]
    for m in range(sleep[0], sleep[1]):
      minState[m] += 1
  bestMin = 0
  bestMinState = 0
  for m in range(len(minState)):
    if minState[m] > bestMinState:
      bestMin = m
      bestMinState = minState[m]
  return total, bestMin, bestMinState

def findBestGuard(guardPerfs, perfNum):
  bestGuard = None
  bestPerf = 0
  for guard in guardPerfs:
    if guardPerfs[guard][perfNum] > bestPerf:
      bestGuard = guard
      bestPerf = guardPerfs[guard][perfNum]
  return bestGuard

def secondStar(input):
  shifts = splitShifts(input)
  guardShifts = dict()
  guardPerfs = dict()
  for shift in shifts:
    processedShift = processShift(shift)
    guard = processedShift[0]
    if guard in guardShifts:
      guardShifts[guard] += processedShift[1:]
    else:
      guardShifts[guard] = processedShift[1:]
  for guard in guardShifts:
    guardPerfs[guard] = processGuardShift(guardShifts[guard])
  bestGuard = findBestGuard(guardPerfs, 2)
  return bestGuard*guardPerfs[bestGuard][1]

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 99911

print("The second star is : {}".format(secondStar(input)))
# The second star is : 65854
