# Portfolio-Luke
//
Disciplined and driven Computer Science student with a love for writing code and a fascination for machine/deep learning and algorithm design. Eager to understand and approach the complex computational problems of the future and contribute to cutting-edge research. searching for opportunities to expand my knowledge and skills, and eventually pursue a PhD in the field of computer science.
//

Some of my major inspirations include Alan Turing, Ada Lovelace, science fiction (hyperion), and ai philosophy. 
                                                                                                                                              |       | 
A collection of my current projects on my journey as a computer scientist, feel free to explore, and see how I approached different problems  | BELOW |
                                                                                                                                              V       V
  

TETRIS (Luke's version)

Important to note; this project utilizes pygame; most importantly for an easy built in game clock, and keyboard detection function. Many 'surfaces' are defined and displayed which take up many lines of variable definition/display statements, but are crucial for the arcade style graphics of this program. This program is split into two main files for organization and readability purposes, main.py and extra.py; the main file consists of all of pygames commands including the game clock and keyboard input detection loop, while extra.py handles most of the data and altering of said data.

When the program is run, there is a menu screen which prompts for user input to start the game, and play the animation. The same thing happens when the user dies, the user is prompted to restart, or click to exit. All data is initialized, including speed, score, and the 2d list/grid representing the location of tetrinomoes on the screen. Peices are chosen psuedo-randomly, each peice having a predeclared array of its individual blocks, that make up its four block body, and its unique color. The peice also has a status, representing wether in play or set. Starting from when the first peice appears on screen, the user can input five movements at any time. These movements include, up, down, right, left, and space. Down, right, and left work as expected moving the peice one grid unit in the corresponding direction. Up however rotates the peice, and space applies a repetitive motion downwards on the peice until set.

After each move, collisions are checked for, and if occured, peice status updated accordingly. When a peice occurs a vertical collision, it is flagged, and no further input will be accepted in the control loop until all proccessing is complete and the flag is removed. After this is done, each row is checked if full, and if so the row is cleared and all above rows move down one. The score is adjusted accordingly, and mutliplied based on the current speed of the game, which increases as the score increases. This continues until a peice is set out of bounds, meaning the user has died. The user is than prompted to exit or restart.

Future changes; Improvements I would like to add to this program, mainly include the graphical interface, and animation. I think that adding an animation when a row is cleared, and the classic arcade music would be a great step for a more authentic feel. In addition I will likely add a slight pause before the peice is set, giving the user an extra quater second to recact, and hopefully make the peices feel more physical rather than weightless images.



SUDOKU SOLVER

Important to note; This program consists of four important files, sudoku.py;the solving strategies, methods.py; the class method that utilizes getitem special method removing a huge amount of redundancy from the program, lastly data.txt and output.txt;containing the starting unsolved sudoku and the solved product data of the program.

Data is read from a file inputed from user into a 2d list, which is then used to create a board object to utilize the get_item method. The board object is able to easily return any row, column or box from the data to the main program, avoiding many repetitive loops. Overall the program relys on sectional functions, which each act as an individual stradegy in solving a given sudoku. The four current main stradegys implemented include; sole candidate, hidden single, naked pair, and hidden pair. Sole candidate and hidden candidate run repeatedly until they are unable to make any changes, next both pair stradegys are used, and this proccess continues until no change is made. With this combination the program is able to solve up to even extreme sudoku's on the sudoku.com website/app.

Future changes; In the future I would like to add more advance stradegies such as X-wing, and swordfish. I am also playing around with the idea of a brute force algorithm which guesses and back traces when board validity is false, over and over untill solved.

                                                                                                                                                         
For more information on the code specifics, veiw the SUDOKU or TETRIS folder under my projects to see my approach and comments.                         
thanks for reading                                                                                                                                       
