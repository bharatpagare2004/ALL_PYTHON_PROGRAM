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
