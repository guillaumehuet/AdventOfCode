gridSize = 300

def firstStar(input):
  grid = inputToGrid(input)
  return str(maxCell(grid, 3)[0][:2])[1:-1].replace(' ', '')

def secondStar(input):
  grid = inputToGrid(input)
  maxValue = 0
  maxIndex = (0, 0, 0)
  for z in range(gridSize):
    index, value = maxCell(grid, z)
    if value > maxValue:
      maxIndex = index
      maxValue = value
  return str(maxIndex)[1:-1].replace(' ', '')

def inputToGrid(input):
  grid = [[0 for _ in range(gridSize + 1)] for _ in range(gridSize + 1)]
  for y in range(1, len(grid)):
    for x in range(1, len(grid[0])):
      grid[y][x] = cellToPower(x - 1, y - 1, input) + grid[y][x - 1] + grid[y - 1][x] - grid[y - 1][x - 1]
  return grid

def cellToPower(x, y, serial):
  # Find the fuel cell's rack ID, which is its X coordinate plus 10.
  rackID = x + 10
  # Begin with a power level of the rack ID times the Y coordinate.
  result = rackID*y
  # Increase the power level by the value of the grid serial number (your puzzle input).
  result += serial
  # Set the power level to itself multiplied by the rack ID.
  result *= rackID
  # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
  result //= 100
  result %= 10
  # Subtract 5 from the power level.
  result -= 5
  return result

def maxCell(grid, size):
  maxValue = 0
  maxIndex = (0, 0, size)
  for y in range(len(grid) - size):
    for x in range(len(grid[0]) - size):
      value = grid[y + size][x + size] - grid[y + size][x] - grid[y][x + size] + grid[y][x]
      if value > maxValue:
        maxIndex = (x, y, size)
        maxValue = value
  return maxIndex, maxValue

input = 6878

print("The first star is : {}".format(firstStar(input)))
# The first star is : 20,34

print("The second star is : {}".format(secondStar(input)))
# The second star is : 90,57,15
