'''https://stepik.org/lesson/24462/step/7?auth=registration&unit=6768'''

classes_dict = {}
run = int(input())
for i in range(run):
    class_parents = [i for i in input().split()]
    classes_dict[class_parents[0]] = class_parents[2:]
for i in classes_dict:
    key = classes_dict[i]  # предок
    value = classes_dict.get(i)  # потомки
    for j in value:
        if j in classes_dict:              # если предок(один из) в потомках(весь словарь)
            for z in classes_dict.get(j):  # для каждого потомка этого предка/потомка
                if z not in value:         # если он еще не в списке потомков основного
                    value.append(z)              # добавим его


run2 = int(input())
for i in range(run2):
    parent_check = [i for i in input().split()]
    parent = parent_check[1]
    child = parent_check[0]
    if parent in classes_dict:
        if child in classes_dict.get(parent) or child == parent:
            print('Yes')
        else:
            print('No')
    else:
        print('No')