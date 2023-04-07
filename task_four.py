# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    __matrix_data = [[]]
    __matrix_x_size = 0
    __matrix_y_size = 0

    def __init__(self, matrix_data):
        self.__matrix_data = matrix_data
        self.__matrix_x_size = len(matrix_data)
        self.__matrix_y_size = len(matrix_data[0])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise RuntimeError("Wrong type of data for other matrix")

        if self.__matrix_x_size != other.__matrix_x_size and self.__matrix_y_size != other.__matrix_y_size:
            raise RuntimeError("Matrix sizes is not the same")

        matrix_data = [[0 for x in range(self.__matrix_y_size)] for y in range(self.__matrix_x_size)]
        for i in range(self.__matrix_x_size):
            for j in range(self.__matrix_y_size):
                matrix_data[i][j] = self.__matrix_data[i][j] + other.__matrix_data[i][j]

        return Matrix(matrix_data)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix_data])


matrix1 = Matrix([[1, 2, 3], [3, 4, 5]])
print(matrix1, "\n")

matrix2 = Matrix([[1, 2, 3], [3, 4, 5]])
print(matrix2, "\n")

print(matrix1 + matrix2, "\n")
