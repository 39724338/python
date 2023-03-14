import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3']})
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7']})

print(df1)
print(df2)

result = pd.concat([df1, df2])
print(result)