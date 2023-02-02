#напишите программу, которая на вход принимает число 
# и выдает его квадрат (число, умноженное само на себя)
def zadacha0():
    number = int(input("Введите число")) 
    result = (number*number)
    print(f'{number}*{number}={result}')
    #или
    print(str(number)+'*'+str(number)+'='+str(result))
#напишите программу, которая на вход принимает
#  2 числа и проверяет является ли одно квадратом другого
def zadacha1():
    number1=int(input('Введите первое число '))
    number2=int(input('Введите второе число '))
    if number1*number2 == number2:
        print('Второе число является квадратом первого')
    elif number1*number2 == number1:
        print('Первое число является квадратом второго')
    else:
        print('Ни одно число не является квадратом другого')
#организуйте последовательный ввод чисел
#  до тех пор, пока не будет 
# введен 0. Подсчитайте среди введенных чисел те, которые кратны 3.
def zadacha2():
    count = 0
    a = int(input('Введите число '))
    while a!=0:
        if a%3==0:
                count+=1
        a=int(input('Введите число '))
    if count == 0:
        print('Чисел, кратных 3, нет')
    else:
        print (f'кол-во чисел, кратных 3: {count}')
# zadacha2()

def zadacha3():
    # Напишите программу, 
    # которая будет на вход принимать
    # число N и выводить числа от -N до N
    number = int(input('Введите число '))
    number = abs(number)
    negative= -number
    while negative<=number:
        print(negative, end =" ")
        negative=negative+1
# zadacha3()

# напишите программу, которая будет 
# принимать на вход дробь и показывать 
# первую цифру дробной части числа.
def zadacha4 ():
    number = 657.9123
    # print(type(number))
    # / - деление
    # % - остаток от деления
    # // - целочисленное деление
    print(number // 1)
    print(number % 1)
    print(int(number % 1*10//1))
# zadacha4 ()

# zadacha3()
#number=5
#if number>3:
#        print('больше 3')
#else:
#        print('меньше 3 или равно') 


# напишите программу, 
# которая находит наибольшне и наименьшее число
# из СПИСКА значений 
# def zadacha5 ():
def zadacha5():
    numbers=[5,3,-1,0,-4,9]
    print(numbers)
# zadacha5 ()
    maxNumber = numbers[0]
    minNumber = numbers[0]
    for el in numbers:
        if el>maxNumber:
            maxNumber=el
        elif el<minNumber:
            minNumber=el
    print(f'максимум равен {maxNumber}')
    print(f'минимум равен {minNumber}')
    print(f'максимум равен {max(numbers)}')
    print(f'минимум равен {min(numbers)}')
# zadacha5()
# возведение в степень
number=25
print(number*number)
print(number**0.5)
# после ** указывается степень
# измерить длину чего-то len
length = len(numbers)
print(f'длина {len(numbers)}')
print(f'индексы {len(numbers)}')