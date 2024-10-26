num_0 = num = int(input('Введите целое число: ')) 
res = ''
letters = 'ABCDEF'
while num > 0:
    remn = num % 16
    if remn >= 10:
        remn = letters[remn - 10]
    else:
        remn = str(remn)
    res = remn + res
    num //= 16
print(res) 
print(f'ПРОВЕРКА: {hex(num_0)}')     # проверка      