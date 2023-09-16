import numpy as np
# arr=np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [0,1,2,3]
#
#
# ])
# print(arr.shape)
# print(arr.ndim)
# print(arr.sum())
# print(arr.conj(arr))
# print(arr.diagonal())
# print(arr.max())
# print(arr.min())
# print(arr.transpose())


import pandas as pd
# x=[1,2,3,4,5]
# print(pd.Series(x))
# var=pd.Series(x)
# print(var)
# print(type(var))
# print(var[2])


# dic_nary={
#     'course':['python','java','c++','c'],
#     'fee':[12000,10000,8000,6000],
#     'rank':[1,2,3,4]
# }
#
# x=pd.Series(dic_nary)
# print(x)

# s1=pd.Series(10,index=[1,2,3,4,5,6,7,8])
# print(s1)
# s2=pd.Series(10,index=[1,2,3,4,5])
# print((s1+s2))


# l1=['apple','mango','banana','peach','papaya']
# x=pd.DataFrame(l1)
# print(x)


d={
    'Name':['Bilal','Moonis','Mohsin','Aaqib'],
    'City':['sopore','srinagar','anantnag','bandipora']

}

# x=pd.DataFrame(d)
# print(x)

# x=pd.DataFrame(d,columns=['Name'],index=['a','b','c','d'])
# print(x)

# x=pd.DataFrame(d)
# print(x)
# print(x['Name'][2])

# list1=[
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ]
#
# x=pd.DataFrame(list1)
# print(x)


# s1={'A':pd.Series([1,2,3,4,5]),'B':pd.Series([6,7,8,9,10])}
#
# x=pd.DataFrame(s1)
# print(x)


# Arithmetic operations using pandas

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]},)
# print(var1)
#
# var1['c']=var1['A'] + var1['B']
# print(var1)


# var1['c']=var1['A'] - var1['B']
# print(var1)


# var1['c']=var1['A'] * var1['B']
# print(var1)


# var1['c']=var1['A'] / var1['B']
# print(var1)

# var1['c']=var1['A'] % var1['B']
# print(var1)


# var1=pd.DataFrame({'A':[10,20,30,40,50],'B':[16,17,18,19,20]},)
#
# var1['Result']=var1['A']<=40
# # print(var1)
#
# var1['Result_2']=var1['B']>=18
# print(var1)

# var1=pd.DataFrame({'x':[1,2,3],'y':[4,5,6]})
# print(var1)

# var1.insert(1,'x1',[7,8,9])
# var1.insert(2,'y1',[10,11,12])
# print(var1)


# var1=pd.DataFrame({'x':[1,2,3,4,5],'y':[6,7,8,9,10]})
# print(var1)
# var1['z']=var1['x'][:3]
# print(var1)

# var1=pd.DataFrame({'x':[1,2,3,4,5],'y':[6,7,8,9,10]})
# print(var1['x'][4])

# var1=pd.DataFrame({'x':[1,2,3,],'y':[4,5,6],'z':[7,8,9]})
# print(var1.pop('x'))
# print(var1)


# del var1['z']
# print(var1)





