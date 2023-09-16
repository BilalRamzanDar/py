import pandas as pd
data={
    'Name':['Rob','Michael','Mohan','Ismail','Korey','Gautam','David','Andrea','Brad','Angelina','Donald','Tom','Arnold',
            'jared','Stark','Ranbir','Dipika','Priyanka','Nick','Alia','Sid','Abdul'],
    'Age':[27,29,29,28,42,39,41,38,36,35,37,26,27,28,29,32,40,41,43,39,41,39],
    'Income($)':[70000,90000,61000,60000,150000,155000,160000,162000,156000,130000,137000,45000,48000,51000,49500,
                 53000,65000,63000,64000,80000,82000,58000]
}
df = pd.DataFrame(data)
# print(df.to_string())
df.to_csv('knn.csv',index=False)
print(df)