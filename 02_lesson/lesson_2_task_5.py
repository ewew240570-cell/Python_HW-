def month_to_season(month):
    seasons = {
        "Зима": [12, 1, 2],
        "Весна": [3, 4, 5],
        "Лето": [6, 7, 8],
        "Осень": [9, 10, 11]
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Неверный номер месяца"


print(month_to_season(2))  # Зима
print(month_to_season(5))  # Весна
print(month_to_season(8))  # Лето
print(month_to_season(11))  # Осень
