class Matrix:
    """Создали класс Matrix, внутри прописали функции:
    – вывода на печать,
    – сравнения матриц,
    – сложения матриц,
    – умножения матриц."""

    def __init__(self, matrix):
        """Проверяем и инициализируем матрицу"""
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError('Invalid matrix')
        self.matrix = matrix


    def __str__(self):
        """Удобный вывод результата для пользователя"""
        return '\n'.join(('\t'.join(map(str, row)) for row in self.matrix))


    def __eq__(self, other: "Matrix"):
        """Проверяет на равенство матрицы"""
        return self.matrix == other.matrix


    def __add__(self, other: "Matrix"):
        """Функция сложения двух матриц (сперва проверяем, что матрицы можно сложить)"""
        if len(self.matrix) != len(other.matrix) \
                or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('The length of the two matrices is not equal')
        result = [[self.matrix[i][j] + other.matrix[i][j]
                   for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result


    def __mul__(self, other: "Matrix"):
        """Функция умножения двух матриц (сперва проверяем, что матрицы можно умножить)"""
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Number of columns first matrix is not equal number of lines second matrix')
        result = [[sum(self.matrix[i][k] * other.matrix[k][j]
                       for k in range(len(self.matrix[0])))
                   for j in range(len(other.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [2, 1]])
    print(m1)
    print('–––––')
    m2 = Matrix([[1, 2], [2, 3]])
    print(m2)
    print('–––––')
    print(f'equal: {m1 == m2}')
    print('–––––')
    print('add:')
    print(Matrix(m1 + m2))
    print('–––––')
    print('mul:')
    print(Matrix(m1 * m2))