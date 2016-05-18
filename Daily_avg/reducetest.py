#!/usr/bin/env python
import sys
import string

sunday_tweet=0
monday_tweet=0
tuesday_tweet=0
wednesday_tweet=0
thursday_tweet=0
friday_tweet=0
saturday_tweet=0
c_avg_sun=0.0
c_avg_mon=0.0
c_avg_tue=0.0
c_avg_wed=0.0
c_avg_thu=0.0
c_avg_fri=0.0
c_avg_sat=0.0

for line in sys.stdin:
	(key,val)=line.strip().split('\t',1)
	if key=='Sun':
		sunday_tweet+=1
	if key=='Mon':
		monday_tweet+=1
	if key=='Tue':
		tuesday_tweet+=1
        if key=='Wed':
		wednesday_tweet+=1
        if key=='Thu':
		thursday_tweet+=1
        if key=='Fri':
		friday_tweet+=1

        if key=='Sat':
		saturday_tweet+=1

c_avg_sun=float(sunday_tweet/52)
print 'Sunday avg:%s' %str(c_avg_sun)

c_avg_mon=float(monday_tweet/52)
print 'Monday avg:%s' %str(c_avg_mon)
c_avg_tue=float(tuesday_tweet/52)
print 'Tuesday avg:%s' %str(c_avg_tue)

c_avg_wed=float(wednesday_tweet/52)
print 'Wednesday avg:%s' %str(c_avg_wed)
c_avg_thu=float(thursday_tweet/52)
print 'Thursday avg:%s' %str(c_avg_thu)
c_avg_fri=float(friday_tweet/52)
print 'Friday avg:%s' %str(c_avg_fri)
c_avg_sat=float(saturday_tweet/52)
print 'Saturday avg:%s' %str(c_avg_sat)


max_avg=max(c_avg_sun,c_avg_mon,c_avg_tue,c_avg_wed,c_avg_thu,c_avg_fri,c_avg_sat)
if max_avg==c_avg_sun:
	print 'PrezOno tweet the most on Sunday'
if max_avg==c_avg_mon:
        print 'PrezOno tweet the most on Monday'
if max_avg==c_avg_tue:
        print 'PrezOno tweet the most on Tuesday'
if max_avg==c_avg_wed:
        print 'PrezOno tweet the most on Wednesday'
if max_avg==c_avg_thu:
        print 'PrezOno tweet the most on Thursday'
if max_avg==c_avg_fri:
        print 'PrezOno tweet the most on Friday'
if max_avg==c_avg_sat:
        print 'PrezOno tweet the most on Saturday'
print max_avg			
