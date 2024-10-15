class method(object):
    
    #initializes oject with 2d list as data attribute (sodoku data)
    def __init__(self, data):
        #3d list for (1-9) attatched to given numbers
        self.data = data

    #allows indexing to return specified individual, row, column, or box data
    def __getitem__(self, key):

        x, y = key

        #get singular item
        if type(x) == int and type(y) == int:
            return self.data[y][x]
        #get row 
        elif type(y) == int and x == 'n':
            row = []
            for num in self.data[y]:
                row.append(num)
            return row
        #get column
        elif type(x) == int and y == 'n':
            column = []
            for i in range(9):
                column.append(self.data[i][x])
            return column
        #get box
        else:
            box = []
            centers = [(1,1), (4,1), (7,1), (1,4), (4,4), (7,4), (1,7), (4,7), (7,7)]
            cx, cy = centers[y]
            for i in range(-1,2):
                for j in range(-1,2):
                    box.append(self.data[cy + i][cx + j])
            return box

    #creates string of raw number data
    def __str__(self):
        display = ''
        for row in self.data:
            for num in row:
                if len(str(num)) == 1:
                    display += str(num)
                else:
                    display += 'x'
            display += '\n'
        return display
