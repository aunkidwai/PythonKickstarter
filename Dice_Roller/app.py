import random
def roll_dice(sides=6):
    """Simulate rolling a die with a given number of sides."""
    return random.randint(1, sides)
def main():
    print("Welcome to the Dice Roller!")
    sides = int(input("Enter the number of sides for the dice: "))
    num_rolls = int(input("Enter the number of times to roll the dice: "))
    results = []
    for _ in range(num_rolls):
        result = roll_dice(sides)
        results.append(result)
        print(f"Rolled a {result}")
    print(f"Results: {results}")
    print(f"Average roll: {sum(results) / len(results):.2f}")
if __name__ == "__main__":
    main()
