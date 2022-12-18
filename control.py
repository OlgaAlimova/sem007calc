import model
import view
import logger

def calculator_func(mi_list):

    nov_list = model.list_num_creaty(mi_list)
    print(f'nov_list = {nov_list}')
    calc_step = model.composition(nov_list)
    print(f'calc_step = {calc_step}')
    calculator = model.sum_difference(calc_step)
    logger.logger_str(mi_list, calculator)
    return calculator

def start_calculator():

    global start_number
    global intermediate_result

    intermediate_result = model.set_intermediate_result(start_number)
    print(f'intermediate_result = {intermediate_result}')
    operation = view.input_operation()

    while operation != '=':

        first = model.get_intermediate_result()
        print(f'first = {first}')
        model.set_next_number(view.input_new_number())
        second = model.get_next_number()
        oper = operation
        model.play_operation(operation)
        res = model.get_intermediate_result()
        view.conclusion_result(model.get_intermediate_result())
        logger.logger(first, second, oper, res)
        operation = view.input_operation()

    view.conclusion_result(model.get_intermediate_result())


def start_work():
    my_list = view.creaty_list()
    start_value = model.data_verification(my_list)
    print(f'start_value = {start_value}')
    print(type(start_value))
    if type(start_value) == list:
        calculator_func(my_list)
    else:
        global start_number
        start_number = model.set_start_number(start_value)
        print(f'start_number = {start_number}')
        start_calculator()

