# -*- coding:utf-8 -*-
import re
f=open('tweet_stream.txt','r')
icount=0
scount=0
lcount=0
xcount=0
for a in f:
	if bool(re.search(u'Sat',a)):
		icount+=1
	elif bool(re.search(u'Sun',a)):
		scount+=1
	elif bool(re.search(u'Mon',a)):
		lcount+=1
	elif bool(re.search(u'Tue',a)):
		xcount+=1	
print u'요일별 사랑 언급 빈도 분석'
print u'토요일 언급횟수:'+ str(icount) +icount/10*'#'
print u'일요일 언급횟수:'+ str(scount)	+scount/10*'#'	
print u'월요일 언급횟수:'+ str(lcount) +lcount/10*'#'
print u'화요일 언급횟수:'+ str(xcount) +xcount/10*'#'	
