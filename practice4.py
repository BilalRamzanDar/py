# engine_on = False
#
#
# class car:
#     def __init__(self):
#         self.command = ''
#
#     def set_commands(self, command):
#         self.command = command
#
#     def output(self):
#         while True:
#             global engine_on
#             commands = input('Enter command (start/stop/status/quit): ')
#
#             if commands == 'start':
#                 if engine_on:
#                     print('Engine is already started.')
#                 else:
#                     print('Starting the engine.')
#                     engine_on = True
#
#             elif commands == 'stop':
#                 if not engine_on:
#                     print('First start your engine.')
#                 else:
#                     print('Stopping the engine.')
#                     engine_on = False
#
#             elif commands == 'status':
#                 if engine_on:
#                     print('Engine is running.')
#                 else:
#                     print('Engine is off.')
#
#             elif commands == 'quit':
#                 print('Exiting the program.')
#                 break
#
#             else:
#                 print('Invalid command.')
#
#     def get_command(self):
#         return self.command
#
#
# c1 = car()
# c1.output()


# updating the name using class concept

# class Students:
#     def __init__(self):
#         self.first_name = input('Enter first name: ')
#         self.middle_name = input('Enter middle name: ')
#         self.last_name = ""
#
#     def default(self):
#         print('First name:', self.first_name)
#         print('Middle name:', self.middle_name)
#
#     def change_details(self):
#         self.first_name = input('Enter new first name: ')
#         self.middle_name = input('Enter new middle name: ')
#         self.last_name = input('enter last name')
#
#     def update(self, last_name):
#         self.last_name = last_name
#         print('Last name:', self.last_name)
#
#     def updated_details(self):
#         print('First name:', self.first_name)
#         print('Middle name:', self.middle_name)
#         print('Last name:', self.last_name)
#
# std1 = Students()
#
# while True:
#     print('Menu:')
#     print('Press 1 to check default details.')
#     print('Press 2 to change details.')
#     print('Press 3 to  update details.')
#     print('Press 4 to check updated details.')
#     choice = input()
#
#     try:
#         choice = int(choice)
#     except ValueError:
#         print('Invalid input. Please enter a valid choice.')
#         continue
#
#     if choice == 1:
#         std1.default()
#         answer = input('If you want to update data, press "y". Otherwise, press any other key to exit: ')
#         if answer.lower() == 'y':
#             continue
#         else:
#             break
#
#     elif choice == 2:
#         std1.change_details()
#         answer = input('If you want to update data, press "y". Otherwise, press any other key to exit: ')
#         if answer.lower() == 'y':
#             continue
#         else:
#             break
#
#     elif choice==3:
#         print('enter last name')
#         Last_name=input()
#         std1.update(Last_name)
#         std1.updated_details()
#         answer = input('If you want to update data, press "y". Otherwise, press any other key to exit: ')
#         if answer.lower() == 'y':
#             continue
#         else:
#             break
#     elif choice == 4:
#         std1.updated_details()
#         answer = input('If you want to update data, press "y". Otherwise, press any other key to exit: ')
#         if answer.lower() == 'y':
#             continue
#         else:
#             break
#
#     else:
#         print('Invalid input. Please enter a valid choice.')
#         answer = input('If you want to update data, press "y". Otherwise, press any other key to exit: ')
#         if answer.lower() == 'y':
#             continue
#         else:
#             break

# EMOJI CONVERTER EXAMPLE using class
# class EmojiConverter:
#     def __init__(self):
#         self.action = {
#             ':)':'😂',
#             ':(':'😭',
#             ':D':'😉',
#             ':P':'😜',
#             ':<3':'❤️'
#         }
#
#     def convert(self,message):
#         self.message=message
#         words = message.split()
#         output=""
#         for word in words:
#             output +=self.action.get(word,word) + " "
#         return output
#
# converter = EmojiConverter()
# while True:
#     message = input('Enter message: ')
#     converted_text = converter.convert(message)
#     print('Converted message :', converted_text)



















