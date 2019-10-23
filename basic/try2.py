# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的:
# 掌握函数的用法

def double_list(input_list):
    'Double all elements of a list'

    for idx in range(len(input_list)):
        input_list[idx]*= 2

    return

# call function
mylist = [1,3,5,7,9]
double_list(mylist)
print(mylist)
