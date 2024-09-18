from datetime import datetime

def is_valid_date(dts):
    try:
        datetime.strptime(dts, '%d.%m.%Y')
        return True
    except ValueError:
        return False


dt = input("Введите дату в формате 'дд.мм.гггг': ")
print(is_valid_date(dt))
