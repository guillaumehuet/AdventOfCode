from pathlib import Path

def readInput(file):
  result = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    result.append(tuple(int(n) for n in line.split()))
  return tuple(result)

def validateReport(report):
  sign  = (report[1] - report[0])
  if sign == 0:
    return False
  sign = sign // abs(sign)
  for i in range(len(report) - 1):
    dist = report[i + 1] - report[i]
    if sign*dist < 1:
      return False
    if sign*dist > 3:
      return False
  return True

def firstStar(input):
  result = 0
  for report in input:
    if validateReport(report):
      result += 1
  return result

def secondStar(input):
  result = 0
  for report in input:
    if validateReport(report):
      result += 1
    else:
      for i in range(len(report)):
        if validateReport(report[:i] + report[i + 1:]):
          result += 1
          break
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 559

print("The second star is : {}".format(secondStar(input)))
# The second star is : 601
