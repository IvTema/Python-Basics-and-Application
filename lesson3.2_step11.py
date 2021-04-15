'''https://stepik.org/lesson/24470/step/11'''
import sys
import re

pattern = r"\b(\w+)\1\b"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.search(pattern, line)
    if finder:
        print(line)