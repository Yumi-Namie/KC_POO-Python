from functools import reduce


"""
This challenge is from the Bootcamp KeepCoding:

Basically is to receive one MATRIX (list of lists) and
calculate the average of each element in this matrix according with their neighbours.
And than, return the new matrix with all those averages.

>> Neighbours: numbers those share one edge.
We could say that there's three kinds of elements: corners, interiors and borders.
- corners have just two neighbours
- borders have three neighbours
- interior have four neighbours

>> Avarages: (own_value + neigbours_values) / ((itself) + neighbours)

"""

def process_matrix(matrix):
    """ Return list of list with avarage.
    >> index represented for columns  by 'i' and for lines (elements) by 'j'
    """
    try:
        processed_list = []
            
        for i, column in enumerate(matrix):
            column_elements = []
            for j, element in enumerate(column):
                column_elements.append(process_element(i, j,matrix))
            processed_list.append(column_elements)
        
        print_matrix(matrix,processed_list)

        return processed_list
    except TypeError:
        print("⚠️" + "  " + "Sorry. Something Wrong")
    

    
    

def process_element(i, j, matrix):
    """
    Get the index of an elements and the list it is in. 
    Computes its average with its neighbors ans returns that everage
    """
    # get the list of neighbors 
    # i, j = get_neighbour_indices(i,columns, j, elements)
    index = get_neighbour_index(i,j,matrix)
    values = get_neighbour_values(index,matrix)

    # calculate your average
    average = get_average(values)
 
    # returns the final average
    return round(average,2)



def get_neighbour_index(i,j,matrix):
    """ 
    Getting all the neighbourhood (own index, upper index, down index, right index, left index.
    Even the imposible neighbours and than, using condicional to get just the posibles neighbours called selected_index
    """
    all_index = []
    n_columns = len(matrix)
    n_row = len(matrix[0])

    all_index.append((i-1,j)) #left-side
    all_index.append((i+1,j)) #right-side
    all_index.append((i,j+1)) #up
    all_index.append((i,j-1)) #down
    all_index.append((i,j)) #own-side

    selected_index = []
    for i,j in all_index:
        if i >= 0 and i<= (n_columns-1) and j >= 0 and j<= (n_row-1):
            selected_index.append((i,j))
    return selected_index

    

def get_neighbour_values(index, matrix):
    """ 
    Getting all the value of the existed neighbours + own value
    """
    values = []
    for i,j in index:
        values.append(matrix[i][j])
    return values
     


def get_average(numbers):
    """"
    Recives a list of numbers and returns their average
    """
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)




""" To transpose the matrix:  """

def nth_elements(matrix,index):
    """
    Recives one matrix and change the position of the elements accordin to the currently position
    """
    result =[]
    for i in matrix:
        result.append(i[index])
    return result



def transpose(matrix):
    """
    Recives one matrix and return a new one transposed
    """
    matrix_transposed = []
    try:
        for i in range(len(matrix[0])):
            matrix_transposed.append(nth_elements(matrix,i))
        return matrix_transposed
    except:
        print(f"Sorry, something wrong\n")



def add_pipe(line):
    """
    Adding bars to the matrix representation
    """
    for element in line:
        print('{:>5}'.format(element) + "   " + '|', end = "  " )
    return ""
    
    
    
def transpose_repr(matrix):
    """
    receives a matrix, transpose it and returns its representation
    """
    try:
        transp = transpose(matrix)
        for line in transp:
            print (add_pipe(line))
        return ""
    except:
        print("Oops, it's not possible to print the matrix\n")

        

def print_matrix(mtx,averages):
    print(f"\nMatrix: {mtx}\n")
    transpose_repr(mtx)
    print(f'\nAvarages: {averages}\n')
    transpose_repr(averages)






if __name__ == "__main__":

    # >> each list = one column
    mtx = [[2,4,5,2],[4,6,2,3],[1,2,3,4],[5,6,7,8]]
    # mtx = [[1,3,4,5],[5,6,7,0],[8,9,10,2]]
    # mtx = [[1,3,4],[5,6,7],[8,9,10],[2,3,4]]
    # mtx = [[1,2,1,2,3,2]]
    # mtx = [[]]
    # mtx = []
    # mtx = [['a','b','c']]

    
    
    process_matrix(mtx)
    