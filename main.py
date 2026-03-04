def main():
	date = input("Введите дату (dd-mm-yy): ")
	try:
		dd, mm, yy = date.split("-")
	except:
		print("Ошибка. Введена неверная дата.")


if __name__ == '__main__':
	main()

