'''stepik.org/lesson/24473/step/2'''
import csv

time = []
crime_dict = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        time = int(row[2][6:10])
        if time == 2015:
            if row[5] not in crime_dict:
                crime_dict[row[5]] = 1
            else:
                crime_dict[row[5]] += 1
sorted_dict = {}
sorted_keys = sorted(crime_dict, key=crime_dict.get)
print(sorted_keys[-1])