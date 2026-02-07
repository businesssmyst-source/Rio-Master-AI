def manage_trade(amount, risk_percent):
    try:
        # Rio calculates how much you can lose safely
        risk_amount = (float(amount) * float(risk_percent)) / 100
        return f"Founder, for a trade of ${amount}, with {risk_percent}% risk, your stop-loss should be at ${risk_amount}."
    except:
        return "I need numbers to calculate the trade, Koushik."

def update_balance(new_data):
    # This saves your trade data to the text file
    with open("accounts.txt", "a") as f:
        f.write(f"\n{new_data}")
    return "Account updated, Boss."