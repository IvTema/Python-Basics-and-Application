'''https://stepik.org/lesson/24470/step/15'''
import sys
import re

pattern = r"(\w)(\1*)"
change = r'\1'

for line in sys.stdin:
    line = line.rstrip()
    #test = re.findall(pattern, line)
    #print(test)
    finder = re.sub(pattern, change, line)
    print(finder)