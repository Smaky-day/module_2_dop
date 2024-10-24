def generate_password(n):
    pairs = []    # Зададим пустой список для хранения пар чисел
    for i in range(1, 21): # Пройдемся по всем возможным парам от 1 до 20 с циклом for для числа i
        for j in range(1, 21): # с вложенным циклом for для числа j
            if n % (i + j)== 0 and i != j:  # заданное число n должно без остатка делиться на сумму i и j
             # при том i не должно равняться j - такую пару добавим в список
                pairs.append((i, j))
    # Теперь избавимся от дубликатов пар
    unique_pairs = []    # Зададим пустой список для хранения уникальных пар чисел
    for pair in pairs:   # Пройдемся по каждой паре чисел в списке pairs
        if pair not in unique_pairs and (pair[1], pair[0]) not in unique_pairs:
        # Если текущая пара и ее обратная пара (цифры поменяны местами) отсутствуют, то добавим в список unique_pairs
            unique_pairs.append(pair)

    password = ''     # Зададим пустую строку для хранения пароля на основе уникальных пар чисел
    for pair in unique_pairs:
        password += str(pair[0]) + str(pair[1])  # объединим преобразованные в строки пары чисел и добавим в строку password

    return password

for n in range(3, 21):   # сгенерируем и выведем на экран все парооли для чисел от 3 до 20
    result = generate_password(n)
    print(f"{n} - {result}")