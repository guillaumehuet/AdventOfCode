def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  req = inputToRequisites(input)
  remaining = sorted(list({x[0] for x in req} | {x[1] for x in req}))
  seq = ""
  while remaining:
    for c in remaining:
      if c not in (x[1] for x in req):
        seq += c
        req = {x for x in req if x[0] != c}
        remaining.remove(c)
        break
  return seq

def inputToRequisites(input):
  result = set()
  for line in input:
    result.add((line[5], line[36]))
  return result

def secondStar(input):
  nWorker = 5
  tStep = 60
  seq = ""
  req = inputToRequisites(input)
  blocking = {x[0] for x in req}
  blocked = {x[1] for x in req}
  blockedBy = blockInfo(req)
  steps = dict.fromkeys(sorted(list(blocking | blocked)), 0)
  for k in blocked:
    steps[k] = -1
  # steps[X] = -1 if NOK to start
  # steps[X] =  0 if OK to start
  # steps[X] =  1 if started
  # steps[X] =  2 if finished
  workers = [["", 0] for _ in range(nWorker)]
  # workers[X] = [ "", _] for free worker
  # workers[X] = ["X", t] for worker working on task X with t seconds remaining
  tick = 0
  while True:
    for w in workers:
      if w[0] != '': # Go through every busy workers
        w[1] -= 1 # Advance through the task
        if w[1] <= 0: # If the task is over, free the worker and unblock corresponding tasks
          finishedTask = w[0]
          w[0] = ''
          seq += finishedTask
          steps[finishedTask] = 2
          for b in blockedBy:
            if finishedTask in blockedBy[b]:
              blockedBy[b].remove(finishedTask)
              if len(blockedBy[b]) <= 0:
                steps[b] = 0
          if(len(seq)) >= len(steps):
            return tick
    for w in workers:
      if w[0] == '': # Go through every free workers
        for k in steps.keys(): # assign next available task
          if steps[k] == 0:
            steps[k] = 1
            w[0] = k
            w[1] = tStep + ord(k) - ord('A') + 1
            break
    tick += 1

def blockInfo(req):
  blockedBy = dict()
  for (blocking, blocked) in req:
    if blocked in blockedBy:
      blockedBy[blocked].append(blocking)
    else:
      blockedBy[blocked] = [blocking]
  return blockedBy

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : JNOIKSYABEQRUVWXGTZFDMHLPC

print("The second star is : {}".format(secondStar(input)))
# The second star is : 1099
