# Portfolio-Luke


My name is Luke Foster, and this is my current portfolio. I am always looking for new challenges and ideas for programs, below are simply the ones I have refined the farthest so far. I plan to add multiple more projects soon, likely including a cypher program to send extremely coded messages, a chess robot, and some neural network image identifiers.
I am Enthusiastic and facinated with writing code, and the theory behind it, currently and especially in deep learning. I hope that through this portfolio I will expand my experience, and create more and more interesting projects.

Some of my major inspirations include Alan Turing, Ada Lovelace, science fiction books (Hyperion & The Invincible), and ai philosophy. 

                                                                                                                                             

Feel free to explore, and see how I approached different problems  (BELOW) 
                                                                                                                                             




TETRIS (Luke's version)

Important to note; this project utilizes pygame; most importantly for an easy built in game clock, and keyboard detection function. Many 'surfaces' are defined and displayed which take up many lines of variable definition/display statements, but are crucial for the arcade style graphics of this program. This program is split into two main files for organization and readability purposes, main.py and extra.py; the main file consists of all of pygames commands including the game clock and keyboard input detection loop, while extra.py handles most of the data and altering of said data.

When the program is run, there is a menu screen which prompts for user input to start the game, and play the animation. The same thing happens when the user dies, the user is prompted to restart, or click to exit. All data is initialized, including speed, score, and the 2d list/grid representing the location of tetrominoes on the screen. Pieces are chosen pseudo-randomly, each piece having a predeclard array of its data including, its four block body's coordinates, its unique color, and its status. The piece's status represents whether in play or set. Starting from when the first piece appears on screen, the user can input five movements at any time. These movements include, up, down, right, left, and space. Down, right, and left work as expected moving the piece one grid unit in the corresponding direction. Up however rotates the piece, and space applies a repetitive motion downwards on the piece until set.

After each move, collisions are checked for, and if occurred, piece status updated accordingly. When a piece occurs in a vertical collision, it is flagged, and no further input will be accepted in the control loop until all processing is complete and the flag is removed. After this is done, each row is checked if full, and if so the row is cleared and all above rows move down one. The score is adjusted accordingly, and multiplied based on the current speed of the game, which increases as the score increases. The speed, is the rate at which an automatic downwards move is applied to the piece, beyond the users control. This continues until a piece is set out of bounds, meaning the user has died. The user is then prompted to exit or restart.

Future changes; Improvements I would like to add to this program, mainly include the graphical interface, and animation. I think that adding an animation when a row is cleared, and the 
classic arcade music would be a great step for a more authentic feel. In addition I will likely add a slight pause before the piece is set, giving the user an extra quarter second to react, and hopefully make the pieces feel more physical rather than weightless images.



SUDOKU SOLVER

Important to note; This program consists of four important files, sudoku.py;the solving strategies, methods.py; the class method that utilizes getitem special method, and lastly data.txt and output.txt;containing the starting unsolved sudoku and the solved product data of the program.

Data is read from a file inputted from the user into a 2d list, which is then used to create a board object to utilize the get_item method. The board object is able to easily return any row, column or box from the data to the main program, avoiding many repetitive loops. Overall the program relies on sectional functions, which each act as an individual strategy in solving a given sudoku. The four current main strategies implemented include; sole candidate, hidden single, naked pair, and hidden pair. Sole candidate and hidden candidate run repeatedly until they are unable to make any changes, next both pair strategies are used, and this process continues until no change is made. With this combination the program is able to solve up to even extreme sudoku's on the sudoku.com website/app.

Future changes; In the future I would like to add more advanced strategies such as X-wing, and swordfish. I am also playing around with the idea of a brute force algorithm which guesses and back traces when board validity is false, over and over until solved.

For more information on the code specifics, view the SUDOKU or TETRIS folder under my projects to see my approach and comments.
thanks for reading!
