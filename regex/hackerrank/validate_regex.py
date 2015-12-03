__author__ = 'rohitat'
import re
for _ in xrange(int(raw_input())):
    match = re.search(r'.*?[[\*][\+]]{0,1}.*',raw_input())
    if(match):
        print "False"
    else:
        print "True"