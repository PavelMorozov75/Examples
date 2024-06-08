number = 12.453
print(round(number, 2))
print(round(number, 1))
print(round(number))

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_HALF_DOWN
#ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше
number = Decimal('2.5')  # Избегаем ошибок округления
rounded_number = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
print(rounded_number)  # Правильное округление до 3