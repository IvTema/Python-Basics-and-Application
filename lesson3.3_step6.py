'''https://stepik.org/lesson/24471/step/6'''
import requests
import re


def checker(A, B):
    pattern = r'\b(https.*html)\b'
    res = requests.get(A)
    if into_checker(A, B, pattern, res) is True:
        print('Yes')
    else:
        print('No')


def into_checker(A, B, pattern, res):
    for i in re.findall(pattern, res.text):
        res1 = requests.get(i)
        if B in res1.text:
            return True


checker(input(), input())