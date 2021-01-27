a = int(input())
all_parents = {}                        # словарь потомок:родитель
for i in range(a):
    error_name = [i for i in input().split()]
    if error_name[0] not in all_parents:
        all_parents[error_name[0]] = []
    if len(error_name) > 1:
        for j in error_name[2:]:
            all_parents[error_name[0]].append(j)
            if j in all_parents:
                for p in all_parents.get(j):
                    if p not in all_parents.get(error_name[0]):
                        all_parents[error_name[0]].append(p)
    for z in all_parents:
        if error_name[0] in all_parents.get(z):
            for h in all_parents.get(error_name[0]):
                if h not in all_parents.get(z):
                    all_parents.get(z).append(h)
#print(all_parents)

b = int(input())
exceptions = []
out = []
for i in range(b):
    exceptions += [i for i in input().split()]
#print(exceptions)
for j in exceptions:                                           # j - потенциальный потомок
    if j not in out:
        if j in all_parents:
            for p in exceptions[:(exceptions.index(j))]:
                if p in all_parents.get(j) and j not in out:   # p - потенциальный родитель
                    out.append(j)

for z in out:
    print(z)