# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的:
# 掌握函数的用法

def fill_list(input_list):
    'Fill sth. into an empty list'

    for idx in range(10):
        input_list.append(idx)

    return

# call function
mylist=[]
fill_list(mylist)
print(mylist)
