import random

# Creating the empty 9x9 matrix
sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def check_row(n, i):

    '''The function checks weather n can be placed in row i.
    Returns True if it can be placed'''

    for k in range(9):
        if n == sudoku[i][k]:
            return False
    return True


def check_column(n, j):

    '''The function checks weather n can be placed in column j.
        Returns True if it can be placed'''

    for l in range(9):
        if sudoku[l][j] == n:
            return False
    return True


def check_box(n, i, j):

    '''The function checks weather it is safe to place the number n in the 3x3 grid containing the cell (i,j)
        Returns True if it can be placed'''

    for k in range(3 * (i // 3), 3 * (i // 3) + 3):
        for l in range(3 * (j // 3), 3 * (j // 3) + 3):
            if n == sudoku[k][l]:
                return False
    return True


def fillPosition(i, j):
    global sudoku

    '''Checking weather the cell already contains a number
    If it does, the function calls itself on the next cell and return what the next cell has returned'''

    if sudoku[i][j] != 0 and sudoku[i][j] != ' ':
        if j < 8:
            return fillPosition(i, j + 1)
        elif i < 8 and j == 8:
            return fillPosition(i + 1, 0)
        else:
            return True
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(l) > 0:
        n = random.choice(l)  # Getting a random number from the list and deleting that element from the list
        l.remove(n)
        if check_row(n, i) and check_column(n, j) and check_box(n, i, j):  # Checking if n can be placed in cell (i,j)
            sudoku[i][j] = n
            if j < 8:
                if fillPosition(i, j + 1):
                    return True
            elif i < 8 and j == 8:
                if fillPosition(i + 1, 0):
                    return True
            else:
                return True
    sudoku[i][j] = 0
    return False  # Returning False if no n can be placed in (i,j)


def delete_elements(m):

    '''Deletes m elements from Sudoku'''

    global sudoku
    k = 0
    while k < m:
        i = random.randrange(0, 9)
        j = random.randrange(0, 9)
        if sudoku[i][j] != ' ':
            sudoku[i][j] = ' '
            k += 1


fillPosition(0, 0)
difficulty = int(input('Enter difficulty level:\n1.Easy\n2.Medium\n3.Hard\nEnter your choice: '))
if difficulty == 1:
    delete_elements(35)
elif difficulty == 2:
    delete_elements(45)
elif difficulty == 3:
    delete_elements(55)
else:
    print('Bad Input')
    exit()

line = ''  # Creating a line
for i in range(35):
    line += '-'

for i in range(9):
    row = ''
    for j in range(9):
        if j == 3 or j == 6:
            row = row + ' | ' + str(sudoku[i][j])
        else:
            row = row + '   ' + str(sudoku[i][j])
    print(row[2:])
    if i == 2 or i == 5:
        print(line)

fillPosition(0, 0)  # Solvin the generated Sudoku
print('\nThe corresponding solution is')
for i in range(9):
    row = ''
    for j in range(9):
        if j == 3 or j == 6:
            row = row + ' | ' + str(sudoku[i][j])
        else:
            row = row + '   ' + str(sudoku[i][j])
    print(row[2:])
    if i == 2 or i == 5:
        print(line)
