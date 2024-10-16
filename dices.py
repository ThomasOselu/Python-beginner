import random


def roll_dice():
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die
    return die1, die2


def main():
    while True:
        # Ask user if they want to roll the dice
        roll = input("Roll the dice? (yes/no): ").lower()

        if roll == "yes":
            die1, die2 = roll_dice()
            print(f"You rolled a {die1} and a {die2}. Total: {die1 + die2}")
        elif roll == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
