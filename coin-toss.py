import random

def coin_toss():
    """
    Simulates a coin toss and returns 'Heads' or 'Tails'.
    """
    # Generate a random number (0 or 1)
    # 0 will represent Tails, 1 will represent Heads
    result = random.randint(0, 1)

    if result == 0:
        return "Tails"
    else:
        return "Heads"

if __name__ == "__main__":
    print("Welcome to the Coin Toss Simulator!")
    input("Press Enter to toss the coin...") # User presses Enter to initiate the toss

    toss_result = coin_toss()
    print(f"\nThe coin landed on: {toss_result}!")

    print("\nThanks for playing!")