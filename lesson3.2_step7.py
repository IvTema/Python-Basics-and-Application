'''https://stepik.org/lesson/24470/step/7'''
import sys
import re

pattern = r"(cat)"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.findall(pattern, line)
    if len(finder) > 1:
        print(line)