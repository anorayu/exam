import random

def quiz_game():
    questions = {
        "Какая столица Франции?": "Париж",
        "Сколько планет в Солнечной системе?": "Восемь",
        "Кто написал роман 'Война и мир'?": "Лев Толстой"
    }

    score = 0

    print("Добро пожаловать в игру 'Викторина'!")

    for question, answer in questions.items():
        print(question)
        user_answer = input("Введите ваш ответ: ")

        if user_answer.lower() == answer.lower():
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно! Правильный ответ: {answer}")

    print(f"Вы набрали {score} из {len(questions)} возможных баллов.")

quiz_game()
