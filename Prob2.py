##################################################
# Name: Jonah Luhrsen
# Collaborators: None
# Estimate of time spent (hr): 1
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    number_of_lists = len(array)
    for i in range(number_of_lists):
        if len(array[i]) != number_of_lists:
            return False
     
    first_row_total = 0
    for i in array[0]:
        first_row_total = first_row_total + i
    
    for i in range(number_of_lists):
        row_total = 0
        for i in array[i]:
            row_total = row_total + i 
        if first_row_total != row_total:
            return False
        
    first_column_total = 0
    for i in range(number_of_lists):
        first_column_total = first_column_total + array[i][0]

    number_of_columns = len(array)
    for i in range(number_of_columns):
        column_total = 0
        for j in range(number_of_lists):
            column_total = column_total + array[j][i]
        if first_column_total != column_total:
            return False
     
    top_to_bottom_diagnol = 0
    bottom_to_top_diagnol = 0
    for i in range(number_of_lists):
        top_to_bottom_diagnol = top_to_bottom_diagnol + array[i][i]
    for i in range(number_of_lists):
        index = len(array[i]) - i - 1
        bottom_to_top_diagnol = bottom_to_top_diagnol + array[i][index]
    if top_to_bottom_diagnol != bottom_to_top_diagnol:
        return False

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))


