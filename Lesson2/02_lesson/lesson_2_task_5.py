def month_to_season(month):
    if month < 1 or month > 12:
        return "Некорректный номер месяца. Введите число от 1 до 12."

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"


print(month_to_season(1))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(11))
