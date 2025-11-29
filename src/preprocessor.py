import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

def process_transactions(df):
    """
    Preprocesses the dataframe to convert transactions into a one-hot encoded format.
    Assumes 'descricao_produtos' column contains items separated by ';'.
    """
    if 'descricao_produtos' not in df.columns:
        raise ValueError("Column 'descricao_produtos' not found in dataframe.")

    print("Processing transactions...")
    transactions = df['descricao_produtos'].apply(lambda x: str(x).split(';')).tolist()

    transactions = [[item.strip() for item in transaction if item.strip()] for transaction in transactions]

    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

    print(f"Encoded data shape: {df_encoded.shape}")
    return df_encoded
