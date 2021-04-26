'''https://stepik.org/lesson/24470/step/13'''
import sys
import re

pattern = r"\b(a+)\b"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.sub(pattern, 'argh', line, 1, re.IGNORECASE)
    print(finder)
