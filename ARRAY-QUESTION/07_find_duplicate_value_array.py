# arr = [1,2,3,4,2,7,8,8,3]
# print(arr)

# for i in range(0 , len(arr)):
#     for j in range(i+1,len(arr)):

#         if arr[i] == arr[j]:

#             print(arr[j],end=" ") 

arr = [1,2,3,4,2,7,8,8,3]
l=[]
for i in arr:
    if i not in l:
        l.append(i)
    else:
        print(i,end=' ')