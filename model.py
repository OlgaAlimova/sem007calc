
start_number = 0
next_number = 0
intermediate_result = start_number
final_result = intermediate_result


list_operation = ['+', '-', '=']
list_priority_operation = ['*', '/']

def summa_numbers():
    global next_number
    global intermediate_result
    global start_number
    intermediate_result = start_number + next_number
    start_number = intermediate_result
    return intermediate_result

def difference_numbers():
    global next_number
    global intermediate_result
    global start_number
    intermediate_result = start_number - next_number
    start_number = intermediate_result
    return intermediate_result

def product_numbers():
    global next_number
    global intermediate_result
    global start_number
    intermediate_result = start_number * next_number
    start_number = intermediate_result
    return intermediate_result

def dividing_numbers():
    global next_number
    global intermediate_result
    global start_number
    intermediate_result = start_number / next_number
    start_number = intermediate_result
    return intermediate_result

def play_operation(operat):
    if operat == '*':
        product_numbers()
    elif operat == '/':
        dividing_numbers()
    elif operat == '+':
        summa_numbers()
    elif operat == '-':
        difference_numbers()
    return intermediate_result

def set_start_number(num):
    global start_number
    start_number = num
    return start_number

def get_start_number():
    global start_number
    return start_number

def set_next_number(num):
    global next_number
    next_number = num
    return next_number

def get_next_number():
    global next_number
    return next_number

def set_intermediate_result(num):
    global intermediate_result
    intermediate_result = num
    return intermediate_result

def get_intermediate_result():
    global intermediate_result
    return intermediate_result

def set_final_result(num):
    global final_result
    final_result = num
    return final_result

def get_final_result():
    global final_result
    return final_result

def lenght_list(mi_list):
    count = 0
    for i in range(len(mi_list)):
        count += 1
    return count

def data_verification(mi_str):
    for i in mi_str:
        if i in list_operation or i in list_priority_operation:
            mi_list = list(mi_str)
            starting_value = mi_list
            break
    else:
        starting_value = int(mi_str)
    return starting_value

def list_num_creaty(mi_list):
    new_list = []
    count = 0
    list_letter_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(mi_list)):
        if mi_list[i] in list_letter_num:
            new_list.append(int(mi_list[i]))
        else:
            new_list.append(mi_list[i])
    print(f'new_list = {new_list}')
    list_red = [new_list[0]]
    for j in range(1, len(new_list)):
        if (new_list[j - 1] in list_numbers) and (new_list[j] in list_numbers):
            num = int(new_list[j - 1] * 10 + new_list[j])
            list_red.pop(j - 1)
            list_red.append(int(num))
        else:
            list_red.append(new_list[j])
        count += 1
    print(f'list_red = {list_red}')
    print(f'count = {count}')
    return list_red
    # print(*list_red, sep='')

def composition(mi_list):

    while ('*' in mi_list) or ('/' in mi_list):
        item = 0
        while item < len(mi_list):
            if mi_list[item] == '*':
                mi_list[item-1] = mi_list[item-1] * mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list* = {mi_list}')
                print(f'item = {item}')
                mi_list.remove(mi_list[item])
                print(f'mi_list* = {mi_list}')
            elif mi_list[item] == '/':
                mi_list[item-1] = int(mi_list[item-1] / mi_list[item + 1])
                mi_list.remove(mi_list[item])
                print(f'mi_list/ = {mi_list}')
                print(f'item = {item}')
                mi_list.remove(mi_list[item])
                print(f'mi_list/ = {mi_list}')

            item += 1
    return mi_list

def sum_difference(mi_list):
    while ('+' in mi_list) or ('-' in mi_list):
        item = 0
        while item < len(mi_list):
            if mi_list[item] == '+':
                mi_list[item - 1] = mi_list[item - 1] + mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list+ = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list+ = {mi_list}')
            elif mi_list[item] == '-':
                mi_list[item - 1] = mi_list[item - 1] - mi_list[item + 1]
                mi_list.remove(mi_list[item])
                print(f'mi_list- = {mi_list}')
                mi_list.remove(mi_list[item])
                print(f'mi_list- = {mi_list}')

            item += 1
    return mi_list