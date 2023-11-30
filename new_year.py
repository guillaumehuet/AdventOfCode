from pathlib import Path
from datetime import date

currYear = str(date.today().year)
inputYear = input("What year folder hierarchy do you want to initialize ({}) ? ".format(currYear)) or currYear
yearPath = Path(__file__).with_name(inputYear)

if yearPath.exists() and (input("Folder {} exists, are you sure you want to overwrite it and all its subfolders (Y/N) ?".format(yearPath)) not in ("y","Y")):
    exit()

yearPath.mkdir()

defautSolvePy = """from pathlib import Path

def readInput(file):
  return Path(__file__).with_name(file).open('r').read().splitlines()

def firstStar(input):
  pass

def secondStar(input):
  pass

input = readInput('input')

print("The first star is : {}".format(firstStar(input)))
# The first star is : 

print("The second star is : {}".format(secondStar(input)))
# The second star is : 
"""

for day in range(1,26):
    dayPath = yearPath / "{:02d}_0".format(day)
    dayPath.mkdir()
    (dayPath / "input").touch()
    (dayPath / "rules.txt").touch()
    (dayPath / "solve.py").open('w').write(defautSolvePy)
