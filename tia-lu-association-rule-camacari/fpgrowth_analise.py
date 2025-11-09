import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

def aplicar_fpgrowth(transacoes, suporte_minimo=0.005):
    print(f"\nAplicando FP-Growth (suporte mínimo: {suporte_minimo*100:.2f}%)...")

    te = TransactionEncoder()
    te_ary = te.fit(transacoes).transform(transacoes)
    df_transacoes = pd.DataFrame(te_ary, columns=te.columns_)

    print(f"Total de itens únicos: {len(df_transacoes.columns)}")

    itemsets_frequentes = fpgrowth(df_transacoes, min_support=suporte_minimo, use_colnames=True)

    print(f"Itemsets frequentes encontrados: {len(itemsets_frequentes)}")

    return itemsets_frequentes, df_transacoes


def gerar_regras_associacao(itemsets_frequentes, confianca_minima=0.5, lift_minimo=1.0):
    if itemsets_frequentes.empty:
        print("Nenhum itemset frequente encontrado.")
        return None

    regras = association_rules(itemsets_frequentes, metric="confidence", min_threshold=confianca_minima)
    regras = regras[regras['lift'] >= lift_minimo]
    regras = regras.sort_values(['confidence', 'lift'], ascending=False)

    print(f"Regras de associação geradas: {len(regras)}")

    return regras
