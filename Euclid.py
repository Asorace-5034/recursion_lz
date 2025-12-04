def NOD(x,y):                       # Функция эвклида
    if y == 0:
        return x
    else:
        return NOD(y, x % y)

def main():                         # Функция вызова всего
    x = int(input('Введите число: '))
    y = int(input('Введите второе число: '))
    print('НОД этих чисел:', NOD(x, y))

if __name__ == "__main__":          #Выполнение кода, если он запущен как самостоятельный файл
    main()

