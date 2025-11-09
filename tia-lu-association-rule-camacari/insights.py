def analisar_resultados(regras, top_n=20):
    if regras is None or regras.empty:
        print("Nenhuma regra encontrada.")
        return

    print(f"\n{'='*80}")
    print(f"ANÁLISE DE REGRAS DE ASSOCIAÇÃO - TOP {top_n}")
    print(f"{'='*80}\n")

    regras['antecedentes'] = regras['antecedents'].apply(lambda x: ', '.join(list(x)))
    regras['consequentes'] = regras['consequents'].apply(lambda x: ', '.join(list(x)))

    for idx, row in regras.head(top_n).iterrows():
        print(f"Regra {idx + 1}:")
        print(f"  Se comprar: {row['antecedentes']}")
        print(f"  Então também compra: {row['consequentes']}")
        print(f"  Suporte: {row['support']:.3f}")
        print(f"  Confiança: {row['confidence']:.3f}")
        print(f"  Lift: {row['lift']:.3f}\n")


def gerar_insights_combos(regras, top_n=10):
    if regras is None or regras.empty:
        return

    print(f"\n{'='*80}")
    print(f"INSIGHTS PARA COMBOS DE PRODUTOS - TOP {top_n}")
    print(f"{'='*80}\n")

    for idx, row in regras.head(top_n).iterrows():
        antecedentes = ', '.join(list(row['antecedents']))
        consequentes = ', '.join(list(row['consequents']))
        print(f"Combo {idx + 1}: {antecedentes} + {consequentes}")
        print(f"  Probabilidade conjunta: {row['confidence']*100:.1f}%")
        print(f"  Frequência: {row['support']*100:.2f}%")
        print(f"  Relevância (Lift): {row['lift']:.2f}x\n")
