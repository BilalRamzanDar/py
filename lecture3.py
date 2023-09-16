# print("Enter Username")
# uname = input()
# print("Enter Password")
# upass = input()
#
# if uname == 'admin' and upass == 'admin123':
#     print("welcome")
# else:
#     print("invalid credentials")

# if uname == 'admin':
#     if upass == 'admin123':
#         print("welcome")
#     else:
#         print("invalid username/password")
# else:
#     print("invalid username/password")

# print("Enter Name")
# name = input()
# if name != 'sam':
#     print("welcome")
# else:
#     print("sorry sam")

# greatest of three numbers

# print("Enter Number1")
# n1 = int(input())
# print("Enter Number2")
# n2 = int(input())
# print("Enter Number3")
# n3 = int(input())
#
# if n1>n2 and n1>n3:
#     print("n1 is greater")
# elif n2>n1 and n2>n3:
#     print("n2 is greater")
# else:
#     print("n3 is greater")

# if n1 > n2:
#     if n1 >n3:
#         print("n1 is greater")
#     else:
#         print("n3 is greater")
# elif n2 > n3:
#     print("n2 is greater")
# else:
#     print("n3 is greater")

#  print('Mujitaba')
# print('enter name')
# name = input()
# print(name)
#
# num1=10
# num2=12
# sum=num1+num2
# print(sum)

# print('enter your numbers')
# num1=int(input('enter num1: '))
# num2=int(input('enter num2: '))
#
# sum=num1+num2
# print('the sum is',sum)

# a=int(input('enter num1: '))
# b=int(input('enter num1: '))
# c=int(input('enter num1: '))
# d=int(input('enter num1: '))
#
# if a>b:
#        if a>c:
#         if a>d:
#             print("a is greater")
#         else:
#             print('d is greater')
#
# else:
#     if b>c:
#         if b>d:
#             print("b is greater")
#         else:
#             print('d is greater')
#     else:
#         if c>d:
#             print('c is greater')
#         else:
#             print('d is greater')

# a=int(input('enter num1: '))
# b=int(input('enter num2: '))
# c=int(input('enter num3: '))
# d=int(input('enter num4: '))
#
# if a>b and a>c and a>d:
#     print('a is greater')
# elif b>c and b>d:
#     print('b is greater')
# elif c>d:
#     print("c is greater")
# else:
#     print('d is greater')

# even odd

# print('enter numbers: ')
# num1=int(input())
# if num1%2==0:
#     print("EVEN")
# else:
#     print('ODD')

# user_name=input('enter your username: ')
# password=input('enter your password: ')
# if user_name=='bilal':
#     if password=="bilal123":
#         print('hello')
#     else:
#         print('invalid input')
# else:
#     print('invalid input))
# print('Enter your details\n')
# adhar=input('enter adhar: ')
# pan=input('enter pan: ')
# passport=input('enter passport: ')
# if adhar=='adhar' and pan =='pancard' or passport=='passport':
#     print('welcome')
# elif pan=='pancard' and passport=='passport' or adhar=='adhar':
#     print('welcome')
# elif passport=='passport' and adhar=='adhar' or pan=='pancard':
#
#     print('welcome')
# else:
#     print('something went wrong!')

# print('enter your details\n')
# adhar=input('Enter your adhar: ')
# pan=input('Enter your your pan: ')
# passport=input('enter passport: ')
#
# if adhar.lower()=='adhar':
#     if passport.lower()=='passport' or pan.lower() =='pancard':
#         print('welcome')
#     else:
#         print('some document missing')
# else:
#     if pan=='pancard':
#         if passport=='passport' or adhar=='adhar':
#             print('welcome')
#         else:
#             print('some document missing')
#     else:
#         if passport=='passport':
#             if adhar=='adhar' or pan=='pancard':
#                 print('welcome')
#             else:
#                 print('some document missing')
#         else:
#             print('some document missing')

# print('enter your details\n')
# user=input('Enter your adhar: ')
# user=input('Enter your your pan: ')
# user=input('enter passport: ')
#
# if user.lower()=='adhar':
#     if user.lower()=='passport' or user.lower() =='pancard':
#         print('welcome')
#     else:
#         print('some document missing')
# else:
#     if user=='pancard':
#         if user=='passport' or user=='adhar':
#             print('welcome')
#         else:
#             print('some document missing')
#     else:
#         if user=='passport':
#             if user=='adhar' or user=='pancard':
#                 print('welcome')
#             else:
#                 print('some document missing')
#         else:
#             print('some document missing')
#
#


