#Muhammad Hamza Farooq
#200901019

import threading
#---------------------------------------------------------#
def list_merge(mylist, list1, list2, list3):
    size1 = list2 - list1 + 1
    size2 = list3 - list2
    arr1 = [0] * size1
    arr2 = [0] * size2

    for i in range(0, size1):
        arr1[i] = mylist[list1 + i]

    for j in range(0, size2):
        arr2[j] = mylist[list2 + 1 + j]
    i = 0 
    j = 0  
    arr3 = list1 
    while i < size1 and j < size2:
        if arr1[i] <= arr2[j]:
            mylist[arr3] = arr1[i]
            i += 1
        else:
            mylist[arr3] = arr2[j]
            j += 1
        arr3 += 1
    while i < size1:
        mylist[arr3] = arr1[i]
        i += 1
        arr3 += 1
    while j < size2:
        mylist[arr3] = arr2[j]
        j += 1
        arr3 += 1

def merge_sorting(mylist, list1, list3):
    if list1 < list3:
        list2 = (list1 + (list3 - 1))//2
        t1 = threading.Thread(target=merge_sorting, args=(mylist, list1, list2))
        t2 = threading.Thread(target=merge_sorting, args=(mylist, list2 + 1, list3))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        list_merge(mylist, list1, list2, list3)

mylist = [16, 14, 23, 2, 21, 6, 3,5]
merge_sorting(mylist, 0, len(mylist) - 1)
print("\n \nFollowing is the merged sorted List: ")
print(mylist)