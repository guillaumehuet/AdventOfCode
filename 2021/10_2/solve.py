from statistics import median

def readInput(file):
  return open(file).read().splitlines()

def firstStar(input):
  score = 0
  for line in input:
    reduced = ""
    for c in line:
      if c in '([{<':
        reduced += c
      else:
        if c == ')':
          if reduced[-1] == '(':
            reduced = reduced[:-1]
          else:
            score += 3
            break
        if c == ']':
          if reduced[-1] == '[':
            reduced = reduced[:-1]
          else:
            score += 57
            break
        if c == '}':
          if reduced[-1] == '{':
            reduced = reduced[:-1]
          else:
            score += 1197
            break
        if c == '>':
          if reduced[-1] == '<':
            reduced = reduced[:-1]
          else:
            score += 25137
            break
  return score

def secondStar(input):
  scores = []
  for line in input:
    reduced = ""
    for c in line:
      if c in '([{<':
        reduced += c
      else:
        if c == ')':
          if reduced[-1] == '(':
            reduced = reduced[:-1]
          else:
            break
        if c == ']':
          if reduced[-1] == '[':
            reduced = reduced[:-1]
          else:
            break
        if c == '}':
          if reduced[-1] == '{':
            reduced = reduced[:-1]
          else:
            break
        if c == '>':
          if reduced[-1] == '<':
            reduced = reduced[:-1]
          else:
            break
    else:
      score = 0
      for c in reversed(reduced):
        score *= 5
        if c == '(':
          score += 1
        elif c == '[':
          score += 2
        elif c == '{':
          score += 3
        elif c == '<':
          score += 4
      scores.append(score)
  return median(scores)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 278475

print("The second star is : {}".format(secondStar(input)))
# The second star is : 3015539998
