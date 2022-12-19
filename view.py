import model

def input_number():
    start_number = int(input('Введите начальное число: '))
    return start_number

def input_new_number():
    next_number = int(input('Введите следующее число: '))
    return next_number

def input_operation():
    operat = input('Введите какую математическую операцию необходимо сделать +, -, *, /, =: ')
    return operat

def conclusion_result(final):
    print(f'Ваш результат вычислений: {final}\n')

def creaty_list():
    my_list = input('Введите данные задачи: ')
    return my_list

def correct_expression():
    my_list = input('Введите условия задачи корректно: ')
    return my_list
