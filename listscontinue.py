# names=['moin','ather','sahil','aijaz','moin']
# names.append('taha')
# print(names.count('moin'))
# print(names)
# names.remove('ather')
# print(names)
# names.pop()
# print(names)
# names.sort()
# print(names)
# names.clear()
# print(names)
# newlist=names.copy()
# print(newlist)
# names.extend(['sahil','rahil'])
# print(names)
# print(names.index('ather'))
# names.reverse()
# print(names)
# names.insert(2,"irfan")
# print(names)


# list1=[]
#  temp=[]
# n=int(input('Enter the size of the list: '))
# for i in  range(n):
#     numbers = int(input('Enter the elements of the list: '))
#     list1.append(numbers)
# print(list1)
# for i in range(0,len(list1)):
#     if list1[i]==list1[::-1]:
#     # if list1[i] ==len(list1):
#         list1.remove(i)
#
#         # temp.append(list1[i])
#  temp.pop()
# # print(temp)
#
# print(list1)


# list1=[1,2,1,3,1,3,4,5,6,2,1,4,4,6]
# temp=[]
# for i in list1:
#     if i not in temp:
#         temp.append(i)
# if len(list1)==1:
#     new_list=[list1[0]]
# else:
#     new_list=[i for i in  list1  if i !=temp[0]]
# print(new_list)

# my_list = [2, 4, 2, 2, 1, 2, 2, 2, 3, 2, 2]
#
# # create an empty list to store unique elements
# unique_list = []
#
# # loop through each element in the original list
# for element in my_list:
#
#     # if the element is not already in the unique_list
#     if element not in unique_list:
#         # append the element to the unique_list
#         unique_list.append(element)
#
# # if the length of unique_list is 1, it means all elements in the original list are the same
# if len(unique_list) == 1:
#
#     # create a new list with just the unique element
#     new_list = [unique_list[0]]
#
# else:
#
#     # otherwise, create a new list with all elements from the original list except the duplicates
#     new_list = [element for element in my_list if element != unique_list[0]]
#
# # print the final new_list
# print(new_list)

#
# list1=[]
# temp=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     numbers=int(input('Enter the elements of the list:'))
#     list1.append(numbers)
#
# for element in list1:
#     if element not in temp:
#         temp.append(element)
# if len(temp[::-1]):
#     new_list = [element for element in list1 if element != temp[::-1]]
#
# if len(temp)==1:
#     new_list=[temp[0]]
# # if len(temp[::-1]):
# #     new_list = [element for element in list1 if element != temp[0]]
# else:
#     new_list = [element for element in list1 if element != temp[0]]
# print(new_list)


# swapping of ist and last element of the list
# list1=[]
# n=int(input('Enter the size of the list1: '))
# for i in range(n):
#     elements=int(input('Enter the elements of the list'))
#     list1.append(elements)
# temp=list1[0]
# list1[0]=list1[n-1]
# list1[n-1]=temp
# print(list1)

# swap of elements

# list1=[]
# n=int(input('Enter the size of the list1: '))
# for i in range(n):
#     elements=int(input('Enter the elements of the list'))
#     list1.append(elements)
# temp=list1[3]
# list1[3]=list1[n-2]
# list1[n-2]=temp
# print(list1)

# list1=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     ele=int(input('Enter the elements of the list1: '))
#     list1.append(ele)
# x=int(input('Enter the element to check in list1: '))
# if x not in list1:
#     print('the enterd ele is not present in the list')
# else:
#     print('it is present')
# import lecture6
# lecture6.add()











