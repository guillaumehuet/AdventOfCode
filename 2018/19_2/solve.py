def sumOfDivisorsOptimized(n):
  return sum(i for i in range(1, n + 1) if not n % i)

def firstStar(input):
  return sumOfDivisorsOptimized(896)

def secondStar(input):
  return sumOfDivisorsOptimized(10551296)

print("The first star is : {}".format(firstStar(input)))
# The first star is : 2040

print("The second star is : {}".format(secondStar(input)))
# The second star is : 25165632
