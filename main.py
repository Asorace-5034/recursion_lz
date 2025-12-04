import Euclid                                        #импортируем вссе файлы
import perfection
import Pascal
import terms


def main():                                             #вызываем их всех по очереди
    Euclid.main()
    perfection.main()
    Pascal.main()
    terms.main()


if __name__ == "__main__":                              #Выполнение кода, если он запущен как самостоятельный файл
    main()