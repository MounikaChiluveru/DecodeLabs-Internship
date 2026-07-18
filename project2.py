
def get_expense_input():
    while True:
        raw_value = input("Enter an expense amount (or type 'quit' to finish): ").strip()

        # Sentinel value check - the "kill switch"
        if raw_value.lower() == "quit":
            return None

        try:
            expense = float(raw_value)
            if expense < 0:
                print("Expense cannot be negative. Please try again.")
                continue
            return expense
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 100, 50.25).")


def track_expenses():
    total = 0.0          # Initialization (Memory) - lives OUTSIDE the loop
    count = 0             # Tracks number of valid entries

    print("=" * 40)
    print("  DecodeLabs Expense Tracker")
    print("=" * 40)

    while True:
        expense = get_expense_input()

        if expense is None:   # Sentinel triggered - break the loop
            break

        total += expense       # Accumulator pattern: State(new) = State(old) + Input
        count += 1
        print(f"  -> Added ${expense:.2f} | Running total: ${total:.2f}\n")

    return total, count


def display_summary(total, count):
    print("=" * 40)
    if count == 0:
        print("No expenses were recorded.")
    else:
        print(f"Total Transactions: {count}")
        print(f"FINAL TOTAL SPENT: ${total:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    final_total, transaction_count = track_expenses()
    display_summary(final_total, transaction_count)