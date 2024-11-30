def is_year_leap(year):
    return "true" if year % 4 == 0 else "false"

year = int(input("Введите число: "))
result = is_year_leap(year)
print(f"Делится ли на четыре {year}? - {result}")
