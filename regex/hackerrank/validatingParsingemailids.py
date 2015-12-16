__author__ = 'rohitat'
import re
eng = 'a-zA-Z'
for i in xrange(int(raw_input())):
        name, emailID = raw_input().split()
        if(re.search(r'\<['+eng+'][\w\-\.]*\@['+eng+']+\.['+eng+']{,3}\>',emailID)):
            print name, emailID

