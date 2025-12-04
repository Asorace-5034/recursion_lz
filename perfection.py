def delitely(n):
    a = []
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    return a


def summa(a, f):
    if f == sum(a):
        print("Число совершенное")
    else:
        print("Число несовершенное")


def main():
    f = int(input("Введите число: "))
    a = delitely(f)
    print(a)
    summa(a, f)

if __name__ == "__main__":   #Выполнение кода, если он запущен как самостоятельный файл
    main()


