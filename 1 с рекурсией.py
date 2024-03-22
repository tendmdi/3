def recursive(list1, list2, index1=0, index2=0, intersection=[]):
    if index1 < len(list1) and index2 < len(list2):
        if list1[index1] == list2[index2]:
            intersection.append(list1[index1])
            return recursive(list1, list2, index1+1, index2+1, intersection)
        elif list1[index1] < list2[index2]:
            return recursive(list1, list2, index1+1, index2, intersection)
        else:
            return recursive(list1, list2, index1, index2+1, intersection)
    return intersection

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 6, 8]
print(recursive(list1, list2))  

