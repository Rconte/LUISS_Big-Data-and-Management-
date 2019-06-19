#Write a script that:
#● Asks the user to insert a string s and two integers x and y such that both x and y 
#are less than len(s). The user must be instructed about the maximum admitted value for x and y.
#● Prints: ● the substring s1 of s going from the beginning of s to the index x included; 
#● the substring s2 of s going from the index -y included till the end of s; 
#● the string obtained by concatenating s1 repeated y times and s2 repeated x times


print('You will be asked to insert a string and two integers..')
#asks the user to insert a string 
s = str(input('Insert a STRING'))

#asks the user for two integer values, and instructs that they need to be less than the string's length
x = int(input('Insert your first INTEGER (Must be LESS than the length of inserted string)'))
y = int(input('Insert your second INTEGER (Must be LESS than the length of inserted string)'))

#substring s1, goes from s to x included (x+1)
s_1 = s[0:x+1]
print(s_1)

#substring s2, goes from -y to the end of s
s_2 = s[-y::]
print(s_2)

#substring concatenated s1 repeated y times and s2 repeated x times
s_concat = (s_1 * y) + (s_2 * x)
print(s_concat)


