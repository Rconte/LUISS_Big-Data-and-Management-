def sort_it(my_string):
    #replace the string with the same string with no spaces, an excercise we completed during the same lesson as the assignment gives us a 
    #perfectly good function to work with this excercise
    my_string = remove_spaces(my_string)
    
    #if the length of the string is less than or equal to one, return the string 
    if len(my_string) <= 1:
        
        return my_string 
    #if element at position 0 is larger(lower) than the element at position 1
    #cut the elements of the string in order to iterate over it until we just have one element left
    elif my_string[0] > my_string[1]:
            
        my_string = my_string[1:]
        my_string = sort_it(my_string) 
        return my_string
    
    #if the length of the string is longer than 2 forms a string with the first element + the string from position 2 onwards and reruns the function
    elif len(my_string) > 2 :
        my_string = my_string[0] + my_string[2:]
        my_string = sort_it(my_string)
        return my_string
        
    else:
        my_string = my_string[0]
        return my_string

#removes spaces from the string
def remove_spaces(my_string):
    
    space = ' '
    if len(my_string) == 0:
        return ''
    if my_string[0] in space:
        
        return remove_spaces(my_string[1:])
    else:
        return my_string[0] + remove_spaces(my_string[1:])


print(sort_it('hello'))
print(sort_it('hey there'))
print(sort_it('banana'))
print(sort_it('zanzibar'))
