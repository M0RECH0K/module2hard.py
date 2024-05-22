while True:
    result = ""
    a = input('Введите число от 3 до 20 ')
    n = int(a)
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    print(result)
    b = (input('Продолжим? '))
    if b == 'Да':
        continue
    else:
        break
    