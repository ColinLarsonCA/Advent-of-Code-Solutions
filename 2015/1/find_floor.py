#!/usr/bin/env python

floor=0
with open( "ff_input" ) as f:
  while True:
    c = f.read(1)
    if not c:
      print floor
      break
    if c == "(":
      floor += 1
    if c == ")":
      floor -= 1

