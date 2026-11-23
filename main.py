import random


def roll_dice(num_dice=1, sides=6):
    return [random.randint(1, sides) for _ in range(num_dice)]


def dice_roller():
    print("\n=== Dice Roller ===")

    while True:
        try:
            num_dice = int(input("how many dics can roll ? (example: 1 or 2): "))
            if num_dice < 1:
                print("minimum 1 dics enter now!\n")
                continue

            sides = int(input("how many sides in dics? (example 6): "))
            if sides < 2:
                print("sides minimum 2 here!\n")
                continue
        except ValueError:
            print("please enter the correct number!\n")
            continue

        results = roll_dice(num_dice, sides)
        print(f"\nroll result: {results}")
        print(f" (Total): {sum(results)}")

        again = input("\nonce again roll? (y/n): ").strip().lower()
        if again != "y":
            print("program finish. thank you!")
            break


if __name__ == "__main__":
    dice_roller()
