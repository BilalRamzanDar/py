import pandas as pd
# create csv
# college={
#     'Name':['Bilal','Aqib','Moonis','Mohsin','Asif','Wasim'],
#     'Branch':['Cse','Civil','Cse','Cse','Mechanical','Civil'],
#     'Semester':['8th','8th','8th','8th','8th','8th',],
#     'Phone No':[8899019669,12345666,678768687,57688900,119087766,908098097],
#     'Address':['Sopore','Srinagar','Srinagar','Anantnag','Sopore','Qazigund']
# }
# x=pd.DataFrame(college)
# print(x)
# x.to_csv('file_1.CSV',index=False)

# read csv file

# x=pd.read_csv("file_1.CSV",names=['col1','col2','col3'])
# print(x)

# x=pd.read_csv("file_1.CSV",nrows=1)
# x=pd.read_csv("file_1.CSV",usecols=['Name','Semester'])
# x=pd.read_csv("file_1.CSV",usecols=[0,1])
# x=pd.read_csv("file_1.CSV",skiprows=[4])

# print(x)


# x=pd.read_csv("file_1.CSV")
# print(x)
# x.index
# x.columns
# print(x.index)
# print(x.columns)
# print(x.head(2))
# print(x.tail(2))

# print(x[:3])
# print(x.to_numpy())
# x.loc[4,'Name']='Junaid'
# print(x)

# print(x.loc[(1,2),['Name','Address']])
# print(x.iloc[2,0])

# employs={
#     'Name':['Bilal','Moonis','Mohsin','Mujtaba','Wasik','Asif','Aqib','Adil','Saqib','Sadaf','Sammen','Danish','Rizwan','haider','Huzaif',
#             'Murtaza','Arif','Atif','Wajahat','Abdul Hanan','Abdul Basit','Bakir'
#             ],
#     'Employ type':['User experience designer','Web Developer','Database Administrator','Information Security Analyst','Data Scientist',
#                    'Software Developer','Support Specialist','Network Engineer','Performance Analyst','Application Architect','Data Analyst',
#                    'DevOps Engineer','Digital marketing','Product Manager','Project Manager','Computer repair technician','Application Developer',
#                    'Cloud Engineer','Computer programmer','Computer and Information Research Scientists','Content strategy','Social media',
#                    ],
#     'Salary Per Month':['100000','90000','80000','85000','78000','50000','40000','30000','60000','65000','45000','47000',
#                         '40000','30000','31000','37000','27000','70000','35000','55000','38000','80000'],
#     'Working Hours Per Day':[6,8,9,8,12,12,12,12,12,12,12,10,12,12,12,10,10,10,12,8,8,8]
# }
# Data1=pd.DataFrame(employs)
# Data1.to_csv('file2.CSV',index=False)
# x=pd.read_csv('file2.csv')
# # print(x.to_string())
#
# x.dropna(axis=1)
# print(x.to_string())

# var=pd.read_csv('file2.csv')
# var.replace('Bakir','Wajid',inplace=True)
# print(var.to_string())

# var=pd.read_csv('file3.csv')
# print(var.to_string())
# var.loc[1] = var.loc[1].fillna({'Name': 'Basit', 'Employ type': 'Data Analyst', 'Salary Per Month': '50000', 'Working Hours Per Day': 12})
# var.loc[23] = var.loc[23].fillna({'Name': 'Basit', 'Employ type': 'Data Analyst', 'Salary Per Month': '50000', 'Working Hours Per Day': 12})
# var.loc[24] = var.loc[24].fillna({'Name': 'Owais', 'Employ type': 'Product Manager','Salary Per Month': '50000', 'Working Hours Per Day': 12 })
# var.loc[25] = var.loc[25] = ['Sakeena', 'Junior engineer', '20000', 12]
#
# var.to_csv('updated_file.csv',index=False)
# print(var.to_string())












