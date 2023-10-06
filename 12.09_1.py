#1. Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.
import numpy as np

import read_from_file

#почитай по поводу функции ZIP и транспонирование матрицы

#а так же сделай чтение из файла
r1 = np.array(read_from_file.read_matrix("r.txt"))
print(r1)
print(np.rot90(r1, -1))