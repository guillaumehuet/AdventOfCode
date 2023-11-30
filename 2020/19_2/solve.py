from pathlib import Path
import re

def readInput(file):
  rules = dict()
  messages = []
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if ':' in line:
      ruleN, rule = line.split(':')
      ruleN = int(ruleN)
      rule = rule.split('|')
      for i, r in enumerate(rule):
        rule[i] = [int(n) if n.isnumeric() else n[1:-1] for n in r.split(' ') if n != '']
      rules[ruleN] = rule
    elif line != '':
      messages.append(line)
  return {'rules': rules, 'messages' : messages}

def regexify(rules):
  regexes = dict()
  ruleProcessedDuringRound = True
  while(ruleProcessedDuringRound):
    ruleProcessedDuringRound = False
    for ruleN, rule in rules.items():
      if ruleN not in regexes:
        currRe = '(?:'
        processableRule = True
        for possibilities in rule:
          if not processableRule:
            break
          for subrule in possibilities:
            if type(subrule) == str:
              currRe += subrule
            elif subrule in regexes:
              currRe += regexes[subrule]
            else:
              processableRule = False
              break
          currRe += '|'
        currRe = currRe[:-1] + ')'
        if processableRule:
          regexes[ruleN] = currRe
          ruleProcessedDuringRound = True
  for i, r in regexes.items():
    regexes[i] = re.compile('^' + r + '$')
  return regexes

def checkMessages(messages, regex):
  result = []
  for m in messages:
    if regex.match(m):
      result.append(m)
  return result

def firstStar(input):
  r = regexify(input['rules'])[0]
  return len(checkMessages(input['messages'], r))

def secondStar(input):
  # r0 is r8 followed by r11
  # r8 is r42 or r42 followed by r8
  # => r8 is at least one repeat of r42 (r42)+
  # r11 is r42 followed by r31 or r42 followed by r11 followed by r31
  # => r11 is at least one repeat of r42 followed by the same amound of repeats of r31
  # => r0 is at least two repeats of r42 followed by a number of repeats of r31 lower than the repeats of r42
  # => We first match for the pattern (r42){2,}(r31)+, then for each result we count the number of r42 matches and check it is more than the r31s'
  r42 = regexify(input['rules'])[42].pattern[1:-1]
  r31 = regexify(input['rules'])[31].pattern[1:-1]
  r = '^(?:' + r42 + '{2,}' + r31 + '+' + ')$'
  r = re.compile(r)
  r42 = re.compile(r42)
  r31 = re.compile(r31)
  messages = checkMessages(input['messages'], r)
  result = 0
  for m in messages:
    n42 = 0
    n31 = 0
    match = True
    while match:
      match = r42.match(m)
      if match:
        n42 += 1
        m = m[match.end():]
    match = True
    while match:
      match = r31.match(m)
      if match:
        n31 += 1
        m = m[match.end():]
    if n42 > n31:
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 139

print("The second star is : {}".format(secondStar(input)))
# The second star is : 289
