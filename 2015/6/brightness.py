#!/usr/bin/env python

import re

lights = [[0 for i in range(1000)] for j in range(1000)]

def change_brightness( x, y, change ):
  lights[x][y] += change
  if lights[x][y] < 0:
    lights[x][y] = 0

def change_range( xrange, yrange, change ):
  for x in xrange:
    for y in yrange:
      change_brightness( x, y, change )

def get_ranges( line ):
  nums = re.findall(r'\d+', line)
  xrange = range(int(nums[0]), int(nums[2])+1)
  yrange = range(int(nums[1]), int(nums[3])+1)
  return [xrange, yrange]

with open('input') as f:
  for line in f:
    ranges = get_ranges(line)
    xrange = ranges[0]
    yrange = ranges[1]
    if 'toggle' in line:
      change_range( xrange, yrange, 2 )
    elif 'turn on' in line:
      change_range( xrange, yrange, 1 )
    else:
      change_range( xrange, yrange, -1 )

print sum(map(sum, lights))
