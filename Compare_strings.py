#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты


def compare_strs(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1==str2:
            return(1)
        elif len(str1)>len(str2): #FTP strings are different
            return(2)
        elif str2=="learn":
            return(3)
        else: return(5)   #when 2 different strings and the second string is longer and is not "learn"    
    else: return(0)   #even 1 argument is not a string

def print_result(arg1,arg2):
    result=compare_strs(arg1,arg2)
    print(f'Arguments: "{arg1}" with a type {type(arg1)} and "{arg2}" with a type {type(arg2)}. Result: {result}')

#MAIN
#str1=input("Input the first string: ")
#str2=input("Input the second string: ")
arg1=1
arg2="string"
#result=compare_strs(arg1,arg2)
print_result(arg1,arg2)
arg1=0.5
arg2="learn"
print_result(arg1,arg2)
arg1="1"
arg2="string"
print_result(arg1,arg2)
arg1="string"
arg2="learn"
print_result(arg1,arg2)