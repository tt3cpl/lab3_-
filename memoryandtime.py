import subprocess
import resource
import time

path = 'ex_7.py'
subprocess.call(['python3', path])

usage = resource.getrusage(resource.RUSAGE_CHILDREN)
max_memory= usage.ru_maxrss / 1024 / 1024

print(f'память равна: {round(max_memory,2 )} мБ')


start_time = time.time()

import ex_1

end_time = time.time()


execution_time = end_time - start_time

print(f'Время выполнения программы: {execution_time} секунд')