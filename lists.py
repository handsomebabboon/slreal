def removeDups(arr,n):
    temp = []
    for i in range(0,n):
        if arr[i] not in temp:
            temp.append(arr[i])
    return temp

l1 = []
n = int(input('enter the number of elements'))

for i in range(0,n):
    temp = int(input('enter element to append'))
    l1.append(temp)
print("inputed list:{}".format(l1))
noDuplicates = removeDups(l1,n)
print("removed duplicates:{}".format(noDuplicates))
n = int(input('enter the number of even numbers'))

newlist = [2*x for x in range(0,n)]
print("even numbers:{}".format(newlist))
newlist.reverse()
print("reversed:{}".format(newlist))
