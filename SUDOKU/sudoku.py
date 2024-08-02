from methods import method
"""
DOCSTRING
"""

def open_file():
    while True:
        file_name = input('Enter your file name: ')
        try:
            fp = open(file_name, 'r')
            return fp
        except FileNotFoundError:
            print('Error, the file name entered does not exist. Please try again.')

def get_data(fp):
    values = '123456789Xx'
    skip_lines = [1,2,3,4,8,12]
    data = []
    text = fp.readlines()

    #itterates through each line of file
    #adds only the numbers and 'xX' to list, skips specific lines 1,2,3,4,8,12 
    i = 0
    for line in text:
        i += 1
        row = []

        if i not in skip_lines:
            for char in line:
                if char in values:
                    if char in 'Xx':
                        row.append(['1','2','3','4','5','6','7','8','9'])
                    else:
                        row.append(char)  
            data.append(row)
    return data

def return_data(board):

    numbers = str(board).replace('\n','')
    #break line = --------|-------|--------
    counter = 1
    row_counter = 0
    output_file = 'output_data.txt'
    with open(output_file, 'w') as file:
        if 'x' in numbers:
            file.write('         SODOKU\nThe data submitted was unable to be solved completely, but is presented below.\n\n           ')
        else:
            file.write('         SODOKU\nThe data submitted was solved and presented below.\n\n           ')

        for char in numbers:
            file.write(f'{char} ')
            if counter % 3 == 0 and counter != 9:
                file.write('|')
            counter += 1
            if counter == 10:
                row_counter += 1
                file.write('\n           ')
                counter = 1
                if row_counter % 3 == 0 and row_counter != 9:
                    file.write('------|------|------\n           ')

def validate_data(data):
    #check that data contains 9 rows 
    if len(data) != 9:
        return False
    
    #check that data contains 9 columns
    for row in data:
        if len(row) != 9: #(checks for 18, becuase each number has a list associatd with it, 9 nums + 9 lists = len(18))
            return False
    return True

def validate_board(board):
    #checks that starting data fits sodokus rules
    for i in range(9):
        #utilize get item class attribute to selectively pull data
        column = board[i, 'n']
        row = board['n', i]
        box = board['b', i]

        #check for numbers occuring more than once in rows, columns, and boxes
        for j in range(1,10):
            if column.count(str(j)) > 1:
                print(f'Error in column {i + 1}: ')
                return False
            elif row.count(str(j)) > 1:
                print(f'Error in row {i + 1}: ')
                return False
            elif box.count(str(j)) > 1:
                print(f'Error in box {i + 1}: ')
                return False
    return True

def sole_candidate(board):
    did_something = False
    for i in range(9):
        for j in range(9):
            if type(board[j, i]) == list:
                box_n = 3 * (i // 3) + (j // 3)

                row = board['n',i]
                column = board[j,'n']
                box = board['B',box_n]
                for k in range(9):  #row
                    if type(row[k]) == str:
                        if row[k] in board[j,i]:
                            board[j,i].remove(row[k])
                            did_something = True

                    if type(column[k]) == str: #column
                        if column[k] in board[j,i]:
                            board[j,i].remove(column[k])
                            did_something = True

                    if type(box[k]) == str: #box
                        if box[k] in board[j,i]:
                            board[j,i].remove(box[k])
                            did_something = True
                if len(board[j,i]) == 1:
                    board.data[i][j] = board[j,i][0]
                    did_something = True
    return did_something 

def hidden_single(board):
    did_something = False

    for i in range(9): #get 9 rows
        row = board['n',i]
        column = board[i,'n']
        box = board['B',i]

        for j in range(1,10): #get numbers 1-9

            r_count = 0
            if str(j) not in row:# ignores counting for already solved numbers
                for k in range(9):
                    if type(row[k]) == list:
                        if str(j) in row[k]:
                            r_count += 1
                            last = k
                if r_count == 1:
                    board.data[i][last] = str(j)
                    did_something = True
            
            c_count = 0
            if str(j) not in column:
                for k in range(9):
                    if type(column[k]) == list and str(j) in column[k]:
                        c_count += 1
                        last = k
                if c_count == 1:
                    board.data[last][i] = str(j)
                    did_something = True

            b_count = 0
            if str(j) not in box:
                for k in range(9):
                    if type(box[k]) == list and str(j) in box[k]:
                        b_count += 1
                        last = k
                if b_count == 1:
                    x = 3 * (i % 3) + (last % 3)
                    y = 3 * (i // 3) + (last // 3)
                    board.data[y][x] = str(j)
                    did_something = True
    return did_something

'''
def naked pair test function

for ROW column and box

a,b = 'N', 'N'
if row contains more than two empty cells #
    if row.count(type(list)) >= 2:
    for thing in row:
        if thing == a,b:
            print('found') #remove all other occurences from 
        if thing == list and len(list) == 2:
            a,b = thing[0], thing[1]

            
    find two cells that share the same ONLY two possibilitys
    remove those possiblities from rest of row and box
'''

def main():
    #print introduction to users
    print('\n                             |SODOKU|\n')
    print('Enter the known numbers into the corresponding spots in your file')
    print('You can reference the template.txt file for help\n')

    #get file name
    fp = open_file()

    #extract sodoku data
    data = get_data(fp)

    #create board
    board = method(data)

    if validate_data == False:
        print('The data file provided does not contain valid data.')
        print('Make sure known numbers are in the correct spot, and unknowns are left as "x" (reference template.txt)')
    elif validate_board == False:
        print("The data provided does not meet sodoku's rule requirements, please check that numbers are in the correct spot")
    else: 
        print('The data file provided was validified,\n     look at file "output_data.txt" for the results.\n')
        #alternate between using sole candidate and hidden single solving stradegies
        #continue calling stradegy functions while at least 1 possibility is removed or candidate is solved for
        #once both functions have been called and no changes have been made, terminate program
            #this means the grid is either solved or unsolvable by programed stradegies
        while True:
            s_progress = sole_candidate(board)
            h_progress = hidden_single(board)
            if s_progress == False and h_progress == False:
                break
        return_data(board)

main()

#consider adding naked pair
#  