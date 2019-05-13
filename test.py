
list1 = ["f","o","n","z","i","e"]
list2 = [1, 2, 3, 4, 5, 6]

l = {key:value for key, value in zip(list1,list2)}
print(l)

d = {}
for key, value in zip(list1 ,list2):
    d[key] = value
print(d)








nums = [2, 7, 11, 15]
target = 9

def getindex(target, nums):
    indexlist = []
    for n in range(len(nums)):
        for i in range(len(nums)):
            if nums[n] + nums[i] == target:
                indexlist.append(n)
                indexlist.append(i)
    output = []
    for i in indexlist:
        if i not in output:
            output.append(i)
    print(str(output))

#getindex(target, nums)

#####################################################################
def twoSum(nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []





#######################################################################

indexlist = []
for n in range(len(nums)):
    for i in range(len(nums)):
        if nums[n] + nums[i] == target:
            indexlist.append(n)
            indexlist.append(i)
output = []
for i in indexlist:
    if i not in output:
        output.append(i)
#print(str(output))










lis = [2,3,5,7,8]
v = 7

l = []
for n in range(len(lis)):
    for i in range(len(lis)):
        if lis[n] + lis[i] == v:
            l.append(n)
            l.append(i)
output = []
for i in l:
    if i not in output:
        output.append(i)
#print(str(output))
