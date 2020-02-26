class ChessBoard:
    def __init__(self, size):
        self.size = size
        self.columns = []

# place in next row
    def next_row(self, column):
        self.columns.append(column)

# remove from current row
    def remove_row(self):
        return self.columns.pop()
 
    def check_column(self, column):
        row = len(self.columns)
 
 # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False
# check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
# check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row == (self.size - column) - row):
                return False
 
        return True
 
    def print_board(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print("♛", end=' ')
                else:
                    print("*", end=' ')
            print()
  
def compute(size, sol):
    board = ChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0

# printing N number of solutions
    while number_of_solutions < sol:
# iterate over different solutions
        while column < size:
            if board.check_column(column):
                board.next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        if (column == size or row == size):
            if row == size:
                board.print_board()
                print()
                number_of_solutions += 1
                board.remove_row()
                row -= 1
# Backtracking
            try:
                prev_column = board.remove_row()
            except IndexError:
                break
            row -= 1
            column = 1 + prev_column

N = 20
print("Welcome to the 20 Queens Program!\n")
sol = int(input("[?] How many solutions do  you want to print? "))
print()
compute(N, sol)