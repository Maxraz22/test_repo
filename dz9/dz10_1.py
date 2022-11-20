import sys

def month(n):
    if n == 1:
        month = "Січень"
    if n == 2:
        month = "Лютий"
    if n == 3:
        month = "Березень"
    if n == 4:
        month = "Квітень"
    if n == 5:
        month = "Травень"
    if n == 6:
        month = "Червень"
    if n == 7:
        month = "Липень"
    if n == 8:
        month = "Серпень"
    if n == 9:
        month = "Вересень"
    if n == 10:
        month = "Жовтень"
    if n == 11:
        month = "Листопад"
    if n == 12:
        month = "Грудень"
    try:
        return month
    except UnboundLocalError as ex:
        print("Місяця під таким номером не існує!", file=sys.stderr)
        print(ex, file=sys.stderr)
    except Exception:
        print("Невідома помилка!", file=sys.stderr)
try:
    print(month(int(11)))
except NameError as ex:
    print("Ви ввели не числове значення номера місяця!", file=sys.stderr)
    print(ex, file=sys.stderr)
except Exception:
    print("Невідома помилка!", file=sys.stderr)
