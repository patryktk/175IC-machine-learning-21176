import numpy as np
import random
import statistics

array_1 = np.zeros(10)
array_3 = np.arange(10,50,1)
array_2 = np.ones(10)*5

matrix_1 = np.arange(9).reshape(3,3)
matrix_2 = np.identity(3)
matrix_3 = np.array([])
matrix_4 = np.arange(0.01, 1.01, 0.01).reshape(10,10)
matrix_5 = np.linspace(0,1,20)

matrix_6 = np.random.randint(1,25, size=(25))
matrix_6 = matrix_6.reshape(5,5)
m6_sum = matrix_6.sum()
m6_mean = matrix_6.mean()
m6_dev = np.std(matrix_6)
m6_suma_col = matrix_6.sum(axis = 0 )

matrix_7 = np.random.randint(100, size=(25))
m7_med = statistics.median(matrix_7)
m7_min = matrix_7.min()
m7_max = matrix_7.max()

matrix_8 = np.random.randint(100, size=(3,5))
m8_t = matrix_8.T

matrix_9 = np.random.randint(100, size=(4,3))
matrix_10 = np.random.randint(100, size=(4,3))
result_1 = matrix_9 + matrix_10

    
matrix_11 = np.random.randint(100, size=(3,5))
matrix_12 = np.random.randint(100, size=(5,3))
result_2 = np.matmul(matrix_11, matrix_12)

