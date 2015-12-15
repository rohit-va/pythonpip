__author__ = 'rohitat'
import re
s = raw_input()
match = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)
if match:
    for i in match:
        print i
else:
    print "-1"
