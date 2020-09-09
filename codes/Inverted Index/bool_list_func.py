def List_AND(list1,list2):

    ptr1 = 0
    ptr2 = 0
    and_list = []

    while ptr1<len(list1) and ptr2<len(list2):
        if list1[ptr1] == list2[ptr2]:
            and_list.append(list1[ptr1])
            ptr1+=1
            ptr2+=1
        elif list1[ptr1] < list2[ptr2]:
            ptr1+=1
        else:
            ptr2+=1

    print(and_list)

List_AND(['Doc1','Doc2','Doc3'],['Doc1','Doc3'])



