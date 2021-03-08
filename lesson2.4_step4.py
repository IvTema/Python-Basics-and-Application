'''https://stepik.org/lesson/24465/step/4?auth=registration&unit=6772'''
with open("dataset_old.txt", 'r') as old, open("dataset_new.txt", 'w') as new:
    new.writelines((old.readlines()[::-1]))