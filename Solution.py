# Mohit Gupta

# Giving the user an option to enter the dimensions of the block

import numpy as np
import random


m = int(input(print("Enter the number of rows:")))

n = int(input(print("Enter the number of columns:")))


def organized_view(puzzle_structure):
    """
    This function will accept the numpy array and display it's contents in an organized way.
    :param puzzle_generator:
    :return:
    """

    for i in puzzle_structure:
        # I am using map function because if I'll use the " ".join(i) code directly, it'll give an error about that
        # it was supposed to get string but it got a list. Thus mapping the list element with the str data type.
        # This loop is to systematically display the initial iteration before randomizing the possible turns
        # from each turn.

        print("      ".join(map(str, i)))


    print("----------------------------------------------------------------\n\n")





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





def random_entry_point(puzzle_structure):
    """
    I will first extract the "first element" from the "first list element" from all the rows of first column.

    Similar procedure would be followed for the "last element" from the "last list element" from all the rows of the
    last column.

    Once I extract all the elements, I will randomly make one of the elements as " 1 " to signify it as the entry point
    or exit point.

    I will save the entry coordinate of the player.

    I also will code that you cannot exit from the entry point.

    :param puzzle_structure: Giving the resultant data structure from puzzle_structure_generator(m,n)
    :return: Returns two objects. One is the actual numpy array with the entry and exit points and
    two, the list which contains the solution coordinates.
    """


    entry_point = puzzle_structure[:, 0, 0]

    # I visited https://www.geeksforgeeks.org/python-select-random-value-from-a-list/ to find better method to randomly select an index.

    random_entry_index = random.randrange(len(entry_point))
    entry_point[random_entry_index] = 1


    exit_point = puzzle_structure[:, n-1, 3]
    random_exit_index = random.randrange(len(exit_point))
    exit_point[random_exit_index] = 1



    # Now I will replace the entry and exit points in the actual numpy array
    puzzle_structure[:, 0, 0] = entry_point
    puzzle_structure[:, n-1, 3] = exit_point


    # I will also save the entry and exit points in a list that will act as a recorder for correct list solutions match.
    # Also, I will not randomly change the direction restrictions of the solution coordinates as they should be fixed.


    solution_coordinate_sequence = [[random_entry_index, 0], [random_exit_index, n-1]]


    return puzzle_structure, list(solution_coordinate_sequence)




def solution_generator(solution_coordinate_sequence):


    coordinates = []

    entry_coordinate = solution_coordinate_sequence[0]
    exit_coordinate =  solution_coordinate_sequence[-1]


    for i in range(n):

        coordinates.append([entry_coordinate[0], i])



    if entry_coordinate[0] > exit_coordinate[0]:

        for i in reversed(range(exit_coordinate[0], entry_coordinate[0])):


            coordinates.append([ i ,n-1])

    if entry_coordinate[0] < exit_coordinate[0]:

        for i in range(entry_coordinate[0] + 1, exit_coordinate[0] + 1):

            coordinates.append([i, n-1])



    return coordinates




def random_direction_generator(puzzle_structure, solution_coordinate_sequence):


    p_structure = puzzle_structure
    solutions = solution_coordinate_sequence
    all_coordinates = []
    required_coordinates = []



    # Generating the possible coordinates for the m * n puzzle

    for i in range(m):

        for j in range(n):

            all_coordinates.append([i,j])



    # Removing the coordinates that are in the solutions so that I would not mistakenly block the solution direction.

    for i in all_coordinates:

        if i not in solutions:
            required_coordinates.append(i)


    for i in required_coordinates:


        for j in range(4):


            # Now I am randomly generating one possible number, either '1' or '0'.
            # I learnt the below one line of code from the below link:
            # https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
            # I the number that I generated is '0' then I will replace the individual element in the direction list to '0'.


            a = np.random.randint(2, size=1)

            if a == 0:
                p_structure[i[0], i[1], j] = 0


    return p_structure



def game_board(m,n,puzzle_structure, entry_coordinate, exit_coordinate):


    # Making a board that only contains zero
    # When I used the below code, I was facing error while replacing the player's position with the an array.
    # I faced an error here earlier here which is described in the comment 39 in the below link:
    # https://stackoverflow.com/questions/4674473/valueerror-setting-an-array-element-with-a-sequence
    # Thus I decided not to use numpy array in this case and generate a normal array


    # zero_board = np.full((m,n), ["0"])

    zero_board = []

    for i in range(m):

        # I am adding eight spaces around both the sides of zero so that it would look presentable while printing the table.
        zero_board.append(["        0        "] * n)

    prev_x_coo = entry_coordinate[0]
    prev_y_coo = entry_coordinate[1]

    curr_x_coo = entry_coordinate[0]
    curr_y_coo = entry_coordinate[1]



    zero_board[curr_x_coo][curr_y_coo] = puzzle_structure[curr_x_coo, curr_y_coo]

    print("\n\nYou can only move in the below shown directions and do not choose one or zero.\n")
    organized_view(zero_board)

    flag = True

    while True:
        try:
            while flag:

                move_by_player = input("\n\n Enter the letter for your move except one and zero or enter 'stop' :")
                move_by_player = move_by_player.lower()

                if move_by_player in ['w', 'n', 's', 'e']:

                    if move_by_player == 'w':

                        curr_y_coo = curr_y_coo -1

                    elif move_by_player == 'n':

                        curr_x_coo = curr_x_coo - 1

                    elif move_by_player == 's':

                        curr_x_coo = curr_x_coo + 1

                    elif move_by_player == 'e':

                        curr_y_coo = curr_y_coo + 1

                elif move_by_player == 'stop':

                    flag = False

                else:
                    print("Please enter the directions only from ['w', 'n', 's', 'e']")

                zero_board[prev_x_coo][prev_y_coo] = "        0        "
                zero_board[curr_x_coo][curr_y_coo] = puzzle_structure[curr_x_coo, curr_y_coo]


                prev_x_coo = curr_x_coo
                prev_y_coo = curr_x_coo

                organized_view(zero_board)

        except IndexError:

            curr_y_coo = prev_y_coo
            curr_x_coo = prev_x_coo
            zero_board[curr_x_coo][curr_y_coo] = "X"
            organized_view(zero_board)








# Step 1 : Generating the base structure of the puzzle

puzzle_structure1 = puzzle_structure_generator(m,n)

# In case if you search for the shape of the above generated puzzle when m * n = 3 * 3,
# the shape would be ( 3, 3, 4 ) as I have designed it to be a multidimensional array.
# Displaying the puzzle in an organized view:
organized_view(puzzle_structure1)



# Step 2:
# Generating random entry and exit points:

puzzle_structure2, solution_coordinate_sequence1 = random_entry_point(puzzle_structure1)
organized_view(puzzle_structure2)




# Step 3:
# Generating the correct coordinate sequence of puzzle solution after randomly generating the
# entry and exit points:


solution_coordinate_sequence2 = solution_generator(solution_coordinate_sequence1)

# print("Below are the solution coordinates in sequence. \nIf any other sequence would be provided, you'll not reach the end point:")
# print(solution_coordinate_sequence)
# print("\n\n\n")




# Step 4:

# Now I will change the existing directions and generate random directions.
puzzle_structure3 = random_direction_generator(puzzle_structure2, solution_coordinate_sequence2)
organized_view(puzzle_structure3)




# Step 5:

entry_coordinate = solution_coordinate_sequence2[0]
exit_coordinate =  solution_coordinate_sequence2[-1]


game_board(m,n, puzzle_structure3, entry_coordinate, exit_coordinate)














