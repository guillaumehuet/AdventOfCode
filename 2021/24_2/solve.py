from pathlib import Path

def readInput(file):
  result = []
  for l, line in enumerate(Path(__file__).with_name(file).open('r').read().splitlines()):
    if l%18 == 0:
      if len(result) > 0:
        result[-1] = tuple(result[-1])
      result.append([])
    if l%18 in (4, 5, 15):
      result[-1].append(int(line.split()[-1]))
  result[-1] = tuple(result[-1])
  return tuple(result)

def reverseMonad(parameters, minimize = False):
  # n is the round number, zn is the value of z at the start of the round, dn is the digit being checked during the round, n in [0..13]
  # p0n, p1n, p2n are respectively the first, second and third value exported from the input for the nth round
  # Let's consider the value of zn after each round :
  # First, some assumptions from the structure of the input, for all n : (TODO : Add Checks)
    # p0n in {1, 26}
    # p0n is half the time 1, half the time 26
    # p0n == 1 <=> p1n >= 10
    # p0n == 26 <=> p1n < 0
    # 0 <= p2n <= 16
  p0nEquilibrium = 0
  for p in parameters:
    if not ((p[0] == 1 and p[1] >= 10) or (p[0] == 26 and p[1] < 0)):
      raise "Case not implemented"
    if p[0] == 26:
      p0nEquilibrium += 1
    else:
      p0nEquilibrium -= 1
  if p0nEquilibrium != 0:
    raise "Case not implemented"
  
  # Let's consider zn as a number in base 26
  # The condition would translate as : take last base 26 digit of zn, add to it p1n, test if equal to dn
  # When p0n == 1, p1n >= 10
    # The condition would auto-fail because even if zn%26 was zero (can never be negative by definition of %), since dn is in [1..9], it could never match
    # In this case : z(n + 1) = 26*int(zn/p0n) + dn + p2n = 26*int(zn/1) + dn + p2n = 26*zn + dn + p2n. Since dn in [1..9] and p2n in [0..16], dn + p2n in [1..25], 0 < dn + p2n < 26
    # This would correspond to shifting the digits in zn left once (26*zn) and adding a new unit number dn + p2n (because it is positive and less than the base)
    # Moreover this number can never be 0, it is strictly positive
  # When p0n == 26, p1n < 0 :
    # The condition could succeed if and only if the last base 26 digit of zn, let's call it zn0, is such that zn0 + p1n == dn. This is possible because p1n < 0 in this case and zn0 is positive.
    # If it succeeds:
      # z(n + 1) = int(zn/p0n) = int(zn/26)
      # This would correspond to shifting the digits in zn right once (int(zn/26)), dropping zn0
    # If it fails:
      # z(n + 1) = 26*int(zn/p0n) + dn + p2n = 26*int(zn/26) + dn + p2n. Since dn in [1..9] and p2n in [0..16], dn + p2n in [1..25], 0 < dn + p2n < 26
      # This would correspond to shifting the digits in zn right once (int(zn/26)), dropping zn0, then shifting them back left once (26*[]) and adding a new unit number dn + p2n (because it is positive and less than the base)
      # This would actually replace zn0 with dn + p2n in the base 26 representation of zn
  # We need z13, the output at the end of the last round to be 0, which is still 0 in base 26, meaning it's size in digits is 0
  # Everytime the condition fails zn either grows by one digit or stays the same size and everytime the condition succeeds it shrinks by one digit
  # Since it starts at size 0, must grow by 1 half the time (when p0n == 1), it must shrink by 1 the remainding of the time (when p0n == 26) to be able to shrink back to size 0
  # This means the condition must suceed everytime p0n == 26 to shrink back to size 0.
  # The condition succeeds if, for j the digit corresponding to the unit in the base 26 digit of dn == dj + p2j + p1n.
  # Let's keep a dictionnary of the concerned n with the corresponding j and (p2j + p1n)
  # This fixes conditions on the digits, but for example if we have dn = dj + 8, we can't set dn = 9 and get a dj = 17 since it must be in [1..9]
  # For the maximize case, we will transform the dictionnary to have only negative or zero added value, this will let us define every digits not in the dictionnary as 9 and calculate the others
  # For the minimize case, we will transform the dictionnary to have only positive or zero added value, this will let us define every digits not in the dictionnary as 9 and calculate the others

  deltaDn = dict()
  z_26 = []
  for i, p in enumerate(parameters):
    if p[0] == 1:
      z_26.append((i, p[2]))
    else:
      j, p2j = z_26.pop()
      added = p[1] + p2j
      if (minimize != (added > 0)):
        deltaDn[j] = (i, -added)
      else:
        deltaDn[i] = (j, added)
  
  result = 0
  for i in range(len(parameters)):
    if minimize:
      d = 1
    else:
      d = 9
    if i in deltaDn:
      d += deltaDn[i][1]
    result *= 10
    result += d

  return result

def firstStar(input):
  return reverseMonad(input)

def secondStar(input):
  return reverseMonad(input, minimize=True)

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 99995969919326

print("The second star is : {}".format(secondStar(input)))
# The second star is : 48111514719111
