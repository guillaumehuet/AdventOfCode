from pathlib import Path

def readInput(file):
  passportData = [dict()]
  for line in Path(__file__).with_name(file).open('r').read().splitlines():
    if len(line) == 0:
      passportData.append(dict())
    for fields in line.split():
      key, value = fields.split(':')
      passportData[-1][key] = value
  return passportData

def firstStar(input):
  required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
  result = 0
  for passport in input:
    for key in required:
      if key not in passport:
        break
    else:
      result += 1
  return result

def secondStar(input):
  required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
  result = 0
  for passport in input:
    for key in required:
      if key not in passport:
        break
      else:
        value = passport[key]
        if key[1:] == 'yr':
          if not value.isnumeric():
            break
          if key == 'byr':
            mini = 1920
            maxi = 2002
          elif key == 'iyr':
            mini = 2010
            maxi = 2020
          else:
            mini = 2020
            maxi = 2030
          value = int(value)
          if value < mini or value > maxi:
            break
        elif key == 'hgt':
          hgt = value[:-2]
          unit = value[-2:]
          if not hgt.isnumeric():
            break
          if unit == 'cm':
            mini = 150
            maxi = 193
          elif unit == 'in':
            mini = 59
            maxi = 76
          else:
            break
          hgt = int(hgt)
          if hgt < mini or hgt > maxi:
            break
        elif key == 'hcl':
          if value[0] != '#':
            break
          try:
            int(value[1:], 16)
          except ValueError:
            break
        elif key == 'ecl':
          if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            break
        else:
          if len(value) != 9:
            break
          if not value.isnumeric():
            break
    else:
      result += 1
  return result

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 235

print("The second star is : {}".format(secondStar(input)))
# The second star is : 194
