"""# Python program to read a String and Print Longest
# word and it's Position
# Read input string
str = input("Enter a String: ")
# Split the string to a list of words
word_list = str.split()
# Find the longest word
longest_word = max(word_list, key = len)
# Find the position (index) of longest word
pos = str.index(longest_word)
# Print the longest word and it's position
print("Longest word: ",longest_word)
print("Position of Longest word: ", pos)"""

# for revision 
str = input("enter the string you want to insert : ")

word_list = str.split()
longest_word = max(word_list,key=len)
position_of_longest_word = str.index(longest_word)
print("longest word of string is =  ",longest_word)
print("the position of sting in the list is : ",position_of_longest_word)