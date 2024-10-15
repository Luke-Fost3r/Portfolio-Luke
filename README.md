# Portfolio-Luke
A collection of my current projects on my journey as a computer scientist, feel free to explore, and see how I approached different problems


Disciplined and driven Computer Science student with a love for writing code and a fascination for
machine/deep learning and algorithm design. Eager to understand and approach the complex computational
problems of the future and contribute to cutting-edge research. Attempting to opportunities to expand my knowledge and skills, and eventually pursue a PhD in the field of computer science.

Some of my major inspirations include Alan Turing, Ada Lovelace, science fiction (hyperion), and ai philosophy. 



TETRIS (Luke's version)

Important to note; this project utilizes pygame; most importantly for an easy built in game clock (set at 60 ticks per second), and keyboard detection function. Many 'surfaces' are defined, and used for 'screen.blit(surface)' which take up many lines of simple variable definition and display statements, but are crucial for the arcade style graphics of this program. This program is split into two main files for organization and readability purposes, main.py and extra.py; the main file consists of all of pygames commands including the game clock and keyboard input detection loop, while extra.py handles most of the data and altering of said data.

Overview; When the program is run, the start() function is called, displaying a button surface, and entering a while loop to detect for the space key. Once pressed a button push animation is prompted, along with breaking from the loop, and calling to the main control() function.
The control function defines the initial speed, score, and blank 2 dimensional list representing the grid which contains the tetromino coordinates. Any of the 7 pieces are chosen by calling the random.randint() from 0-6. using this generated integer, the information for any piece is grabbed by calling to the peice_info() function which returns a list representing the starting coordinates of each block unit in a piece, the color title, and pieces status which is either 'N' for no action, or 'S' meaning the piece must be set. Once starting variables are initialized, the main game loop begins, which constantly checks for the following keyboard actions;

LEFT: Calls to move_peice() function passing the piece data, x movement instructions of -1, y movement instructions of 0, and the piece map defined previously as a 2d list.

RIGHT: Similar to when the left keystroke is detected except the x movement instruction is 1.

DOWN: Also same as previous key detections, exception being x instructions at 0, with y instructions at 1.

SPACE: begins loop of repeatedly calling move_peice function with downward instruction of y = 1, until a collision is detected which breaks from the loop.

UP: calls to rotate_peice() function which utilizes a rotation formula for each block unit in a piece, where the rotation point is the second coordinate in each tetromino’s list of coordinates.


For each of the above keystrokes, the coordinates before movement are held in a placeholder variable, then the coordinates are adjusted, passed to the check_collision() function, so that if a collision is detected the changed coordinates are discarded and the placeholder is returned. A piece is never set due to a horizontal collision, the status of the piece is only updated to 'S' if a vertical collision is found. If the current peice's status is set at 'S', a freeze variable is set at true, which ensures that no more key detection is used until the piece is finished setting, and all corresponding functions have completed their task. This variable was key to eliminating bugs such as unexpected piece behavior when keystrokes where pressed the instant the program was attempting to set a piece. Once freeze is true, the score is increased, and the set_peice() function is called, which stores the color of the tetromino’s blocks for each of their coordinates for later graphic display. Next, the clear_row() function is called, checks to see if the piece map grid has a full row, and if so brings all data from above rows down one row towards the cleared row. Then the player_dead() function is called that checks if the set pieces current coordinates are out of bounds of the piece map; if so, the control loop is exited, and similar to the start() function a dead_restart() function is called which displays a restart button animation if space is detected, and calls back to control function restarting the game. Finally new peice_data is retrieved, the speed of the game is updated based on the height of the score variable, and freeze is set to false allowing key detection to start again.

Outside of the key detection in this control() function an x variable counts each tick of the 60 ticks per second game clock. If x becomes equal to the speed variable, an automatic downwards move of the piece is called. Essentially speed becomes a lower and lower number as the score increases, meaning x reaches the same value of the speed varaible quicker as the game goes on resulting in the increased automatic downwards movement of the game making it harder and harder to stay alive. Each time x reaches the speed variable, representing a move occuring, the display_peice(), blit_grid(), display_background(), blit_score(), blit_onhold(), and pygame.display.update() are called sequentially, updating the graphics in the following; the current piece is displayed using its piece data and color, the grid lines are displayed over the piece, the background is then displayed which includes the title, the score is displayed over the background, the up next piece is displayed in a box over the background, and then all graphic updates to the game window are updated calling to pygame.




SUDOKU SOLVER

Important to note; This program consists of four important files, sudoku.py;the solving strategies, methods.py; the class method that utilizes getitem special method removing a huge amount of redundancy from the program, lastly data.txt and output.txt;containing the starting unsolved sudoku and the solved product data of the program.

Data is read from a file inputed from user into a 2d list, which is then used to create a board object to utilize the get_item method. The board object is able to easily return any row, column or box from the data to the main program, avoiding many repetitive loops. Overall the program relys on sectional functions, which each act as an individual stradegy in solving a given sudoku. The four current main stradegys implemented include; sole candidate, hidden single, naked pair, and hidden pair. Sole candidate and hidden candidate run repeatedly until they are unable to make any changes, next both pair stradegys are used, and this proccess continues until no change is made. With this combination the program is able to solve up to even extreme sudoku's on the sudoku.com website/app.

Future changes; In the future I would like to add more advance stradegies such as X-wing, and swordfish. I would also like to play around with a brute force algorithm which guesses and back traces when board validity is false, over and over untill solved.

For more information on the code specifics, veiw the sudoku folder under my projects to see my approach and comments.
