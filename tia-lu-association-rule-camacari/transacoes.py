import pandas as pd
from collections import Counter
from preprocessamento import preprocessar_produtos

def carregar_transacoes(arquivo_csv):
    print("Carregando dados do arquivo CSV...")
    df = pd.read_csv(arquivo_csv)

    print(f"Total de transações: {len(df)}")

    transacoes = []
    for _, row in df.iterrows():
        produtos = preprocessar_produtos(row['descricao_produtos'])
        if produtos:
            transacoes.append(produtos)

    print(f"Transações processadas: {len(transacoes)}")

    todos_produtos = [p for t in transacoes for p in t]
    contador = Counter(todos_produtos)

    print("\nTop 10 produtos mais frequentes:")
    for produto, count in contador.most_common(10):
        print(f"  {produto}: {count}")

    return transacoes
