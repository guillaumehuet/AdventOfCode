import re
from collections import defaultdict

def gan(s):
  return list(map(int, re.findall(r'-?\d+', s)))
def lenr(l):
  return range(len(l))
d = '''pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1'''.split('\n')
d = '''pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5'''.split('\n')
d = open('input').readlines()
nanobots = list(map(gan, d))
nanobots = [((n[0], n[1], n[2]), n[3]) for n in nanobots]

def dist(pos, npos):
  return abs(pos[0]-npos[0]) + abs(pos[1]-npos[1]) + abs(pos[2]-npos[2])

srad = 0
rad_idx = 0
in_range = defaultdict(int)
for i in lenr(nanobots):
  pos, rng = nanobots[i]
  strength = 0
  if rng > srad:
    srad = rng
    rad_idx = i
    for j in lenr(nanobots):
      npos, _ = nanobots[j]
      if dist(pos, npos) <= rng:
        in_range[i] += 1

print("a", in_range[rad_idx])

from z3 import *
def zabs(x):
  return If(x >= 0,x,-x)
(x, y, z) = (Int('x'), Int('y'), Int('z'))
in_ranges = [
  Int('in_range_' + str(i)) for i in lenr(nanobots)
]
range_count = Int('sum')
o = Optimize()
for i in lenr(nanobots):
  (nx, ny, nz), nrng = nanobots[i]
  o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nrng, 1, 0))
o.add(range_count == sum(in_ranges))
dist_from_zero = Int('dist')
o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
print(o.check())
#print o.lower(h1)
#print o.upper(h1)
print("b", o.lower(h2), o.upper(h2))
#print o.model()[x]
#print o.model()[y]
#print o.model()[z]
