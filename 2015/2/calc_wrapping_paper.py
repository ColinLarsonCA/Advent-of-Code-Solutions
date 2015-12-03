#!/usr/bin/env python

total = 0
with open( "input" ) as f:
  for line in f:
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    lw = length * width
    wh = width * height
    hl = height * length
    surface_area = 2*lw + 2*wh + 2*hl
    extra = min( lw, wh, hl )
    total += surface_area + extra

print total
