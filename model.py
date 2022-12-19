import view

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

def index_parentheses(mi_list):
    index_list_open = []
    index_list_close = []
    for i in range(len(mi_list)):
        if mi_list[i] == '(':
            index_list_open.append(i)
        elif mi_list[i] == ')':
            index_list_close.append(i)
    print(f'index_list_open = {index_list_open}')
    print(f'index_list_close = {index_list_close}')
    if len(index_list_open) == len(index_list_close):
        index_pair = []
        temporary = index_list_open[0]
        for j in range(1, len(index_list_open)):

            if index_list_open[j] == (temporary + 1):
                temp = index_list_open[j-1]
                index_list_open[j-1] = index_list_open[j]
                index_list_open[j] = temp

            index_pair.append(index_list_open[j - 1])
            index_pair.append(index_list_close[j - 1])

            print(f'index_list_open = {index_list_open}')
            print(f'index_pair = {index_pair}')

            temporary = index_list_open[j]
        index_pair.append(index_list_open[j])
        index_pair.append(index_list_close[j])
        print(f'index_pair = {index_pair}')
        return index_pair
    else:
        mi_list = view.correct_expression()
        index_parentheses(mi_list)

def pair_parentheses(mi_list, index_pair):
    for i in index_pair:
        part_mi_list = []
        for j in range(len(mi_list)):

            if j == index_pair[i]:
                part_mi_list.append(mi_list[j])
            if index_pair[i] < j <= index_pair[i+1]:
                part_mi_list.append(mi_list[j])
        part_mi_list.remove(part_mi_list[0])
        part_mi_list.remove(part_mi_list[-1])
        print(f'part_mi_list = {part_mi_list}')
        return part_mi_list

def update_list(mi_list, index_pair):
    for i in index_pair:
        new_mi_list = []
        for j in range(len(mi_list)):

            if j < index_pair[i]:
                new_mi_list.append(mi_list[j])
            if j == index_pair[i]:
                new_mi_list.append('temp')
                print(f'new_mi_list = {new_mi_list}')
            if j > index_pair[i + 1]:
                new_mi_list.append(mi_list[j])
                print(f'new_mi_list = {new_mi_list}')
        print(f'new_mi_list = {new_mi_list}')
        mi_list = new_mi_list
        print(f'mi_listk = {mi_list}')

        break
    return mi_list

def correct_index_list(index_pair):

    index_pair.remove(index_pair[0])
    index_pair.remove(index_pair[0])
    print(f'index_pair = {index_pair}')
    return index_pair

def change_part_list(mi_list, calc):

    for i in range(len(mi_list)):
        if mi_list[i] == 'temp':
            mi_list[i] = calc[i]
    return mi_list
# def search_pair(mi_list,calc):
#
#     for i in range(len(in_list)):
#         print(i)


def composition(sm_list):

    while ('*' in sm_list) or ('/' in sm_list):
        item = 0
        while item < len(sm_list):
            if sm_list[item] == '*':
                sm_list[item-1] = sm_list[item-1] * sm_list[item + 1]
                sm_list.remove(sm_list[item])
                print(f'sm_list* = {sm_list}')
                print(f'item = {item}')
                sm_list.remove(sm_list[item])
                print(f'sm_list* = {sm_list}')
            elif sm_list[item] == '/':
                sm_list[item-1] = sm_list[item-1] / sm_list[item + 1]
                sm_list.remove(sm_list[item])
                print(f'sm_list/ = {sm_list}')
                print(f'item = {item}')
                sm_list.remove(sm_list[item])
                print(f'sm_list/ = {sm_list}')
            item += 1
            print(f'sm_list = {sm_list}')
    return sm_list


def sum_difference(stm_list):
    while ('+' in stm_list) or ('-' in stm_list):
        item = 0
        while item < len(stm_list):
            if stm_list[item] == '+':
                stm_list[item - 1] = stm_list[item - 1] + stm_list[item + 1]
                stm_list.remove(stm_list[item])
                print(f'stm_list+ = {stm_list}')
                stm_list.remove(stm_list[item])
                print(f'stm_list+ = {stm_list}')
            elif stm_list[item] == '-':
                stm_list[item - 1] = stm_list[item - 1] - stm_list[item + 1]
                stm_list.remove(stm_list[item])
                print(f'stm_list- = {stm_list}')
                stm_list.remove(stm_list[item])
                print(f'stm_list- = {stm_list}')

            item += 1
    return stm_list