#!/usr/bin/env python

from itertools import izip, islice

vowels = ['a', 'e', 'i', 'o', 'u']
naughty_phrases = ['ab', 'cd', 'pq', 'xy']

def lock_step_line( line, num_characters ):
  slices = []
  for index in range(num_characters):
    slices.append( islice(line, index, None) )
  return izip( *slices )

def is_nice( line ):
  num_vowels = 0
  has_repeat = False
  for (cursor, peek) in lock_step_line(line, 2):
    if cursor in vowels:
      num_vowels += 1
    if cursor is peek:
      has_repeat = True
    if ''.join((cursor, peek)) in naughty_phrases:
      return False
  return num_vowels >= 3 and has_repeat

num_nice = 0
with open( 'input' ) as f:
  for line in f:
    if is_nice( line ):
      num_nice += 1
print num_nice

