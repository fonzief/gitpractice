
list1 = ["f","o","n","z","i","e"]
list2 = [1, 2, 3, 4, 5, 6]

l = {key:value for key, value in zip(list1,list2)}
print(l)

d = {}
for key, value in zip(list1 ,list2):
    d[key] = value
print(d)
