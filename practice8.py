# import pandas as  pd
# data={
#     'age':[22,2,5,47,52,46,56,55,60,62,61,18,27,29,49,55,25,58,19,18,21,26,40,45,50,54,23],
#     'bought_insurance':[0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0]
# }
# df=pd.DataFrame(data)
# print(df.to_string())

# print(df.to_string())
# x=df.to_csv('insurance.csv',index=False)

# import pandas as pd
# marks_details = {
#     'Bilal':[90,99,94,92,98],
#     'Moonis':[99,90,91,93,94],
#     'Mohsin':[92,93,94,90,95],
#     'Mujitaba':[94,91,90,96,89],
#     'Muntazir':[94,95,92,97,99]
# }
# names = list(marks_details.keys())
# marks = list(marks_details.values())
# df = pd.DataFrame.from_dict(marks_details,orient='index',columns=['English','Maths','Science','Urdu','Social Science'])
# df['Average']=df.mean(axis=1)
# print(df.to_string())
#
# import matplotlib.pyplot as plt
# df.plot.bar(rot=0)
# plt.xlabel('Name of Student')
# plt.ylabel('Marks/subject')
# plt.show()

# import pandas as pd
# marks_details = {
#     'Names':['Bilal','Moonis','Mohsin','Mujitaba','Muntazir'],
#     'English':[90,99,94,92,98],
#     'Maths':[99,90,91,93,94],
#     'Science':[92,93,94,90,95],
#     'Social Science':[94,91,90,96,89],
#     'Urdu':[94,95,92,97,99]
# }
# data_frame= pd.DataFrame(marks_details)
# print(data_frame)
# import matplotlib.pyplot as plt
# data_frame.plot.bar(rot=0)
# plt.xlabel('Name of Student')
# plt.ylabel('Marks/subject')
# plt.show()
