# Sudoko-Solution-Validator

Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9*9 grid with numbers so that each row, column and 3*3 section contain all of the digits between 1 and 9, As a logic puzzle. 

**METHODOLOGY**
Follow the steps below to solve the problem:
1.  Traverse the given matrix sudoku[][].
2.  Check if the 3 conditions are satisfied or  not.
3.  If any of the conditions are not satisfied, then print “Not valid“.
4.  Otherwise, print “Valid“.
**
IMPLEMENTATION **
1. To determine if all of the entries in the list (sudoku row or sudoku column) are unique,  we use the built-in set() function.
2. The set() function, in essence, eliminates any duplicate   entries from the list. There are no duplicate elements if the set is 9 elements long.
3. To obtain the column elements, we'll use the list comprehension approach.
   [item[col num] for sudoku item]
4. To retrieve the items for each cell, a slicing process from the Python list is employed.


This project is done by :

[Konijeti Sri Vyshnavi](https://github.com/srivyshnavikonijeti)<br/>
[Methuku Samhitha](https://github.com/METHUKUSAMHITHA)<br/>
[Lokavarapu Varsha](https://github.com/varsha743)<br/>
[Mucharla Deeksha]()
