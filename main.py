import pandas as pd
import re
import numpy as np

from collections import Counter
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

from transacoes import carregar_transacoes
from fpgrowth_analise import aplicar_fpgrowth, gerar_regras_associacao
from insights import analisar_resultados, gerar_insights_combos

def main():
    print("="*80)
    print("ANÁLISE DE REGRAS DE ASSOCIAÇÃO - FP-GROWTH (Vestuário)")
    print("="*80)

    transacoes = carregar_transacoes('vendas_dataset.csv')

    if not transacoes:
        print("Erro: Nenhuma transação válida encontrada.")
        return

    itemsets, df_transacoes = aplicar_fpgrowth(transacoes, suporte_minimo=0.005)
    regras = gerar_regras_associacao(itemsets, confianca_minima=0.5, lift_minimo=1.0)

    analisar_resultados(regras, top_n=20)
    gerar_insights_combos(regras, top_n=10)

    if regras is not None and len(regras) > 0:
        regras_export = regras.copy()
        regras_export['antecedentes'] = regras_export['antecedents'].apply(lambda x: ', '.join(list(x)))
        regras_export['consequentes'] = regras_export['consequents'].apply(lambda x: ', '.join(list(x)))
        regras_export[['antecedentes', 'consequentes', 'support', 'confidence', 'lift']].to_csv(
            'regras_associacao.csv', index=False, encoding='utf-8-sig'
        )
        print("\nResultados salvos em 'regras_associacao.csv'")

if __name__ == "__main__":
    main()
