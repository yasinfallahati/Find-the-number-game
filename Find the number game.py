import random

def play():
    print("=" * 40)
    print("     🎮Find the number game  🎮")
    print("=" * 40)
    print("I picked a number between 1 and 99!")
    print("You have 7 tries to find it.")
    print("=" * 40)

    secret = random.randint(1, 99)
    max_tries = 7

    for attempt in range(1, max_tries + 1):
        remaining = max_tries - attempt + 1
        print(f"\nAttempt {attempt}/{max_tries}  |  {remaining} chances left")

        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number!")
            attempt -= 1
            continue

        if guess < 1 or guess > 99:
            print("⚠️  Number must be between 1 and 99!")
            attempt -= 1
            continue

        if guess == secret:
            print(f"\n🎉  Correct! The number was {secret}!")
            print(f"You found it in {attempt} attempt(s)!")
            break
        elif guess < secret:
            print("⬆️   Go higher!")
        else:
            print("⬇️   Go lower!")
    else:
        print(f"\n😢  Game over! The number was {secret}.")

    print("\n" + "=" * 40)
    again = input("Play again? (y/n): ").strip().lower()
    if again == 'y':
        play()
    else:
        print("Goodbye! 👋")

if __name__ == "__main__":
    play()
