#Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в переменную
#Вывести содержимое переменной на экран

def what_to_do(age):
    if age>0:
        if age<2:
            print("Пока еще ползает дома")
        elif age<6.5:
            print("В детском саду или у бабушки с дедушкой")
        elif age<18:
            print("В школе учится. Или не учится. Но в школе.")
        elif age<23:
            print("Высшее образование вымучивает")
        elif age<65:
            print("Должен работать")
        elif age<100:
            print("Наслаждается пенсией")
        else:
            print("Столько не живут!")
    elif age==0:
        print("Вот как раз сейчас рождается")
    elif age>-0.75:
        print("В животике у мамы пока еще")
    else:
        print("Пока еще только в планах")
        


age_str=input("Введите возраст в годах: ")
try:
    age_num=float(age_str)
except TypeError:
    print("А возраст вводится циферками...")
    exit()
what_to_do(age_num)
#if isinstance(age_str,int) or isinstance(age_str, float):
 #   age_fl=float(age_str)
 #   what_to_do(age_fl)
#else:
 #   print("А возраст вводится циферками...")
