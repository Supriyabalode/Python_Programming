# def binary_search(arr,target,low,high):
#     if low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             return binary_search(arr,target,mid+1,high)
#         else:
#             return binary_search(arr.target,low,mid-1)
#     else:
#         return -1
# arr=[2,3,4,10,40]
# target=10
# result=binary_search(sorted(arr),target,0,len(arr)-1)
# if result!=-1:
#     print(f"element found at index {result}")
# else:
#     print("element not found")



# list1=[12,23,34,45,56,67,78,89,90]
# num=int(input("enter a number:"))
# start=0
# end=len(list1)-1
# while start<=end:
#     mid=(start+end)//2
#     if list1[mid]==num:
#         print(f"{num} is found at position {mid}")
#         break
#     elif num<list1[mid]:
#         end=mid-1
#     elif num>list1[mid]:
#         start=mid+1    
# else:
#     print("element is not found")




# list1=[10,20,30,40,50,60,70,80,90]
# num=int(input("enter a number:"))
# start=0
# end=len(list1)-1
# while start<=end:
#     mid=(start+end)//2
#     if list1[mid]==num:
#         print(f"number is found at  {mid}")
#         break
#     elif num>list1[mid]:
#         start=mid+1
#     elif num<list1[mid]:
#         end=mid-1
# else:    
#     print("not found....")



# list1=[1,2,3,4,5,6,7,8]
# n=5
# start=0
# end=len(list1)-1
# while start<=end:
#     mid=(start+end)//2
#     if list1[mid]==n:
#         print(f"number is found at position {mid}")
#         break
#     elif n>list1[mid]:
#         start=mid+1
#     else:
#         end=mid-1
# else:
#     print("not found")


# list1=[1,2,3,4,5,6,7,8]
# n=5
# start=0
# end=len(list1)-1
# while start<=end:
#     mid=(start+end)//2
#     if list1[mid]==n:
#         print(f"number is found at index {mid}")
#         break
#     elif n<list1[mid]:
#         end=mid-1
#     else:
#         start=mid+1
# else:
#     print("not found") 




n=67
list1=[1,2,3,4,5,6,7,8,9,10]
list1.sort()
start=0
end=len(list1)-1
while start<=end:
    mid=(start+end)//2
    if list1[mid]==n:
        print(f"number is found at index {mid}")
        break
    elif n>list1[mid]:
        start=mid+1
    else:
        end=mid-1
else:
    print("not found......")

