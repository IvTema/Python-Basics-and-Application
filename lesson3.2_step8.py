'''https://stepik.org/lesson/24470/step/8'''
import sys
import re

pattern = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.search(pattern, line)
    if finder:
        print(line)