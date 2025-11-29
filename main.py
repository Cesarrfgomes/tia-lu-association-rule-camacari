import os
import sys

# Add the current directory to sys.path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_data
from src.preprocessor import process_transactions
from src.fpgrowth_model import run_fpgrowth, generate_rules
from src.utils import save_results, print_top_rules

def main():
    DATA_FILE = os.path.join(os.path.dirname(__file__), "vendas_dataset.csv")
    OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "regras_associacao.csv")
    MIN_SUPPORT = 0.005
    MIN_CONFIDENCE = 0.2

    print(f"Starting analysis on {DATA_FILE}")

    df = load_data(DATA_FILE)
    if df is None:
        return

    df_encoded = process_transactions(df)

    frequent_itemsets = run_fpgrowth(df_encoded, min_support=MIN_SUPPORT)
    if frequent_itemsets.empty:
        print("No frequent itemsets found. Try lowering min_support.")
        return

    rules = generate_rules(frequent_itemsets, min_threshold=MIN_CONFIDENCE, metric="confidence")

    if not rules.empty:
        save_results(rules, OUTPUT_FILE)
        print_top_rules(rules, n=10, sort_by='lift')
    else:
        print("No association rules found.")

if __name__ == "__main__":
    main()
