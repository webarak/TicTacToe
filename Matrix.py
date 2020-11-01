class Matrix(object):
    cols = 0
    rows = 0
    turn = 'x'
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        #initialize matrix and fill with zeroes
        self.matrix = []
        for i in range(rows):
            ea_row = []
            for j in range(cols):
                ea_row.append('')
            self.matrix.append(ea_row)

    def __setitem__(self, row, col, v):
        self.matrix[row-1][col-1] = v

    def __getitem__(self, row, col):
        return self.matrix[row-1][col-1]

    def CheckRow(self, row, v):
        w=1
        for i in range(self.cols):
            if not(self.matrix[row-1][i] == v):
                return 0
        return w

    def CheckCol(self, col, v):
        for i in range(self.rows):
            if not(self.matrix[i][col-1] == v):
                return 0
        return 1

    def CheckDiagonal(self, v):
        for i in range(self.rows):
            if not (self.matrix[i][i] == v):
                return 0
        return 1

    def CheckSeconderyDiagonal(self, v):
        for i in range(self.rows):
            if not (self.matrix[i][self.cols-i-1]==v):
                return 0
        return 1

    def __repr__(self):
        Str = " "
        for i in range(self.rows):
            for n in range(self.cols):
                Str += self.matrix[i][n] +' |'
            Str +='\n'
        return Str


if __name__ == '__main__':
    n = Matrix(3,3)
    n.__setitem__(1,1,'x')
    n.__setitem__(1,2,'x')
    n.__setitem__(1,3,'x')
    n.__setitem__(2,1,'x')
    n.__setitem__(2,2,'x')
    n.__setitem__(2,3,'x')
    n.__setitem__(3,1,'x')
    n.__setitem__(3,2,'x')
    n.__setitem__(3,3,'x')
    print(n)
    print(n.CheckDiagonal('x'))