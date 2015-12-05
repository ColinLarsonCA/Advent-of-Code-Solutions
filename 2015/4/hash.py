#!/usr/bin/env python
import hashlib

orig_hash = hashlib.md5()
orig_hash.update('iwrupvqb')

i = 1
while True:
  new_hash = orig_hash.copy()
  new_hash.update(str(i))
  hash_str = new_hash.hexdigest()
  if hash_str.startswith('00000'):
    print i
    break
  i += 1
