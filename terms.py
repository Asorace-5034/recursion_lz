def foo(n, k = None):               # Функция разложения на слагаемые
    if k is None:
        k = n

    if n == 0:
        return []

    result = []
    if n <= k:
        result.append([n])
    for i in range(1, 1+min(n, k)):
        for l in foo(n-i, i):
            result.append(l + [i])

    return result

def main():                                     # Вызов главной функции
    n = int(input('Введите число для разложения: '))
    print(*foo(n), sep='\n') 

if __name__ == "__main__":                      #Выполнение кода, если он запущен как самостоятельный файл
    main()

    