# print("Do you have an adhar press y else n")
# adhar = input()
#
# print("Do you have an Pancard press y else n")
# pancard = input()
#
# print("Do you have an Passport press y else n")
# passport = input()
#
# if (adhar == 'y' and pancard == 'y') or (adhar == 'y' and passport == 'y') or (pancard == 'y' and passport == 'y'):
#     print("welcome")
# else:
#     print("not welcome")


# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,5,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)
# for i in range(5):
#     print("welcome")

# for i in range(1,11):
#     if i%2!=0:
#         print(i)

# for i in range(20,61):
#     if i%2==0:
#         print(i)

# n=int(input('enter a number: '))
# for n in range(20,60):
#     if n%2==0:
#         print(n)
#
#
# for i in range(100,0,-1):
#     if i%2!=0:
#         print(i)


# i=int(input('enter number'))
# for i in range(100,0,-1):
#     if i%2!=0:
#         print(i)

# n=int(input('Enter the number: '))
# for i in range(1,11):
#     print(n*i)

# Factorial of number
# fact=1
# n=int(input('Enter number: '))
# for i in range(1,n+1):
#    fact=fact*i
#    print(fact)

# print("Enter the numner to check the factorial: ")
# num=int(input('Enter the number:'))
# fact=1
# if num<0:
#     print('Factorial does not exist')
# elif num==0:
#     print('fact of 0 is 0')
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#         print(fact)

# n = 10;
# sum = 0;
# for i in range(1,11):
#     sum = sum+i
#     print(sum)
# sum=0
# n=int(input('Enter the number: '))
# for i in range(1,n+1):
#         sum=sum+i
#         print(sum)

# n=int(input('enter a number: '))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
print(sum)

# num=10
# sum=0
# for i in range(1,num+1):
#     if i%2==0:
#         sum+=i
#         print('\nthe sum numbers is',num,'is: ',sum)
#     else:
#         print('odd is',i)


# string=input('enter the string: ')
# count=0
# for i in range(0,len(string)):
#     if (string[i]!=''):
#         count=count+1
#         print('The total characters in string: '+str(count))


# string='bilal'
# for i in range(0,len(string)):
#     print(str(i))

# for i in range(1500,2700):
#     if i%5==0 and i%7==0:
#         print(i)

# n=int(input('Enter the number: '))
# for i in range(n,2700):
#     if i%7==0 and i%5==0:
#         print(i)

# temp=input('Enter the temperature to convert in celcius and farenhiet: ')
# degree=int(temp[0:-1])
# i_convention=temp[-1]
# if i_convention.upper()=='C':
#     result=int(round(9*degree/5+32))
#     o_convention='Farhenheit'
# elif i_convention.upper()=='F':
#     result=int(round(degree-32*5/9))
#     o_convention='Celsius'
# else:
#     print('input proper temp')
#     quit()
# print('the temprature in',o_convention,'is',result,'degrees')


# celsius=float(input('Enter the degree temperature: '))
# farnhiet=(celsius*9/5)+32
# print('the temperature in',celsius,'is','equal to',farnhiet,'f')

# faranhiet=float(input('Enter the farnhiet temperature: '))
# celsius=(faranhiet/9*5)-32
# print('the temperature in',faranhiet,'faranhiet','is','equal to',celsius,'c')


# unit=str(input('Enter the temperature in Celisius or Faranhiet: '))
# temp=float(input('Enter the temperature: '))
# if unit=='f' or unit== 'F':
#     print('The temperature will b tranformed from farnhiet to celsius')
#     converted_tempC=(temp-32)*(5/9)
#     print(f"{temp} F expressed in celsius is{converted_tempC} C")
# elif unit=='c' or unit=='C':
#         print('The temperature will b tranformed from celsius to farnhiet')
#         converted_tempF = (temp * 9 / 5) + 32
#         print(f"{temp} C expressed in farnhiet is ',{converted_tempF} F")
# else:
#     print('enter valid input')


# Leap_year program
# year = int(input('Enter a year: '))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f'The year {year} is leap_year')
#     else:
#         print(f'The year {year} is not leap_year')
# else:
#     if year % 4 == 0:
#         print(f'The {year} is leap_year')
#     else:
#         print(f'The entered year {year} is not leap_year')
