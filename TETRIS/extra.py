def peice_info(num):
    colors = ["yellow", "cyan3", "red", "orange", "blue", "purple", "green"]
    #rotate about second coordinate value (excluding O)
    O = [[4,0],[5,0],[4,1],[5,1]]
    I = [[4,0],[4,1],[4,2],[4,3]]
    S = [[5,0],[5,1],[6,0],[4,1]] 
    L = [[4,0],[4,1],[4,2],[5,2]]
    J = [[5,0],[5,1],[5,2],[4,2]]
    T = [[4,1],[5,1],[6,1],[5,0]]
    Z = [[4,0],[5,0],[5,1],[6,1]]
    peices = [O, I, S, L, J, T, Z]

    #peice coordinates, peice color, peice status
    return [peices[num].copy(), colors[num],'N']

def clear_row(peice_map):
    rows_cleared = 0
    for i in range(17):
        row = peice_map[i]
        #if row is full
        if 0 not in row:
            for j in range(i):
                #move all contents down one
                peice_map[i-j] = peice_map[i-(j+1)]
            #top most row set to empty
            peice_map[0] = [0,0,0,0,0,0,0,0,0,0]
            rows_cleared += 1
    return (rows_cleared ** 2) * 10

#if a peice is set out of bounds, return dead
def player_dead(peice_data):
    coordinates = peice_data[0]
    for x,y in coordinates:
        if y < 4:
            return True
    return False

#set peice on map, will then be displayed in location unlessed row is cleared
def set_peice(peice_data,peice_map):
    coordinates = peice_data[0]
    color = peice_data[1]
    for x,y in coordinates:
        y = y - 4
        peice_map[y][x] = color

def check_collision(x,y,dx,dy,peice_map):
    #wall collisions
    if not 0 <= x <= 9:
        return 'H'  #horizontal collision
    elif not y <= 20:
        return 'V'  #vertical collision

    #peice on peice collision
    if y >= 4 and peice_map[y-4][x] != 0:
        if dx != 0:
            return 'H'
        elif dy != 0:
            return 'V'
        else:
            return True
    return False

def move_peice(peice_data, dx, dy, peice_map):
    holder = peice_data[0].copy()
    for i in range(4):
        x,y = holder[i]
        #applys move to copy
        x,y = x + dx, y + dy
        holder[i] = [x,y]
        status = check_collision(x,y,dx,dy,peice_map)
        #if move is valid, transfered to original data, else the copy is discarded
        if status != False:
            if status == 'V':
                #if move causes downwards collision, mark peice to be set
                peice_data[2] = 'S'
            return peice_data
    peice_data[0] = holder.copy()
    return peice_data

def rotate_peice(peice_data, dx, dy, peice_map):
    if peice_data[1] != 'yellow': #square peice does not rotate
        holder = peice_data[0].copy()
        a,b = holder[1]
        for i in range(4):
            x,y = holder[i]
            #rotates around given axis (second coordinate in list)
            x,y = -(y - b) + a, (x - a) + b 
            holder[i] = [x,y]
            #if move causes collision, copy is discarded
            if check_collision(x,y,dx,dy,peice_map):
                return peice_data
        peice_data[0] = holder.copy()
    return peice_data

def tela_peice(peice_data, peice_map):
    #when space is pressed, a downward move of the peice is applied repeatedly until collision
    while peice_data[2] == 'N':
        peice_data = move_peice(peice_data, 0, 1, peice_map)
    return peice_data
    
