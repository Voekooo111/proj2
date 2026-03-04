import re

def main():
	date = input("Введите дату (dd.mm.yy): ")
	try:
		if re.match(r'\b\d{2}\.\d{2}\.\d{4}\b', date):
			dd, mm, yy = date.split(".")
		else:
			print("Ошибка. Введена неверная дата.")
		
	except:
		print("Ошибка. Введена неверная дата.")


if __name__ == '__main__':
	main()

