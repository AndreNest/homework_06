# 2*)  Сделать поле чудес . Компьютер загадывает слово.
# А мы его угадываем. Делаем с помощью функций. Кто хочет посложней - добавляем очки и барабан.
import random
import time
def get_question():
    with open('word.txt', 'r', encoding = 'utf-8') as f:
        question_line = f.read().splitlines()
        random_question = random.randrange(0, len(question_line))
        question_and_answer = str(question_line[random_question])
        for i in range(0, len(question_and_answer)):
            if question_and_answer[i] == '-':
                question = question_and_answer[:i]
                answer = question_and_answer[i+1:]
        return question, answer

def game_viewer(answer):
    game_view = []
    for i in range(len(answer)):
        game_view.append('*')
    return game_view

def game(question, answer, set_view):
    user_answer = []
    points = 0
    while True:
        print('Барабан крутится!')
        random_whels = random.randrange(50, 500, 50)
        time.sleep(random.randint(1,5))
        print(f'Сектор {random_whels} на барабане')
        print(f"Вопрос - {question}")
        print(''.join(set_view))
        user = input('Введите букву или слово целиком: ')
        if user == answer:
            print(''.join(set_view))
            print('Вы угадали слово!')
            print(f'Вы набрали {points + (random_whels * 5)} за полностью угаданное слово!')

            break
        if user in answer:
            print('такая буква есть!')
            points += random_whels
            print(f'Вы набрали {points}')
            for i in range(len(answer)):
                if answer[i] == user:
                    set_view[i] = user
                    user_answer = ''.join(set_view)
        else:
            print('Такой буквы нет!')
        if user_answer == answer:
            print(''.join(set_view))
            print('Вы угадали все буквы!')
            print(f'Вы набрали {points}')
            break

question, answer = get_question()
game(question, answer, game_viewer(answer))







