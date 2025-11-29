from mlxtend.frequent_patterns import fpgrowth, association_rules

def run_fpgrowth(df_encoded, min_support=0.005):
    """
    Applies FPGrowth algorithm to find frequent itemsets.
    """
    print(f"Running FPGrowth with min_support={min_support}...")
    frequent_itemsets = fpgrowth(df_encoded, min_support=min_support, use_colnames=True)
    print(f"Found {len(frequent_itemsets)} frequent itemsets.")
    return frequent_itemsets

def generate_rules(frequent_itemsets, min_threshold=0.1, metric="confidence"):
    """
    Generates association rules from frequent itemsets.
    """
    print(f"Generating rules with {metric} >= {min_threshold}...")
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    print(f"Generated {len(rules)} rules.")
    return rules
