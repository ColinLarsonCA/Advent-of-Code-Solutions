#!/usr/bin/env python

total = 0
with open( "input" ) as f:
  for line in f:
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    sorted_dimensions = sorted( map( int, dimensions ) )
    short = sorted_dimensions[1]
    shortest = sorted_dimensions[0]
    distance_around = shortest + shortest + short + short
    volume = length * width * height
    total += distance_around + volume

print total 
