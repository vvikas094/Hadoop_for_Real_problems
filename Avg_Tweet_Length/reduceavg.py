#!/usr/bin/env python
import sys
import string

prez_avg=0
others_avg=0
tweetcount=0
tweetcount2=0
sum1=0
sum2=0
preztw=list()
for line in sys.stdin:
        (key,val) = line.strip().split('\t',1)
        if key == 'PrezLength':
                preztw.append(int(val))
                sum1= sum1+int(val)
                tweetcount+=1
        if key == 'OthersLength':
                sum2 = sum2+int(val)
                tweetcount2+=1
if tweetcount== 0:
        prez_avg=0
else:
        prez_avg = float(sum1/tweetcount)
if tweetcount2!=0:        
    others_avg = float(sum2/tweetcount2)
print 'prez_average:%s\tothers_average:%s' % (prez_avg, others_avg)
print 'PrezOno tweet lengths: '
print preztw
print 'PrezOno max tweet length: %s' %max(preztw)
print 'PrezOno min tweet length: %s' %min(preztw)

