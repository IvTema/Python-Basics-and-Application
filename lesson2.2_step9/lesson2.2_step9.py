'''https://stepik.org/lesson/24466/step/9?unit=6773'''
from simplecrypt import decrypt, DecryptionException


with open("lesson2.2_step9/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("lesson2.2_step9/passwords.txt", "r") as inf:
    for line in inf:
        try:
            password = line.strip()
            plaintext = decrypt(password, encrypted)
            print(plaintext.decode("utf-8"))
        except DecryptionException:
            pass
