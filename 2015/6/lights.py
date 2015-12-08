#!/usr/bin/env python

import re

lights = [[False for i in range(1000)] for j in range(1000)]

def set( x, y, on ):
  lights[x][y] = on

def toggle( x, y ):
  set(x, y, not lights[x][y])

def set_range( xrange, yrange, on ):
  for x in xrange:
    for y in yrange:
      set(x, y, on)

def toggle_range( xrange, yrange ):
  for x in xrange:
    for y in yrange:
      toggle(x, y)

def command_set( line ):
  return 'turn' in line

def command_on( line ):
  return 'on' in line

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
    if command_set(line):
      set_range(xrange, yrange, command_on(line))
    else:
      toggle_range(xrange, yrange)

print sum(row.count(True) for row in lights) 
