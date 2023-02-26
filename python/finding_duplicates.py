my_list = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1]

duplicates = []

for i in my_list:
    if my_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

uniques = []
dup = []

for elm in my_list:
    if elm not in uniques:
        uniques.append(elm)
    elif elm not in dup:
        dup.append(elm)
print(dup)
