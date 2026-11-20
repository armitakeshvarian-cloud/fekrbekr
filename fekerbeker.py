"""armita keshvatian . 404131123 , fekrbekr.py"""

import random


# تولید رمز تصادفی چهار رقمی
def generate_code():

    secret = []

    while len(secret) < 4:

        number = random.randrange(1, 7)

        # جلوگیری از تکراری بودن ارقام
        if number not in secret:
            secret.append(number)

    return secret


# بررسی معتبر بودن حدس بازیکن
def check_input(guess):

    # بررسی تعداد و نوع ورودی
    if len(guess) != 4 or not guess.isdigit():
        return False

    # بررسی محدوده ارقام
    for i in range(4):
        if guess[i] < '1' or guess[i] > '6':
            return False

    # بررسی تکراری نبودن ارقام
    for i in range(4):
        for j in range(i + 1, 4):
            if guess[i] == guess[j]:
                return False

    return True


# مقایسه حدس با رمز مخفی
def compare_code(secret, guess):

    correct = 0
    wrong_place = 0

    for i in range(4):

        if guess[i] == secret[i]:
            correct += 1

        elif guess[i] in secret:
            wrong_place += 1

    print("Correct digits in correct place:", correct)
    print("Correct digits in wrong place:", wrong_place)

    if correct == 4:
        return True

    return False


# تابع اصلی بازی
def main():

    secret = generate_code()

    attempts = 0
    win = False

    while attempts < 10 and not win:

        print("\nRemaining chances:", 10 - attempts)

        guess = input("Enter your guess: ")

        # بررسی معتبر بودن ورودی
        if not check_input(guess):
            print("Invalid input! Try again.")
            continue

        # تبدیل ورودی به لیست اعداد
        guess = [int(guess[0]), int(guess[1]),
                 int(guess[2]), int(guess[3])]

        attempts += 1

        # مقایسه حدس با رمز مخفی
        win = compare_code(secret, guess)

        if win:
            print("You won")
            print("Number of attempts:", attempts)

    # اعلام باخت و نمایش رمز مخفی
    if not win:
        print("Game Over!")
        print("The secret code was:", secret)


# شروع بازی
main()