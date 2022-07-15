def dogs_old_like_human():
    dogs_old = int(input('Введите возраст собаки: '))
    dogs_year = 0
    if dogs_old >= 2:
        for i in range(0, 2):
            dogs_year += 10.5
        for i in range(0, dogs_old - 2):
            dogs_year += 4
    else:
        dogs_year += 10.5
    print(f'Возраст собаки в человеческих мерках равен {dogs_year}')
dogs_old_like_human()