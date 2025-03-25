import math

def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    return math.ceil(tip_amount)  # rounding up to the nearest whole number

def main():
    print("Welcome to the Tip Calculator!")
    try:
        bill_amount = float(input("Enter the bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage (e.g., 15, 20): "))
        tip = calculate_tip(bill_amount, tip_percentage)
        print(f"The tip amount is: ${tip}")
    except ValueError:
        print("Please enter valid numbers for bill amount and tip percentage.")

if __name__ == "__main__":
    main()