import fractions
import math
frac_1, frac_2 = input('Введите 1-ю дробь в виде "a/b": ').split('/'), input('Введите 2-ю дробь в виде "a/b": ').split('/')
a, b, c, d = int(frac_1[0]), int(frac_1[1]), int(frac_2[0]), int(frac_2[1])

# Умножение дробей
prod_frac = [a * c, b * d]
nod = math.gcd(prod_frac[0], prod_frac[1])
prod_frac = [int(prod_frac[0] / nod), int(prod_frac[1] / nod)]

# Сумма дробей
sum_frac = [a * d + b * c, b * d]
nod = math.gcd(sum_frac[0], sum_frac[1])
sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]

# Проверка с помощью модуля fractions
fraction_1 = fractions.Fraction(a, b)
fraction_2 = fractions.Fraction(c, d)
sum = fraction_1 + fraction_2
prod = fraction_1 * fraction_2
print(f'Результат произведения - {prod_frac[0]}/{prod_frac[1]}')
print(f'Результат суммы - {sum_frac[0]}/{sum_frac[1]}')
print(f'ПРОВЕРКА ПРОИЗВЕДЕНИЯ: {prod}')
print(f'ПРОВЕРКА СУММЫ: {sum}')