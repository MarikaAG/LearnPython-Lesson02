#Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
#Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ. Например:
#Пользователь: Что делаешь?
#Программа: Программирую

ANSWERS={"Как дела?": "Хорошо!",
         "Что делаешь?": "С тобой разговариваю",
         "Как тебя зовут?": "Компутер я!!",
         "До свидания": "До свидания",
         "Пока": "Пока-пока!"}

GOODBYE={"До свидания": "До свидания :)",
         "Пока": "Пока-пока!"}


def ask_user():
    user_answer=input("Как дела?")
    while user_answer!="Хорошо":
        user_answer=input("Как дела?")
    print(f'User wrote {user_answer}')
    return()

def answer_user():
    user_speech=input("Привет! Что скажешь?  ")
    while user_speech not in GOODBYE:
        if user_speech in ANSWERS:
            user_speech=input(f'{ANSWERS[user_speech]}  ')
        else:
            user_speech=input("Я не знаю... Напиши еще что-нибудь  ")
    print(GOODBYE[user_speech]) #the answer is in GOODBYE


#MAIN
#ask_user()
answer_user()