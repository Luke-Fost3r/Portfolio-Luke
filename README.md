# Portfolio-Luke
A collection of my current projects on my journey to become a computer scientist, feel free to explore, and see how I approached different problems
Tetris and sudoku are games ive played since childhood, so once my programming ability had grown some, I knew these games would be on my project list


TETRIS (lukes version)

Important to note;
this project utilizes pygame; most importantly for an easy built in game clock, and keyboard detection function.
many 'surfaces' are defined, and used for 'screen.blit(surface)' which take up many lines of simple variable definition and display statments, but are crucial for the arcade style graphics of this program. 
This program is split into two main files for orginization and readaility purposes, main.py and extra.py; the main file consists of all of pygames commands including the gameclock and keyboard input detection loop, while the extra function handles most of the data and altering of said data.

Overveiw;
When the program is run, the start function is called, displaying a button surface, and entering a while loop to detect for the space key. Once pressed a button push animation is prompted, along with breaking from the loop, and calling to the main control function.
The control function defines the initial speed, 





SUDOKU SOLVER

