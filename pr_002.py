def find_longest_word(input_string):
    words = input_string.split()
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

def char_frequency(input_string, char):
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count

def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    return input_string == input_string[::-1]

def find_substring(input_string, substring):
    index = input_string.find(substring)
    return index

# Input string
input_string = input("Enter a string: ")

# a) To display word with the longest length
longest_word = find_longest_word(input_string)
print("Word with the longest length:", longest_word)

# b) To determine the frequency of occurrence of a particular character in the string
char_to_count = input("Enter a character to count: ")
frequency = char_frequency(input_string, char_to_count)
print(f"Frequency of '{char_to_count}' in the string: {frequency}")

# c) To check whether the given string is a palindrome or not
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# d) To display the index of the first appearance of the substring
substring_to_find = input("Enter a substring to find: ")
index = find_substring(input_string, substring_to_find)
if index != -1:
    print(f"The substring '{substring_to_find}' first appears at index {index}.")
else:
    print("The substring is not found in the string.")