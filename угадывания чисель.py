import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100.")

    while True:
        guess = int(input("Попробуйте угадать число: "))
        attempts += 1

        if guess < number:
            print("Ваше число слишком маленькое.")
        elif guess > number:
            print("Ваше число слишком большое.")
        else:
            print(f"Поздравляю! Вы угадали число {number}!")
            print(f"Количество попыток: {attempts}")
            break

guess_number()
