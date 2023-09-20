#Function to display the Menu of Operations: 
 
def showMenu():     
    
    
    
    print( 
""" 
*****************    Operation Menu:    *********************
           
[1]	To display word with the longest length.  
[2]	To determines the frequency of occurrence of particular character in the string.  
[3]	To check given string is palindrome or not.  
[4]	To display index of first substring.  
[5]	To count the occurrences of each word in string.
[6]     Exit.  
 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""" 
) 
 
# Function to display the longest word and it's length
def longest(main_string,split_string):    
    long = max(split_string,key=len) 
 
    print("The Longest Word is: ",long," and it's Length is: ",len(long)) 
 
# Function to display the frequency of character taken from user 
def freqChar(main_string):     
   
     chr = input("Enter character: ") 
     count = 0 
     for ch in main_string:         
        if chr == ch:             
           count+=1 
        
           print("The frequency of the character in the Main String is: ",count) 
 
# Function to display whether the string is Palindrome or not  
def isPalindrome(main_string):  
    if(main_string[::-1] == main_string): 
        print("The given string is a Palindrome!") 
    else:         
        print("The given string is not a Palindrome!") 
 
# Function to display the index at first occurrence of a sub-string 
def indexChar(main_string):     
    subStr = input("Enter Substring: ") 
    fnd = main_string.find(subStr) 
 
    if(fnd == -1): 
        print("The sub-string is not found!")   
    else:         
        print("The index of the sub-string is: ",fnd) 
 
# Function to display the Frequency of the words in the Main String
def freqWord(main_string):  
    splitStr = main_string.split() 
 
    lst = [] 
 
    for i in splitStr:         
        if i not in lst:             
            lst.append(i) 
 
    for i in range(0,len(lst)): 
        print("The Frequency of the word:",lst[i]," is ",splitStr.count(lst[i])) 
 
#Main Program as Follows : 
loop_status = True  
main_string = input("Enter the main String: ") 
split_string = main_string.split() 
 
showMenu() 
 
while(loop_status):     
    ch = int(input("Enter your choice for operation: ")) 
 
    if ch == 1:        
        longest(main_string,split_string) 
 
    elif ch == 2: 
        freqChar(main_string) 
 
    elif ch == 3: 
        isPalindrome(main_string) 
 
    elif ch == 4:         
        indexChar(main_string) 
 
    elif ch == 5: 
      freqWord(main_string) 
 
    elif ch == 6: 
       loop_status = False 
    else: 
        print("Wrong Input Given!!!") 
