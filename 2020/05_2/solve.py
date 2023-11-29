from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def seatID(seat):
  row = 0
  column = 0
  for c in seat:
    if c in 'FB':
      row *= 2
      if c == 'B':
        row += 1
    else:
      column *= 2
      if c == 'R':
        column += 1
  return row*8 + column

def firstStar(input):
  result = 0
  for boardingPass in input:
    result = max(result, seatID(boardingPass))
  return result

def secondStar(input):
  seats = set()
  for boardingPass in input:
    seats.add(seatID(boardingPass))
  for seat in range(min(seats), max(seats)):
    if seat not in seats:
      return seat

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 922

print("The second star is : {}".format(secondStar(input)))
# The second star is : 747
