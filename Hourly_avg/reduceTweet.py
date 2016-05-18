#!/usr/bin/env python

import sys
import string

hour_count = 0
hour = None

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if hour != key:
    if hour:
      print '%s\t%s' % (hour, hour_count)
      hour_count = 0
  hour = key
  try:
    hour_count = hour_count + int(val)
  except:
    continue
print '%s\t%s' % (hour, hour_count)
