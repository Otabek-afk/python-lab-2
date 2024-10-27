money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

wallet = money_capital + salary - spend
month = 0
while wallet > 0:
    spend *= (1 + increase)
    wallet += salary
    wallet -= spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
