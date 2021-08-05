from Inheritance import Player


fields = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
def drawBoard(fields):
    for row in range(13):
        if row%2 == 0:
            prow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    pcolumn = int(column/2)
                    tile = fields[pcolumn][prow]
                    if column != 12:
                        print(tile,end="")
                    else:
                        print(tile)
                else:
                    print("|",end="")
        else:
            print("-------------")
    print("/n")

def updateBoard(num,player):
    column = fields[num]
    index = ""
    reversedColumn = column[::-1]
    for row in reversedColumn:
        if row == " ":
            index = reversedColumn.index(row)
            reversedColumn[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = reversedColumn[::-1]
    fields[num] = column
    drawBoard(fields)
    return True

def fourInRow():
    winner = False
    for column in fields:
        counter = 0
        length = len(column)
        for i in range(1,length):
            if column[i-1] != " " and column[i] != " " and column[i-1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i-1]
                return winner
    return winner

def fourInColumn(column_matrix):
    winner = False
    for column in column_matrix:
        counter = 0
        length = len(column)
        for i in range(1,length):
            if column[i-1] != " " and column[i] != " " and column[i-1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i-1]
                return winner
    return winner

def fourInForwardDiagonal(column_matrix,player):
    for i in range(0,len(column_matrix)):
        for j in range(0,len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i+1][j-1] == player and column_matrix[i+2][j-2] == player and column_matrix[i+3][j-3] == player:
                    return True
            except IndexError:
                next
    return False

def fourInReverseDiagonal(column_matrix,player):
    for i in range(0,len(column_matrix)):
        for j in range(0,len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i+1][j+1] == player and column_matrix[i+2][j+2] == player and column_matrix[i+3][j+3] == player:
                    return True
            except IndexError:
                next
    return False

def isValidMove(column_no):
    if column_no >= 1 and column_no <= 7:
        return True
    else:
        return False

def createColumnMatrix():
    column_matrix = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
    for i in range(7):
        for j in range(len(fields[i])):
            column_matrix[i][j] = fields[i][j]
    return column_matrix

def start():
    player = 1
    no_win = True
    winner = ""
    while(no_win):
        column_no = int(input("Enter the column\n"))
        if column_no:
            if isValidMove(column_no) == False:
                print("This is not a right move")
            else:
                updated_flag = updateBoard(column_no-1,player)
                if updated_flag:
                    print("")
                    current_player = player
                    tile = "X" if player == 1 else "O"
                    player = 2 if player == 1 else 1
                    winner = fourInRow()
                    if winner:
                        no_win = False
                    else:
                        column_matrix = createColumnMatrix()
                        winner = fourInColumn(column_matrix)
                        if winner:
                            no_win = False
                        elif fourInReverseDiagonal(column_matrix,tile):
                            winner = current_player
                            no_win = False
                        elif fourInForwardDiagonal(column_matrix,tile):
                            winner = current_player
                            no_win = False
                else:
                    print("This is not a roght move")
        else:
            print("This is not a roght move")

    if winner == "X":
        winner = "1"
    else:
        winner = "2"
    print('THE WINNER IS PLAYER '+ str(winner))


print('Starting Connect 4 Game... Get ready!\n')

drawBoard(fields)
start()
