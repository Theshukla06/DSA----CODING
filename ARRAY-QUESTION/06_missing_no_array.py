def MissingElement(arr):
    Step1_sum = sum(arr)
    step2_total = (l+1)*(l+2)/2
    return step2_total - Step1_sum

arr = [1,2,4,5]
l = len(arr)
print(MissingElement(arr))

# def MissingNO(arr):
#     for element in range(arr[0],arr[-1]+1):
#         if element not in arr:
#             a.append(element)
#     return a
# a=[]
# arr=[1,2,3,5]
# print(MissingNO(arr))








# # arr=[1,2,3,4,5,6,7,9,10]

# # missing_element = []

# # for element in range(arr[0],arr[-1]+1):
    
# #     if element not in arr:
# #         missing_element.append(element)
# # print(missing_element)


# #   USER INPUPT IN ARRAY

# # a = int(input("Enter Length Of Array :- "))
# # b=[]

# # for i in range(a[0],a[-1]+1):
# #     c=int(input())
# #     b.append(c)
# # print(b)

# a = [1,2,3,5]
# missin_element = []

# for element in range(a[0],a[-1]+1):
#     if element not in a:
#         missin_element.append(element)

# print('Your missig element is :- ',missin_element)

# def MissingElement(arr):
#     step1_sum = sum(arr)
#     step2_total = (l+1) * (l+2)/2 
    
#     return step2_total - step1_sum

# arr = [1,2,4,5]
# l = len(arr)
# print(MissingElement(arr))