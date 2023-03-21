import pandas as pd

id = int(input("id: "))

df = pd.read_csv('../API/exemplo.csv')
print(df)

print(df.iloc[[id]])
