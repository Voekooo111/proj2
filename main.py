import re
from goroscope import find as fd

def main():
    date = input("Введите дату (dd.mm.yyyy): ").strip()

    if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", date):
        print("Ошибка. Введена неверная дата.")
        return

    print(fd(date))

if __name__ == "__main__":
    main()