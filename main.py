import logging # Стандартна бібліотека для логування перебігу програми
logging.basicConfig(level = logging.DEBUG,
                    filename = 'logs.log',
                    filemode = 'w',
                    format ='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
logging.info('info')
logging.error('error')
logging.warning('warning')
logging.critical('critical')
try:
    print(10/0)
except Exception:
    logging.exception('Помилка(')
#Факторіал числа

def factorial(n):
    logging.info(f'озочато обчислення факторіалу числа {n}')
    result = 1
    for i in range(1, n + 1):
        result *= i #1*2*3....
    logging.info(f'озочато обчислення факторіалу числа завершено {n}. Результата виконання {result}')
    return result
logging.basicConfig(level = logging.INFO)
print(factorial(5))