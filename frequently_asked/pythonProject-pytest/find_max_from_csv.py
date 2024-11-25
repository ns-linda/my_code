import pandas as pd

df=pd.read_csv("test_file.csv")
# print(df['Age'].max())
# print(df[df.Age == df.Age.max()])
# result = df.groupby('Gender').agg({'Age': ['min'], })
# print(result)

df.sort_values("Age", axis = 0, ascending = True,
                 inplace = True, na_position ='last')

gk = df.groupby('Gender').groups
print(gk)

# print(df)

