#Доработайте файл answers.py,
# чтобы он использовал конструкцию if __name__=="__main__"
# За основу для доработки взят файл Chat_user_exception.py 
#Для проверки импорта используется файл Chat_user_imp_to.py



ANSWERS={"Как дела?": "Хорошо!",
         "Что делаешь?": "С тобой разговариваю",
         "Как тебя зовут?": "Компутер я!!",
         "До свидания": "До свидания",
         "Пока": "Пока-пока!"}

GOODBYE={"До свидания": "До свидания :)",
         "Пока": "Пока-пока!"}


def answer_user_except():
    try:
        user_speech=input("Привет! Что скажешь?  ")
    except KeyboardInterrupt:
        print("Ну и ладно! Пока...")
        return
    #user_speech=input("Привет! Что скажешь?  ")
    while user_speech not in GOODBYE:   #If a user didn't say good bye
        if user_speech in ANSWERS:
            user_speech=input(f'{ANSWERS[user_speech]}  ')
        else:                           #
            user_speech=input("Я не знаю... Напиши еще что-нибудь  ")
    print(GOODBYE[user_speech]) #if a user said good bye


#MAIN
if __name__=="__main__":
    answer_user_except()