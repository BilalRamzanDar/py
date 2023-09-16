# names = ['irfan','sahil','irfan','aijaz','ranveer'];
# print(type(names))
# print(names)
# print(names[0])

# names[0]='alim'
# print(names)

# fruits = list((''))

# for i in names:
#     print(i)


# for i in range(0,len(names)):
#     print(names[i]);

# equilateral triangle pattern
# rows=5
# for i in range(0,rows):
#
#     for j in range(0,rows-i):
#         print(end=" ")
#
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print("")

# inverted traiangle
# rows=5
# for i in range(rows,0,-1):
#
#     for j in range(0,rows-i):
#         print(end=" ")
#
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")


# total=0
# alpha=[]
# n=int(input('Enter the number of elements in list: '))
# for i in range(0,n):
#     print('entered elements are: ')
#     ele=[input()]
#     alpha.append(ele)
#
# print('The entered list is: ', alpha)


# sum of elements of the list user_input
# total=0
# list1=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     numbers=int(input('enter number: '))
#     list1.append(numbers)
# print('List:',list1)
# for ele in range(0, len(list1)):
#     total = total + list1[ele]
# print(f'Sum of elements of{list1} is',total)

# second approach
# total=0
# numbers=[10,2,34,5,6,]
# for n in range(0,len(numbers)):
#     total+=numbers[n]
# print(total)

# list1=[10,2,34,5,6]
# print("the sum of elements of the list1 is: ",sum(list1))

# list1=[]
# s=int(input('enter the size of list: '))
# for i in range(s):
#     numbers=int(input('enter number: '))
#     list1.append(numbers)
# print(f'The sum of the entered elements of{list1} is =',sum(list1))

# multiplication of the elements of the list

# multiple=1
# list1=[1,2,3,1,3,4,5]
# for i in range(0,len(list1)):
#     multiple=multiple*list1[i]
# print(multiple)

# second approach using user input
# multiple=1
# list1=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     numbers=int(input('Enter the elements of the list: '))
#     list1.append(numbers)
# print(list1)
# for j in range(0,len(list1)):
#     multiple*=list1[j]
#     # multiple=multiple*list1[j]
# print(f'multiple of the elements of the list1{list1} = ',multiple)

# largest element of the list:
# list1=[1,2,4,56,7,55,4,8]
# max=list1[0]
# for i in range(1,len(list1)):
#     if list1[i]>max:
#         max=list1[i]
# print('the max number of list1 is',max)

# list1=[]
# n=int(input('Enter the size of list: '))
# for i in range(n):
#     numbers=int(input('enter the elements of the list:'))
#     list1.append(numbers)
# print(list1)
# max = list1[0]
# for i in range(1, len(list1)):
#     if list1[i] > max:
#         max=list1[i]
# print("The max element of the list is:", max)
#REMOVIN THE DUPLICATE ELEMENTS OF LIST
# list1=[1,2,3,1,3,4]
# temp=[]
# for i in(list1):
#     if i not in temp:
#         temp.append(i)
# print(temp)

# list1=[]
# temp = []
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     numbers=int(input('Enter the elements of the list: '))
#     list1.append(numbers)
# print(list1)
# for i in list1:
#     if i not in temp:
#         temp.append(i)
# print(temp)

# same_list=[]
# temp = []
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     numbers=int(input('Enter the elements of the list: '))
#     same_list.append(numbers)
# print(same_list)
# [temp.append(i) for i in same_list if i not in temp]
# print(temp)


# arr=[1,2,3,4,5,6,7,8,9,10]
# temp=[]
# for i in range(0,len(arr)):
#     if arr[i]%2==0:
#         temp.append(arr[i])
# print(temp)

# list1=[]
# temp=[]
# n=int(input('Enter the size of list: '))
# for i in range(n):
#     numbers=int(input('enter the number in list1: '))
#     list1.append(numbers)
# print(f'The entered list is : ',list1)
# for i in range(0,len(list1)):
#     if list1[i]%2==0:
#         temp.append(list1[i])
# print(f'The even elements of the list {list1} are: ',temp)



# arr=[1,2,3,4,5,6,7,8,9,10]
# temp=[]
# for i in range(0,len(arr)):
#    if arr[i]%2!=0:
#        temp.append(arr[i])
# print(temp)

# list1=[]
# temp=[]
# n=int(input('Enter the size of list: '))
# for i in range(n):
#     numbers=int(input('enter the number in list1: '))
#     list1.append(numbers)
# print(f'The entered list is : ',list1)
# for i in range(0,len(list1)):
#     if list1[i]%2!=0:
#         temp.append(list1[i])
# print(f'The odd elements of the list {list1} are: ',temp)


# templist1=['a','e','o','u','o','a']
# temp=[]
# for i in range(1,len(list1)):
#     if list1[i]=='a' or 'e'or 'i'or 'o'or 'u':
#         temp.append(list1[i])
# print(temp)
# print(list1)

#
# list1=[]
# temp=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     alpha=str(input('Enter the characters of the list: '))
#     list1.append(alpha)
# print(list1)
#
# for j in range(0,len(list1)):
#     # if list1[j].lower()=='a' or 'e'or 'i' or 'o' or 'u':
#      if list1[j].lower()=='a':
#          temp.append(list1[j])
#      elif list1[j].lower()=='e':
#         temp.append(list1[j])
#      elif list1[j].lower()=='i':
#             temp.append(list1[j])
#      elif list1[j].lower()=='o':
#         temp.append(list1[j])
#      elif list1[j].lower()=='u':
#          temp.append(list1[j])
#
# print(temp)
#
#





































