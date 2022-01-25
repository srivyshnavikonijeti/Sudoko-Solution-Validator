# Sudoko-Solution-Validator

Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9*9 grid with numbers so that each row, column and 3*3 section contain all of the digits between 1 and 9, As a logic puzzle. 

EXAMPLES :

1.   	INPUT :
sudoku =    [ [ 7, 9, 2, 1, 5, 4, 3, 8, 6 ],
                     [ 6, 4, 3, 8, 2, 7, 1, 5, 9 ],
                     [ 8, 5, 1, 3, 9, 6, 7, 2, 4 ],
                     [ 2, 6, 5, 9, 7, 3, 8, 4, 1 ],
                     [ 4, 8, 9, 5, 6, 1, 2, 7, 3 ],
                     [ 3, 1, 7, 4, 8, 2, 9, 6, 5 ],
                     [ 1, 3, 6, 7, 4, 8, 5, 9, 2 ],
                     [ 9, 7, 4, 2, 1, 5, 6, 3, 8 ],
                     [ 5, 2, 8, 6, 3, 9, 4, 1, 7 ] ]
EXPECTED OUTPUT :
Sudoku is valid.

2.    INPUT :
 sudoku =       [[5,3,4,6,7,8,9,1,2],
           	[6,7,2,1,9,5,3,4,8],
           	[1,9,8,3,4,2,5,6,7],
           	[8,5,9,7,6,1,4,2,3],
           	[4,2,6,8,5,3,7,9,1],
           	[7,1,3,9,2,4,8,5,6],
           	[9,6,1,5,3,7,2,8,4],
           	[2,8,7,4,1,9,6,3,5],
           	[3,4,5,2,8,6,1,7,8]]
                        
EXPECTED OUTPUT :
Sudoku is not valid.

