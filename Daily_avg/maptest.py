#!/usr/bin/env python
import sys
import string
import json
from datetime import datetime

def getUser(jsonData):
	if 'user' in jsonData:
		if jsonData["user"]["screen_name"]=="PrezOno":
			created=jsonData["created_at"]
			d= datetime.strptime(created,'%a %b %d  %H:%M:%S +0000 %Y')
			
			day=str(d.strftime('%a'))

                        fin=str(day)                                       
			print '%s\t%s'%(fin,1)




for line in sys.stdin:
	jsonData = json.loads(line)
	getUser(jsonData)
