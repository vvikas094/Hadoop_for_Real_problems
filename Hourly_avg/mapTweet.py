#!/usr/bin/env python

import sys
import string
import json
import time

errors = 0
successes = 0
tweets = 0

def timeConvert(rawDateTime):
    parseTime = time.strptime(rawDateTime,'%a %b %d %H:%M:%S +0000 %Y')
    extractHour = time.strftime('%H', parseTime)
    return extractHour
    
def dateConvert(rawDateTime):
    parseTime = time.strptime(rawDateTime,'%a %b %d %H:%M:%S +0000 %Y')
    extractDate = time.strftime('%b %d %Y', parseTime)
    return extractDate
    
for line in sys.stdin:
    tweets += 1
    try:
        json_str = json.loads(line)
        if ((json_str['user']['screen_name'] == 'PrezOno') or (json_str['user']['id'] == 211178363)):
            print '%s\t%s' % (timeConvert(json_str['created_at']), 1)
    except:
        errors += 1
        continue    
    successes +=1
    print '%s\t%s' % (dateConvert(json_str['created_at']), 1)

print '%s\t%s' % ('Success', successes)
print '%s\t%s' % ('Errors', errors)
print '%s\t%s' % ('Total Tweets', tweets)
