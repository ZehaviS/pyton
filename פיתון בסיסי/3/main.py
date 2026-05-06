#
# my_set = set()
#
# def analyze_list(lst):
#     minimom=99999999
#     maximom=0
#     sum=0
#     for i in lst:
#         sum+=i
#         if i <minimom:
#             minimom=i
#         if i>maximom:
#             maximom=i
#
#         if lst.count(i) == 1:
#             my_set.add(i)
#     return my_set,maximom,minimom,sum/len(lst)
#
# print(analyze_list([1, 9, 6, 8, 8, 9, 8]))

def filter_dict(d, threshold):
    new_l=[]
    for key,value in d.items():
        if value >threshold:
            new_l.append(key)
    return new_l
d={"gjyhg":8956287,
   "drff":5555,
   "dfghj":23456789}

print(filter_dict(d,77777))

