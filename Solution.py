# Mohit Gupta

# Giving the user an option to enter the dimensions of the block

import numpy as np


m = int(input(print("Enter the number of rows:")))

n = int(input(print("Enter the number of columns:")))






def puzzle_structure_generator(m, n):
    """

    :param m: The desired rows input by the user
    :param n: The desired columns input by the user
    :return:  The final base structure of the puzzle
    """


    # Using list comprehension to generate the initial puzzle in the form of nested lists

    # Here "W" = West
    # Here "N" = North
    # Here "S" = South
    # Here "E" = East

    a = [["W", "N", "S", "E"] for i in range(m)]
    puzzle_structure = [a for i in range(n)]


    puzzle_structure = np.array(puzzle_structure)

    # As shown diagrammatically in the document submitted with this assignment,
    # a person cannot take a turn towards a wall.
    # Thus, for the turns adjacent to the below walls, I've to make the below elements zero.
    # For turns adjacent to:
    # West Wall, "W" == 0
    # North Wall, "N" == 0
    # South Wall, "S" == 0
    # East Wall, "E" == 0


    for i in range(n):

        # For North Wall, "N" = 0
        puzzle_structure[0][i][1] = 0

        # For South Wall, "S" = 0
        puzzle_structure[m-1][i][2] = 0


    for i in range(m):



        # For West Wall, "W" = 0
        puzzle_structure[i][0][0] = 0

        # For East Wall, "E" = 0
        puzzle_structure[i][n-1][3] = 0



    return puzzle_structure




puzzle_structure = puzzle_structure_generator(m,n)





for i in puzzle_structure:
    # I am using map function because if I'll use the " ".join(i) code directly, it'll give an error about that
    # it was supposed to get string but it got a list. Thus mapping the list element with the str data type.
    # This loop is to systematically display the initial iteration before randomizing the possible turns
    # from each turn.

    print("      ".join(map(str, i)))















