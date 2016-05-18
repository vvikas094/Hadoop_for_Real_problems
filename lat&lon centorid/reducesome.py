#!/usr/bin/python
import sys
import string
import json

lats_sum = 0
longs_sum = 0
coord_count = float(0)
total_count = float(0)
result = {}
# reducer to calculate centroid and poportion of location
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  # converting string to a json
  coordsD = json.loads(val)
  lats_sum += float(coordsD["lat"])
  longs_sum += float(coordsD["long"])
  coord_count += float(coordsD["yes"])
  total_count += 1
cLatLong = (0, 0)
if coord_count:
  cLatLong = (lats_sum/float(coord_count), longs_sum/float(coord_count))  
result['centroid'] = cLatLong
# calcuate proportion of tweets with location to without = count(tweets without location) / count(tweets with location)
result['proportionOfCoordsToNoCoords'] = ((total_count - coord_count)/coord_count)
# print the centroid and proportion
print 'result\t%s' % json.dumps(result)
