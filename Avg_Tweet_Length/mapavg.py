#!/usr/bin/env python
import sys
import string
import json
#sums = 0
#sums2 = 0
for line in sys.stdin:
    jsonData = json.loads(line)
    if 'user' in jsonData:
        if jsonData["user"]["screen_name"] == "PrezOno":
                created=jsonData["text"]
                print 'PrezLength\t%s' %(len(created))

        else:
                created2=jsonData["text"]
                print 'OthersLength\t%s' %(len(created2))


   # print 'PrezSum\t%s' %sums
   # print 'OthersSum\t%s' %sums2       

