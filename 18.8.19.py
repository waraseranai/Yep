cost = 0
tickets = int(input("Введтие количество билетов: "))
for i in range(tickets):
    i = int(input("Введите возраст посетителя: "))
    if i < 18:
        cost += 0
    elif 18 <= i <= 25:
        cost += 990
    elif i > 25:
        cost += 1390
if tickets > 3:
    discount = cost / 100 * 10
    cost -= discount
print("Сумма к оплате -", cost)
