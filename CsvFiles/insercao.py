import pandas as pd

nome = str(input("Nome: "))
idade = int(input("Idade: "))

#abrir arquivo atual
df = pd.read_csv('../API/exemplo.csv')

# criar um df vazio com as colunas nome e idade
#df = pd.DataFrame()

df = pd.concat([df,pd.DataFrame({
  'nome':[nome],
  'idade':[idade]
})], ignore_index=True)

# inserir um registro com o nome e a idade lida anteriromente no df
#df = pd.DataFrame({'Nome':[nome],'Idade': [idade]})

# df é o objeto da classe DataFrame, to_csv é o método.
df.to_csv('./exemplo.csv', index=False)

