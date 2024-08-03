# Portfolio-Luke
A collection of my current projects on my journey to become a computer scientist, feel free to explore, and see how I approached different problems



TETRIS (lukes version)

Important to note;
this project utilizes pygame; most importantly for an easy built in game clock (set at 60 ticks per second), and keyboard detection function.
many 'surfaces' are defined, and used for 'screen.blit(surface)' which take up many lines of simple variable definition and display statments, but are crucial for the arcade style graphics of this program. 
This program is split into two main files for orginization and readaility purposes, main.py and extra.py; the main file consists of all of pygames commands including the gameclock and keyboard input detection loop, while the extra function handles most of the data and altering of said data.

Overveiw;
When the program is run, the start() function is called, displaying a button surface, and entering a while loop to detect for the space key. Once pressed a button push animation is prompted, along with breaking from the loop, and calling to the main control() function.


The control function defines the initial speed, score, and blank 2 dimensional list representing the grid which contains the tetromino coordinates. Any of the 7 peices are chosen by calling the random.randint() from 0-6. using this generated integer, the information for any peice is grabbed by calling to the peice_info() function which returns a list representing the starting coordinates of each block unit in a peice, the color title, and peices status which is either 'N' for no action, or 'S' meaning the peice must be set.
Once starting variables are initialized, the main game loop begins, which constantly checks for the following keyboard actions;


LEFT: Calls to move_peice() function passing the peice data, x movement instructions of -1, y movement instructions of 0, and the peice map defined previously as a 2d list.

RIGHT: Simaler to when left key stroke is detected except the x movement instruction is 1.

DOWN: Also same as previous key detections, exception being x instructions at 0, with y instructions at 1.

SPACE: begins loop of repreatedly calling move_peice function with downward instruction of y = 1, until a collision is detected which breaks from loop.

UP: calls to rotate_peice() function which utilizes a rotation formula for each block unit in a peice, where the rotation point is the second coordinate in each tetominos list of coordinates.

For each of the above keystokes, the coordinates before movement are held in a placeholder variable, then the coordinates are adjusted, passed to the check_collision() function, so that if a collision is detected the changed coordinates are discarded and the placeholder is returned. A peice is never set due to a horizontal collision, the status of the peice is only updated to 'S' if a vertical collision is found.
If the current peice's status is set at 'S', a freeze variable is set at true, which ensures that no more keydetection is used until the peice is finished setting, and all coresponding functions have completed there task. This variable was key to eliminating bugs such as unexpected peice behavior when keystrokes where pressed the instant the program was attempting to set a peice. Once freeze is true, the score is increased, and the set_peice() function is called, which stores the color of the tetrominos blocks for each of their coordinates for later graphic desplay. Next, the clear_row() function is called, checks to see if the peice map grid has a full row, and if so brings all data from above rows down one row towards the cleared row. Then the player_dead() function is called that checks if the set peices current coordinates are out of bounds of the peice map; if so, the control loop is exited, and simaler to the start() function a dead_restart() function is called which displays a restart button animation if space is detected, and calls back to control function restarting the game. Finally new peice_data is retrieved, the speed of the game is updated based on the height of the score variable, and freeze is set to false allowing keydetection to start again.


Outside of the keydetection in this control() function an x variable counts each tick of the 60 ticks per second game clock. If x becomes equal to the speed variable, an automatic downards move of the peice is called. Essentailly speed becomes a lower and lower number as the score increases, meaning x reaches the same value of the speed value quicker as the game goes on resulting in the increased automatic downwards movement of the game making it harder and harder to stay alive.
Each time x reaches the speed variable, representing a move occuring, the display_peice(), blit_grid(), display_background(), blit_score(), blit_onhold(), and pygame.display.update() are called sequentially, updating the graphics the following; the current peice is displayed using its peice data and color, the grid lines are displayed over the peice, the background is then displayed which includes the title, the score is displayed over the background, the upnext peice is displayed in a box over the background, and then all graphic updates to the game window are updated calling to pygame.


###########################################################################################################################################################################################


SUDOKU SOLVER

Important to note; This program consists of four important files, sudoku.py which contains the solving stradegies, methods.py containing the class method which most importantly utilizes the __getitem__ special method and removes a huge amount of redundancy from the program, then finnaly the data.txt, and output.txt which contain the starting unsolved sudoku, and the solved product data of the program.

Overview;
A file pointer is retrieved by calling the open_file() function. This function repeatedly asks the user for a file name until the file is succesfully opened and the fp is returned to main().
The sodoku data is retrieved, by calling get_data(). Using the file pointer, the file is read line by line, and the numbers and blank spaces are extracted and appended to a 2d list representing the unsolved sudoku board, with each unsolved value a list of all nine possibilites.

Next a board object is created by calling the method() class. Method(), initializes itself with the data extracted, includes a printing method which returns a string of the data, and most importanty contains the get_item special method. This method allows the program to pull specific row, column, or box lists from the data by stating board[a,b]. If both a and b are integers, a single number is returned representing x,y coordinates of the number. If only b is provided, than a row is returned. If only a is provided a column is returned. If b is provided with a being some character, than that number b, box is returned.

Next validate_data() and validate_board() are called. validate_data() returns false if the input file given by the user contains not enough data, or inproper data. validate_board() returns false if the data inputed by the user does not meet the rules of sudoku.
If the data entered is validated, then a loop is entered which repeatedly calls to the two solving stradegies;

Sole_candidate(): This stradigy itterates through each list of rows, columns and boxes. For each solved value in a list, that value is removed from the possibilities list. At any point during this proccess, if a list conatains a possibilities list with only one possibiliite, that value is filled in for that spot.
hidden_single(): This stradegy itterates through every list of rows, columns, and boxes aswell. For each list, a count of all the possibilities is made. If any number has only a count of one, that value is filled in for that spot.

As long as at least one possibilitie is crossed of, or one unit is solved in that itteration. Once this is not the case, return_data() is called which checks to see if the board was able to be completed, formats the data along with a message to the user, and opens a file with that data.
