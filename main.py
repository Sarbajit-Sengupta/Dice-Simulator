import random


def main():
    while True:
        print("Rolling The Dices...")
        print("The Values are :")
        print(random.randint(1, 6))
        print(random.randint(1, 6))
        try:
            answer = input("Roll the Dices Again?").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if answer not in {"yes", "y"}:
            return


if __name__ == '__main__':
    main()
