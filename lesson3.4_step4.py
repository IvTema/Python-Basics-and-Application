'''https://stepik.org/lesson/24473/step/4'''
import json
import operator

run = input()
classes_dict = json.loads(run)
counter = len(classes_dict)
child_dict = {}
final_dict = {}
all_items = set()
for i in range(counter):
    key = classes_dict[i]['name']  # потомок
    value = classes_dict[i]['parents']  # предки
    child_dict[key] = value
for i in child_dict:
    value1 = child_dict.get(i)
    for j in value1:
        if j in child_dict:              # если предок(один из) в потомках(весь словарь)
            for z in child_dict.get(j):  # для каждого потомка этого предка/потомка
                if z not in value1:         # если он еще не в списке потомков основного
                    value1.append(z)              # добавим его

for k in child_dict:            # заполняем словарь final_dict предок : потомки
    all_items.add(k)            # + множество со всеми элементами словаря
    for z in child_dict[k]:
        all_items.add(z)
        if z not in final_dict:
            final_dict[z] = [k]
        else:
            final_dict[z].append(k)

for p in all_items:              # добавляем в словарь final_dict самонаследование
    if p not in final_dict:
        final_dict[p] = [p]
    else:
        final_dict[p].append(p)

sorted_tuples = sorted(final_dict.items(), key=operator.itemgetter(0))
sorted_final_dict = {k: v for k, v in sorted_tuples}
for y, x in sorted_final_dict.items():
    print(y, ":", len(x))