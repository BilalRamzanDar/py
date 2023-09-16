# def add():
#     print("welcome")
# add()
# from lecture1 import total


# def add(x,y):
#     # print(x+y)
#     return  x+y
#
# def sub(x,y):
#     print(x-y)
#
#
# res = add(10,29)
#
# sub(res,30)

# def sub(x,y):
#     return x-y
# def mul(x,y):
#     print(x*y)
# result=sub(20,10)
# mul(result,2)

# rock paper secissor game using function

# import  random
# def get_choices():
#     print("Welcome To The Game! ")
#     print('Do You Want To play: ')
#     Answer = input('Enter Answer as YES Or NO: ')
#     if Answer.lower() == 'yes':
#         print('OK Lets play')
#     else:
#         print(quit())
#         return get_choices()
#
#
#     player_choice=input('Enter your choice{rock,paper,scissors}: ')
#     options=['rock','paper','scissors']
#     computer_choice=random.choice(options)
#     choices={'player':player_choice,'computer':computer_choice}
#     return choices
# def check_winner(player,computer):
#     print(f'you choose {player} ,computer choose {computer}')
#     if player==computer:
#         return 'it is tie'
#     elif player =='rock':
#         if computer=='scissors':
#             return 'you win'
#         else:
#             return 'you loose'
#     elif player=='paper':
#         if computer=='scissors':
#             return 'computer wins'
#         else:
#             return 'you win'
#     elif player=='scissors':
#         if computer=='paper':
#             return 'you win'
#         else:
#             return 'computer win'
# choices=get_choices()
# result=check_winner(choices['player'],choices['computer'])
# print(result)

# def greaterOfThree(x,y,z):
#     if x > y and x > z:
#         return 'x is greater'
#     elif y > x and y>z:
#         return 'y is greater'
#     else:
#         return 'z is greater'
#
# result=greaterOfThree(10,20,30)
# print(result)
# Greatest of 3 numbers using function

# def greaterOfTwo(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def greaterOfThree(x,y,z):
#     return greaterOfTwo(x,greaterOfTwo(y,z))
# res=greaterOfThree(10,20,30)
# print(res)
# Greatest of 4 numbers using function

# def greatestOfTwo(a,b):
#     if a >b:
#         return a
#     else:
#         return b
# def greaterOf3(a,b,c):
#     if a > b and a> c:
#         return a
#     elif b>a and b> c:
#         return b
#     else:
#         return c
#
# def greaterOf4(a,b,c,d):
#     return greaterOf3(a,b,greatestOfTwo(c,d))
# res=greaterOf4(10,20,30,40)
# print(res)
# Sum of elements of the list using function

# def sum(list1):
#     total=0
#     for i in list1:
#         total+=i
#     return total
# list1=[]
# n=int(input('Enter the size of the list: '))
# for i in range(n):
#     ele=int(input('Enter the elements of the list: '))
#     list1.append(ele)
# res=sum(list1)
# print(res)

# palindrome of a number

# x=121
# temp = x
# rev = 0
# while (x>0):
#     dig = x % 10
#     rev = rev * 10 + dig
#     x = x // 10
# if temp==rev:
#     print('it is palindrome')
# else:
#     print('not palindrome')

# n=int(input('Enter any number : '))
# temp=n
# sum=0
# while(n>0):
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# if temp==sum:
#     print('It is a palindrome')
# else:
#     print('It is not a palindrome')

# def palindrome(x):
#     n=int(input('Enter a number: '))
#     temp=n
#     sum=0
#     while (n>0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     if temp==sum:
#         return 'its a palindrome'
#     else:
#         return 'its not a palindrome'
# res=palindrome(sum)
# print(res)

# def palidrome(word):
#     word=str(input('Enter a string to check if it is palindrome: '))
#     if word==word[::-1]:
#         return 'it is palindrome'
#     else:
#         return 'it is not palindrome'
# res=palidrome('word')
# print(res)

# def palidrome():
#     word=str(input('Enter a string to check if it is palindrome: '))
#     if word==word[::-1]:
#         return 'it is palindrome'
#     else:
#         return 'it is not palindrome'
# print(palidrome())













