import pandas as pd


class PandasDataProvider:
    def __init__(self):
        pass

    def inserir_registro(self, nome, idade):
        df = pd.read_csv('exemplo.csv', index_col=False)
        # inserindo dados no csv
        df = pd.concat([df, pd.DataFrame({
            'nome': [nome],
            'idade': [idade]
        })], ignore_index=True)
        df.to_csv('./exemplo.csv', index=False)

    def ler_registro(self, id_registro):
        df = pd.read_csv('exemplo.csv', index_col=False)
        registro = df.iloc[[id_registro]].to_dict(orient='records')
        return registro

    def excluir_registro(self, id_registro):
        df = pd.read_csv("exemplo.csv", index_col=False)
        df = df.drop([id_registro])
        df.to_csv('./exemplo.csv', index=False)
