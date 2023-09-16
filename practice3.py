# CAR engine program


# engine_on=False
#
# commands = {
#     'start':'staring the engine: ',
#     'stop': 'stopping the engine: ',
#     'status': 'checking engine status: ',
#     'quit': 'exiting the program: ',
#
# }
#
# while True:
#     command=input('Enter a command(start/stop/status/quit): ')
#     if command.lower()=='start':
#         if engine_on:
#             print('engine is alraedy start')
#         else:
#             print('starting the engine: ')
#             engine_on=True
#     elif command.lower()=='stop':
#         if not engine_on:
#             print('first start your engine')
#         else:
#             print('stopping the engine')
#             engine_on=False
#     elif command.lower()=='status':
#         if engine_on:
#             print('engine is running')
#         else:
#             print('engine is off')
#     elif command.lower()=='quit':
#         print('exiting the program')
#         break
#     else:
#         print('invalid command')
#         quit()
# print()


# Guessing game

# import random
# print('welcome to guessing Game')
# answer=input('Do you want to Play!{Yes/No}:  ')
# if answer.lower()=='yes':
#     print(f'ok lets play')
# else:
#     print(quit())
# secret_number=random.randint(0,9)
# guess_count=0
# while True:
#     guess = int(input('Enter a number: '))
#     if guess == secret_number:
#         print('you won')
#         guess_count += 1
#
#         break
#     else:
#         print('you loose')
#         guess_count+=1
#
# print(f'you won in {guess_count} number of guesses',)

# import random
# def guessing_game():
#     secret_numbers=random.randint(0,9)
#     guess_count=0
#     while True:
#         guess=int(input('Enter your guess: '))
#         guess_count+=1
#         if guess==secret_numbers:
#             print('you won')
#             break
#         else:
#             print('you loose')
#             guess_count+=1
# guessing_game()



# print("Enter Your Age")
# age = int(input())
# if age>18:
#     print("Welcome")
# else:
#     print("sorry")
# print("hi there")
# print("hello there")









