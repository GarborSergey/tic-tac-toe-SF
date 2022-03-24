import random

# Нумерация областей идет слева-направо сверху-вниз
# None - область пустая
# True - область с "Х"
# False - область с "O"
area_values = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}

turns = 0

hello = "__________________________________________\n" \
        "****** Welcom to tic-tac-toe game! *******\n" \
        "*enter 'help' to see the list of commands*\n" \
        "__________________________________________"

help_txt = "___________________________________________\n" \
          "******* enter 'start' to start game********\n" \
          "******** enter 'exit' to exit game*********\n" \
          "Numbering of the cells of the playing field\n" \
          "****************** 1|2|3 ******************\n" \
          "****************** _____ ******************\n" \
          "****************** 4|5|6 ******************\n" \
          "****************** _____ ******************\n" \
          "****************** 7|8|9 ******************\n" \
          "___________________________________________\n"


# Рисует горизонтальную линию
def draw_line():
    print('-----')


# Заполняет клетку взависимости от ходов
def draw_in_are(area):
    if area == True:
        return 'x'
    elif area == False:
        return 'o'
    return ' '


# Рисует горизонтальные области поля
def print_line_area(first, second, third):
    print(
        draw_in_are(first) + '|' + draw_in_are(second) + '|' + draw_in_are(third)
    )


# Рисует поле
def print_area(area_values):
    print_line_area(area_values[1], area_values[2], area_values[3])
    draw_line()
    print_line_area(area_values[4], area_values[5], area_values[6])
    draw_line()
    print_line_area(area_values[7], area_values[8], area_values[9])


# Проверяет можно ли нарисовать в этой области
def chek_area(number):
    if area_values[number] == None:
        return True
    return None


# Ход пользователя
def turn_user(area_values):
    global turns
    try:
        turn = int(input('Enter the cell number of the game field ---> '))
        if turn in range(1, 10):
            if chek_area(turn):
                area_values[turn] = True
                turns += 1
                return True
            print('This cell is already occupied!')
            return False
        print('Enter the correct cell number of the field!')
        return False
    except ValueError:
        print('Enter something field!')


# Проверяет условия победы
def check_win(area_values):
    # Проверяет три области
    def check_win_line(first, second, third):
        global turns
        if all([first, second, third]):
            print('You WIN! Enter "start" to restart game.')
            return True
        elif first == False and second == False and third == False:
            print('You lose( Enter "start" to restart game.')
            return True
        elif turns == 9:
            print('Nobody win! Enter "start" to restart game.')
            return True
        return False

    # Все условия победы
    if check_win_line(area_values[1], area_values[2], area_values[3]) or \
            check_win_line(area_values[4], area_values[5], area_values[6]) or \
            check_win_line(area_values[7], area_values[8], area_values[9]) or \
            check_win_line(area_values[1], area_values[4], area_values[7]) or \
            check_win_line(area_values[2], area_values[5], area_values[8]) or \
            check_win_line(area_values[3], area_values[6], area_values[9]) or \
            check_win_line(area_values[1], area_values[5], area_values[9]) or \
            check_win_line(area_values[3], area_values[5], area_values[7]):
        return True
    return False


# Ход компьютера
def turn_computer(area_values):
    # Проверка не победит ли пользователь на следующем ходу
    def check_upcoming_win(first, second, third):
        if first == True and second == True and third == None:
            return True
        elif first == True and second == None and third == True:
            return True
        elif first == None and second == True and third == True:
            return True
        return False

    # Рисует в одной свободной области из 3
    def draw_in_free_area(first, second, third):
        global turns
        if area_values[first] == None:
            area_values[first] = False
        elif area_values[second] == None:
            area_values[second] = False
        elif area_values[third] == None:
            area_values[third] = False
        turns += 1

    # Рисует в случайно выбранной, пустой области
    def draw_in_random_area(area_values: dict):
        global turns
        free_areas = []
        if turns < 9:
            for key in area_values:
                if area_values[key] == None:
                    free_areas.append(key)
            area_values[random.choice(free_areas)] = False
            turns += 1

    if check_upcoming_win(area_values[1], area_values[2], area_values[3]):
        draw_in_free_area(1, 2, 3)
    elif check_upcoming_win(area_values[4], area_values[5], area_values[6]):
        draw_in_free_area(4, 5, 6)
    elif check_upcoming_win(area_values[7], area_values[8], area_values[9]):
        draw_in_free_area(7, 8, 9)
    elif check_upcoming_win(area_values[1], area_values[4], area_values[7]):
        draw_in_free_area(1, 4, 7)
    elif check_upcoming_win(area_values[2], area_values[5], area_values[8]):
        draw_in_free_area(2, 5, 8)
    elif check_upcoming_win(area_values[3], area_values[6], area_values[9]):
        draw_in_free_area(3, 6, 9)
    elif check_upcoming_win(area_values[1], area_values[5], area_values[9]):
        draw_in_free_area(1, 5, 9)
    elif check_upcoming_win(area_values[3], area_values[5], area_values[7]):
        draw_in_free_area(3, 5, 7)
    else:
        draw_in_random_area(area_values)


# Петля игры
def game_loop():
    while not check_win(area_values):
        print_area(area_values)
        if turn_user(area_values):
            turn_computer(area_values)
            print(turns)
        else:
            continue
    print_area(area_values)


# Очищает игровое поле
def restart(area_values: dict):
    global turns
    for key in area_values:
        area_values[key] = None
    turns = 0


# Петля программы
def main_loop():
    print(hello)
    while True:
        command = input('enter the command ---> ')
        if command == 'start':
            restart(area_values)
            game_loop()
        elif command == 'help':
            print(help_txt)
        elif command == 'exit':
            break
        else:
            print(f'command "{command}" not found. Enter "help" to see list of commands')


main_loop()
