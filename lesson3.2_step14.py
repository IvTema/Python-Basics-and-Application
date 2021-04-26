'''https://stepik.org/lesson/24470/step/13'''
import sys
import re

pattern = r"\b(\w)(\w)([\w]*)\b"
change = r'\2\1\3'

for line in sys.stdin:
    line = line.rstrip()
    #test = re.findall(pattern, line)
    # print(test)
    finder = re.sub(pattern, change, line)
    print(finder)