def readInput(file):
  blueprints = []
  for line in open(file).read().splitlines():
    line = line.split()
    oreForOreRobot = int(line[6])
    oreForClayRobot = int(line[12])
    oreForObsidianRobot = int(line[18])
    clayForObsidianRobot = int(line[21])
    oreForGeodeRobot = int(line[27])
    obsidianForGeodeRobot = int(line[30])
    blueprints.append(((oreForOreRobot, 0, 0, 0), (oreForClayRobot, 0, 0, 0), (oreForObsidianRobot, clayForObsidianRobot, 0, 0), (oreForGeodeRobot, 0, obsidianForGeodeRobot, 0)))
  return tuple(blueprints)

def computeScore(step, resources, robots, maxStep):
  idleResources = tuple(reversed([r_i + rob_i*(maxStep - step) for r_i, rob_i in zip(resources, robots)]))
  return idleResources

def neighboors(position, blueprint, maxCost, maxStep):
  score, step, resources, robots = position
  newStep = step + 1
  newResources = tuple(r_i + rob_i for r_i, rob_i in zip(resources, robots))
  newScore = computeScore(newStep, newResources, robots, maxStep)
  result = [(newScore, newStep, newResources, robots)]
  for robotId, cost in enumerate(blueprint):
    if robotId < 3 and maxCost[robotId] <= robots[robotId]:
      continue
    if all(c_i <= r_i for c_i, r_i in zip(cost, resources)):
      newResources = tuple(r_i + rob_i - c_i for r_i, rob_i, c_i in zip(resources, robots, cost))
      newRobots = tuple(r + 1 if i == robotId else r for i, r in enumerate(robots))
      newScore = computeScore(newStep, newResources, newRobots, maxStep)
      result.append((newScore, newStep, newResources, newRobots))
  return result

def firstStar(input):
  maxStep = 24
  prevStep = 0
  limitSearch = 100 # Increase if the result is too low, the larger the limit, the most precise but the slowest
  result = 0
  for i, blueprint in enumerate(input):
    currResult = 0
    step = 0
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)
    score = computeScore(step, resources, robots, maxStep)
    position = (score, step, resources, robots)
    maxCost = tuple(max(cost) for cost in zip(*blueprint))
    boundary = neighboors(position, blueprint, maxCost, maxStep)
    boundarySet = set(boundary)
    while boundary:
      position = boundary.pop(0)
      boundarySet.remove(position)
      score, step, resources, robots = position
      if prevStep != step:
        boundary = [position] + boundary
        boundary.sort(reverse=True)
        boundary = boundary[:limitSearch]
        boundarySet = set(boundary)
        prevStep = step
        continue
      if step >= maxStep:
        currResult = max(currResult, resources[-1])
      else:
        for neighboor in neighboors(position, blueprint, maxCost, maxStep):
          if neighboor not in boundarySet:
            boundary.append(neighboor)
            boundarySet.add(neighboor)
    result += currResult*(i + 1)
  return result

def secondStar(input):
  maxStep = 32
  prevStep = 0
  limitSearch = 100 # Increase if the result is too low, the larger the limit, the most precise but the slowest
  result = 1
  input = input[:3]
  for i, blueprint in enumerate(input):
    currResult = 0
    step = 0
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)
    score = computeScore(step, resources, robots, maxStep)
    position = (score, step, resources, robots)
    maxCost = tuple(max(cost) for cost in zip(*blueprint))
    boundary = neighboors(position, blueprint, maxCost, maxStep)
    boundarySet = set(boundary)
    while boundary:
      position = boundary.pop(0)
      boundarySet.remove(position)
      score, step, resources, robots = position
      if prevStep != step:
        boundary = [position] + boundary
        boundary.sort(reverse=True)
        boundary = boundary[:limitSearch]
        boundarySet = set(boundary)
        prevStep = step
        continue
      if step >= maxStep:
        currResult = max(currResult, resources[-1])
      else:
        for neighboor in neighboors(position, blueprint, maxCost, maxStep):
          if neighboor not in boundarySet:
            boundary.append(neighboor)
            boundarySet.add(neighboor)
    result *= currResult
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 1389

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3003
