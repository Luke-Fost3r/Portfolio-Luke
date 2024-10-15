from methods import method

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
                        row.append([1,2,3,4,5,6,7,8,9])
                    else:
                        row.append(int(char))  
            data.append(row)
    return data

def return_data(board):

    numbers = str(board).replace('\n','')
    counter = 1
    row_counter = 0
    output_file = 'output_data.txt'
    #open output file and write the board in formated format
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
            if column.count(j) > 1:
                print(f'Error in column {i + 1}: ')
                return False
            elif row.count(j) > 1:
                print(f'Error in row {i + 1}: ')
                return False
            elif box.count(j) > 1:
                print(f'Error in box {i + 1}: ')
                return False
    return True

def sole_candidate(board):
    #as long as function removes a single candidate from any cell, did_something will be true
    did_something = False
    for i in range(9):
        for j in range(9):
            if type(board[j, i]) == list:
                box_n = 3 * (i // 3) + (j // 3) #get box number from coordinates

                #utilize class get_item method to get lists of row, column, and box
                row = board['n',i]
                column = board[j,'n']
                box = board['B',box_n]

                #itterate through list and remove al possible candidates
                for k in range(9):  #row
                    if type(row[k]) == int:
                        if row[k] in board[j,i]:
                            board[j,i].remove(row[k])
                            did_something = True

                    if type(column[k]) == int: #column
                        if column[k] in board[j,i]:
                            board[j,i].remove(column[k])
                            did_something = True

                    if type(box[k]) == int: #box
                        if box[k] in board[j,i]:
                            board[j,i].remove(box[k])
                            did_something = True
                #if a cell is unsolved yet contains one possibility, set it to that possibility
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

            #count number of candidate occurences
            r_count = 0
            if j not in row:# ignores counting for already solved numbers
                for k in range(9):
                    if type(row[k]) == list:
                        if j in row[k]:
                            r_count += 1
                            last = k
                #if number only occurs once, set cell to said num
                if r_count == 1:
                    board.data[i][last] = j
                    did_something = True
            #same as above for column, and box
            c_count = 0
            if j not in column:
                for k in range(9):
                    if type(column[k]) == list and j in column[k]:
                        c_count += 1
                        last = k
                if c_count == 1:
                    board.data[last][i] = j
                    did_something = True

            b_count = 0
            if j not in box:
                for k in range(9):
                    if type(box[k]) == list and j in box[k]:
                        b_count += 1
                        last = k
                if b_count == 1:
                    x = 3 * (i % 3) + (last % 3)
                    y = 3 * (i // 3) + (last // 3)
                    board.data[y][x] = j
                    did_something = True
    return did_something

def naked_pair(cells): #cells is a list being a column, row, or box
    did_something = False
    unsolved = 0

    #count unsolved values, at least 2 required for pair to be possible
    for value in cells:
        if type(value) == list:
            unsolved += 1
    if unsolved > 2:
        #find pair
        for j in range(9):
            candidates = cells[j]

            #check if a cell contains two possibilitys
            if type(candidates) == list and len(candidates) == 2:
                if cells.count(candidates) == 2:
                    a,b = candidates[0], candidates[1]
                    
                    #remove all occurences of a and b
                    for value in cells:
                        if type(value) == list and len(value) != 2:
                            if a in value:
                                value.remove(a)
                                did_something = True
                            if b in value:
                                value.remove(b)
                                did_something = True
    return did_something

def hidden_pair(cells):
    did_something = False
    counts = [0,0,0,0,0,0,0,0,0]
    pair = []
    unsolved = 0

    #itterate through row column or box; check that pair is possible via more than two open cells
    for value in cells:
        if type(value) == list:
            unsolved += 1
    if unsolved > 2:

        for i in range(9):
            candidates = cells[i]
            if type(candidates) == list:
                for num in candidates:
                    counts[num - 1] += 1
        print("counts",counts)
        if counts.count(2) >= 2:
            #identify numbers to look for and remove non possible candidate for pair
            for i in range(9):
                if counts[i] == 2:
                    pair.append(i + 1) #this adds (1-9) the actuall number in the pair we are looking for to array

            s = 0
            a,b = pair[0], pair[1]
            for value in cells:
                if type(value) == list and a in value and b in value:
                    #we have found half a pair
                    s += 1
            
            if s == 2:
                #naked pair found
                #this means those two nums are unique to this row/column/box, 
                #    if any cell in this row contains such nums, we can remove all other candidates
                for i in range(9):
                    if type(cells[i]) == list and a in cells[i]:
                        if cells[i] != [a, b]:
                            did_something = True
                            cells[i][:] = [a, b] # [:] is necasary to modify list in place, or scope of changes end when function ends
    return did_something

def pairs(board,data):
    changed = []
    #for naked pair
    for i in range(9):
        changed.append(naked_pair(board['n',i])) #row
        changed.append(naked_pair(board[i,'n'])) #column
        changed.append(naked_pair(board['B',i])) #box

    #for hidden pair
    for i in range(9):
        changed.append(hidden_pair(board['n',i])) #row
        changed.append(hidden_pair(board[i,'n'])) #column
        changed.append(hidden_pair(board['B',i])) #box

    if True in changed:
        return True
    return False

def main():
    #print introduction to users
    print('\n                             |SODOKU|\n')
    print('Enter the known numbers into the corresponding spots in your file')
    print('You can reference the template.txt file for help\n')

    #get file name
    fp = open_file()

    #extract sodoku data
    data = get_data(fp)

    #create board object
    board = method(data)

    print(board)

    if validate_data(data) == False:
        print('The data file provided does not contain valid data.')
        print('Make sure known numbers are in the correct spot, and unknowns are left as "x" (reference template.txt)')
    elif validate_board(board) == False:
        print("The data provided does not meet sodoku's rule requirements, please check that numbers are in the correct spot")
    else: 
        print('The data file provided was validified,\n     look at file "output_data.txt" for the results.\n')

        #sole candidate and hidden candidate must be seperate from other removal stradegies
        #     pair stradegys need fully updated data, in order to run without error
        while True:
            while True:
                s_progress = sole_candidate(board)
                h_progress = hidden_single(board)
                if s_progress == False and h_progress == False:
                    break

            p_progress = pairs(board,data)
            if p_progress == False:
                break
    return_data(board)

main()
