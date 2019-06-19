
#Write a program that:
#● lets the user insert a filename;
#● try to read from that file, catching possible exceptions;
#● constructs a dictionary whose keys are letters of the alphabet and such that the value associated to letter L is the number of occurrences of L in the specified file.
#● prints the dictionary to a file "output.txt" in the following format:
#L1: V1 L2: V2 L3: V3 ...
#● where V1 is the number of occurrences of L1, V2 the number of occurrences of L2,

#prints out the dictionary in a tidier way by dividing up key and values with a ':' stirng in the middle
def tidy_print(out_dict):
    for key,values in out_dict.items():
        print(key, ' : ', values)
    return ''

#tidy output, same as tidy_prtint but outputs to file
def tidy_out(filename, out_dict):
    file_output = open(filename,'w')
    for key,values in out_dict.items():
        
        file_output.write(key)
        file_output.write(' : ')
        file_output.write(str(values))
        file_output.write('\n')

    file_output.close()
    return 'File saved as output.txt'

#creates an empty dictionary with  alphabet keys and empty (string) values. Its not the only way but its a good way to split the task at hand
def create_alpha_dict():
    alpha_keys = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        for j in alphabet:
            alpha_keys[alphabet[i]] = ''

    
    return alpha_keys


def file_handling_ex(filename = 'input.txt'):
    #asks for the filename, no extension needed, the program will concatenate it automatically. This makes it easier for an inexperienced user {we could easily change the file extension in the program or place an if/else statement for different types of files}
    filename = str(input('Please insert filename  \nFile extension will be added automatically  '.upper()))
    filename = filename + '.txt'
    created_dict = create_alpha_dict()
    output_dict = dict()
    counter = 0 
    
    
    #tries if the file is good-to-go or there are errors
    try:
        file_input = open(filename,'r')
        file_in = file_input.read()
       
    except:

        print('There was an error with your file, please try again')

    
    #opens the output file
    output_file = open('output.txt','w')
    print('Working..')
    #iterates all the letters in the alphabet {A-Z}
    for iteration in range(len(created_dict)):
        #shows the program is working, a sanity check for me mostly
        print('..iteration',iteration+1, 'out of ',len(created_dict))
        print('..')
        #iterates over the keys of the dict
        for key in created_dict.keys():
            counter = 0 
            for letter in file_in:
                if key == letter:
                    #counts the number of occurances for the letter in question
                    counter += 1
            output_dict[key.upper()] = counter
        print('DONE.')            
    print(tidy_print(output_dict))            
    print(tidy_out('output.txt',output_dict))
    #close input and output files, we are done with them
    file_input.close()
    output_file.close()
    #returns the dictionary
    return output_dict

def main():
    
    file_handling_ex()



if __name__ == '__main__':

    main()


