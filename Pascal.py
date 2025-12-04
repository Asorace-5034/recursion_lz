def Pascal(n):                                # Функция, которая выводит строку из треугольника Паскаля
    if n == 0:
        return [1]
    else:
        row = [1]
        previous_row = Pascal(n - 1)
        for i in range(len(previous_row) - 1):
            row.append(previous_row[i] + previous_row[i + 1])    
        row.append(1)
        return row

def main():                                       # Главная функция вызова
    n = int(input('Введите число, которое хотите превратить в треугольник Паскаля: '))
    for i in range(n):
        print(Pascal(i))

if __name__ == "__main__":                              #Выполнение кода, если он запущен как самостоятельный файл

    main()



#https://it.kgsu.ru/Python_Recursion/pythonRecursion073.html
