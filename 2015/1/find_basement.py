#!/usr/bin/env python

pos=0
floor=0
with open( "ff_input" ) as f:
  while True:
    c = f.read(1)
    pos += 1
    if not c:
      print "Santa never entered the basement!"
      break
    if c == "(":
      floor += 1
    if c == ")":
      floor -= 1

    if floor < 0:
      print pos
      break
