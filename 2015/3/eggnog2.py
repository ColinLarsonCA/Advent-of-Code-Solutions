#!/usr/bin/env python

move = 0
santas = ( [0, 0], [0, 0] )
houses = set()
houses.add( (0, 0) )
with open( "input" ) as f:
  while True:
    c = f.read(1)
    move += 1
    which_santa = move % 2
    if not c:
      print len( set( houses ) )
      break
    santa_pos = santas[which_santa]
    if c == "<":
      santa_pos[0] -= 1
    if c == ">":
      santa_pos[0] += 1
    if c == "^":
      santa_pos[1] += 1
    if c == "v":
      santa_pos[1] -= 1
    houses.add( tuple( santa_pos ) )

