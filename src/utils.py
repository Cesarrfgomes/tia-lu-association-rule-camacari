import os

def save_results(rules, output_path):
    """Saves the rules to a CSV file."""
    try:
        rules.to_csv(output_path, index=False)
        print(f"Rules saved to {output_path}")
    except Exception as e:
        print(f"Error saving rules: {e}")

def print_top_rules(rules, n=10, sort_by='lift'):
    """Prints the top n rules sorted by a metric."""
    if rules.empty:
        print("No rules to display.")
        return

    print(f"\nTop {n} rules sorted by {sort_by}:")
    print(rules.sort_values(by=sort_by, ascending=False).head(n))
