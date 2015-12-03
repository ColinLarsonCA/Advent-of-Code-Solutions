#!/usr/bin/env python

x = 0
y = 0
houses = set()
houses.add( (x, y) )
with open( "input" ) as f:
  while True:
    c = f.read(1)
    if not c:
      print len( set( houses ) )
      break
    if c == "<":
      x -= 1
    if c == ">":
      x += 1
    if c == "^":
      y += 1
    if c == "v":
      y -= 1
    houses.add( (x, y) )

