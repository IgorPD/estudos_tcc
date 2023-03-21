import pandas as pd
df = pd.read_csv('../API/exemplo.csv', index_col=False)


def inserir_registro(nome, idade):
  df = pd.read_csv('../API/exemplo.csv', index_col=False)
  # inserindo dados no csv
  df = pd.concat([df, pd.DataFrame({
    'nome': [nome],
    'idade':[idade]
  })], ignore_index=True)
  df.to_csv('./exemplo.csv', index=False)


def ler_registro(id):
  df = pd.read_csv('../API/exemplo.csv', index_col=False)
  print(df.iloc[[id]])


def excluir_registro(id):
  df = pd.read_csv("../API/exemplo.csv", index_col=False)
  df = df.drop([id])
  df.to_csv('./exemplo.csv', index=False)


if __name__ == '__main__':
  df = pd.read_csv('../API/exemplo.csv', index_col=False)
  while True:
    print("----------------")
    print("1-Inserir")
    print("2-Ler")
    print("3-Excluir")
    print("0-Sair")
    print("----------------")

    # Opção do usuário
    opc = int(input("Escolha uma operação: "))

    if opc == 1:
      print("Inserir\n")
      nome = str(input("Nome: "))
      idade = int(input("Idade: "))
      inserir_registro(nome,idade)

    elif opc == 2:
      df = pd.read_csv('../API/exemplo.csv')
      #print(df,'\n')
      id = int(input("id: "))
      ler_registro(id)

    elif opc == 3:
      print("Excluir \n")
      id = int(input("id: "))
      excluir_registro(id)

    elif opc == 0:
        # df.to_csv('./exemplo.csv', index=False)
        break
    else:
      print("Opção inválida, tente novamente\n")