#Write a function that takes as input a square matrix M 
#(represented as list of lists) and returns a list L containing two lists: 
#● M[0] is the list of the maxima of the rows of M 
#● M[1] is the list of the maxima of the columns of M 


def matrix(mat):

    #prints the matrix
    print('This is your Matrix\n')
    print(print_out_matrix(mat)) 
    print('\n')
    #print the max row values and the max column values, calling the respective functions which have been split in two for simplicity
    print('Max Row Values : ',find_max_row(mat))
    print('Max Column Values : ',find_max_col(mat))
    return [find_max_row(mat),find_max_col(mat)]
    
    
#prints the matrix horizontally, as if a normal list of numbers
def print_out_matrix(mat):
    for index in mat:
        print(index)
    print('\n in 1D\n')
    return mat


def find_max_row(matrix):
    
    row_length = len(matrix)
    max_row = 0 
    max_row_list = []
    #iterates row length times
    for j in range(row_length):
        #attributes max row value to the first value in the first row/column in order to benchmark it with the other values
        max_row = matrix[j][0]
        #iterate over the indexes of the matrix / row elements
        for i in matrix[j]:
            #if the max row value is bigger than the 'benchamrked value'it takes that value as the temporatru max value 
            if max_row < i:
                max_row = i
        #appends the max row value to a anew list which will be returned
        max_row_list.append(max_row)
    #returns the max row
    return max_row_list


def find_max_col(matrix):
    #initialize list for max column
    max_column_list = []
    i = 0 
    #using while loop makes it more streamlined for the columns, while the counter is less than the length of the matrix row 0 loop keeps going
    while i < len(matrix[0]):
        max_column = matrix[0][i]
        j = 1
        while j < len(matrix):
            if matrix[j][i] > max_column:
                max_column = matrix[j][i]
            j += 1
        #append the max column to the list
        max_column_list.append(max_column)
        i += 1
    return max_column_list
       
print(matrix(([7,9,1],[6,8,9],[3,2,9])))
print(matrix([[1,2,4],[3,1,4],[6,7,2]]))
print(matrix(([4,9,8],[3,2,7],[0,5,1])))
print(matrix([[1,8,3],[2,1,5],[0,9,2]]))
