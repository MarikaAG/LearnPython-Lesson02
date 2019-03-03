#Напишите функцию get_summ(num_one, num_two), 
# которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() 
# и перехватывать исключение ValueError если приведение типов не сработало

def get_summ(num_one, num_two):
    try:
        n1=int(num_one)
        n2=int(num_two)
    except (ValueError, TypeError): #TypeError is included for None
        return(None)
    return(n1+n2)
     
def print_result(n1,n2):  #the function was made in order not to repeat the formatted print with descriptions
    summa=get_summ(n1,n2)
    if summa==None:
        print(f"Хотя бы одно из слагаемых {n1} и {n2} не может быть приведено к типу int")
    else:
        print(f'Слагаемые {n1} и {n2} привелись к типу int и дали в сумме {summa}')
 


#MAIN
print_result(1,2)
print_result("7","-4")
print_result("abc","0")
print_result(None, 5)
print_result("-3,5",4)