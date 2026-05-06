my_dict={
    "banana":(9,6),
    "apple":(100,8),
    "orange":(10,5),
    "mango":(19,4)
}


def inventory_summary(my_item):
    count=0
    for key,value in my_item.items():
       count+=value[0]
    return count

print(inventory_summary(my_dict))

def print_args_kwargs(*args,**kwargs):
    print(args)
    for key,value in kwargs.items():
        print(key,value)

print_args_kwargs("asa","aad","codec",כמות=5,מחיר=6)

dict_student={
    "fesfr":23,
    "drrt":18,
    "sdftg":6,
    "dfty":8
}

def find_student(dict_student,key_student,value_student):
    for key,value in dict_student.items():
        if key==key_student and value==value_student:
            return  value_student,key_student
        else:
            return None
    return None

print(find_student(dict_student,"fesfr",23))
print(find_student(dict_student,"ggg",23))


