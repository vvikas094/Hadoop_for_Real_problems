#!/usr/bin/env python

import sys

file =  open("cloudresults.txt", 'r')
data = file.read().splitlines()

counter = 0

for line in data:
    (key,val) = line.strip().split('\t',1)
    if ((key == 'Errors') or (key == 'Success') or (key == 'Total Tweets')):
      continue
    try:
        int(key)
    except:
        counter = counter + 1
        continue

for line in data:
    (key,val) = line.strip().split('\t',1)
    if ((key == 'Errors') or (key == 'Success') or (key == 'Total Tweets')):
      print '%s,%s' % (key, val)
      continue
    try:
        int(key)
        from decimal import *
        val2 = Decimal((Decimal(val) / Decimal(counter)))
        print '%s,%s,%s' % (key, val, val2)
    except:
        continue

print '%s,%s' % ('Days Tweeted', counter)
