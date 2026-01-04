def month_to_season(month):
    seasons = {
        (12, 1, 2): "Зима",
        (3, 4, 5): "Весна",
        (6, 7, 8): "Лето",
        (9, 10, 11): "Осень"
    }

    for months, season in seasons.items():
        if month in months:
            return season

    return "Неверный номер месяца. Введите число от 1 до 12."

