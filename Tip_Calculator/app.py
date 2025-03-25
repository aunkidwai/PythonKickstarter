def calculate_tip(total_bill, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    return tip_amount

def main():
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("Please enter the total bill amount: $"))
    tip_percentage = float(input("Please enter the tip percentage (e.g., 15 for 15%): "))
    tip = calculate_tip(total_bill, tip_percentage)
    print(f"The tip amount is: ${tip:.2f}")

if __name__ == "__main__":
    main()