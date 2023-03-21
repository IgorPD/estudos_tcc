import pandas as pd

nome = int(input("nome: "))

df = pd.read_csv("../API/exemplo.csv")

index = df[df["nome"] == nome].index[0]
df = df.drop(index)

print(df)

df.to_csv('./exemplo.csv', index=False)