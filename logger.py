from datetime import datetime as dt
path = 'log.txt'
def logger(first, second, oper, res):
    log = f'{dt.now()} | {first} {oper} {second} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)

def logger_str(mi_list, calc):
    log = f'{dt.now()} | {mi_list}  = {calc}\n'
    with open(path, 'a') as data:
        data.write(log)