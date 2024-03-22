def intersect(list1, list2):
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, 4]
list2 = [2, 3, 6, 8]
print(intersect(list1, list2))
