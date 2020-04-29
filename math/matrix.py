class Matrix:
    """The class is an implementation of the mathematical concept of matrix."""

    def __init__(self, data_set):
        """Create a new matrix instance."""
        self._matrix = data_set
        self._rows = len(self._matrix)
        self._columns = len(self._matrix[0])

    def __str__(self):
        """Return the string representation of the matrix."""
        return str(self._matrix)

    def __repr__(self):
        """Return the representation of the matrix."""
        return f"{self.__class__.__name__}({self._matrix})"
        
    def __getitem__(self, indexes):
        """Return the element of the matrix with specified indexes"""
        return self._matrix[indexes[0]][indexes[1]]

    def __setitem__(self, indexes, value):
        """Set the value of the element at indexes indexes."""
        self._matrix[indexes[0]][indexes[1]] = value

    def __add__(self, other):
        """Return the result of the two matrix addition."""
        if self._rows != other._rows or self._columns != other._columns:
            raise ValueError("Can't add matricies with different dimensions.")
        result = []
        for line0, line1 in zip(self._matrix, other._matrix):
            result.append([i + j for i, j in zip(line0, line1)])
        return self.__class__(result)

    def __mul__(self, other):
        """Return the result of matrix multiplication."""
        if self._columns != other._rows:
            raise ValueError("Inappropriate sizes of matricies.")
        product = self.__class__(
            [[0] * other._columns for i in range(self._rows)]
        )
        for i in range(self._rows):
            for j in range(other._columns):
                product[i,j] = sum(
                    self[i, k] * other[k, j] for k in range(self._columns)
                )
        return product


if __name__ == "__main__":
    matrix0 = Matrix([[1, 2,], [3, 4,]])
    matrix1 = Matrix([[2, 1, 3,], [0, 0, 1,]])
    print(matrix0 + matrix1)
