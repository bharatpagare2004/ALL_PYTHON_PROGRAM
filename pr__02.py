# this is second practical of "fds"
# (1) To display word with longest length . 
str = input("enter your string : ")
def long_len():
    str_list = []
    long_len  =[]
    str_list = str.split(" ")
    for i in str_list:
        long_len.append(len(i))
    long_len .sort (reverse =True)
    print("word is = ",long_len[0])
    print( " this is len :", max((long_len))) 

# To determine the frequency of occurence of particular character in the string.
def freq_char():
    c = input("enter character for finding its frequency in string  : ")
    print("c= ",c)
    g = str.count(c)
    print(g)

# To cheak given string is palindrome of not . 
def str_pali():
    m= str[::-1]
    print(m)
    if m==str:
        print("string is palindrome.")
    else:
        print("string is not palindrome.") 
  
# To display index of first occurences of the substring
def index_substring():
    print("enter the character:")
    str_substring=input()
    list_str = str.split()
    for i in range(len(list_str)):
        if str_substring == list_str[i]:
            print(str)
            print(i)
            break
# to frequency of each word        
def freq_word():
    list_str = str.split(" ")
    print("count of each word")
    for i in range(len(list_str)):
        print(list_str[i],"=",list_str.count(list_str[i])) 

if __name__ =="main":
    print("$$$$$$$$$ this is menu $$$$$$$$$")

while(True):
      print("`1. this is for word with longest length ")

      print(" 2. to display the character of occurences of particular character in the string")

      print(" 3.to cheak whether the given string is palindrome of not")

      print(" 4.to display index of first appereance of the substring ")

      print(" 5.to count the occurence of each word in given string ")

      print(" 6.exit")
      ch = int(input("enter your choice:"))

      if( ch ==1):
        long_len()
      elif(ch==2):
         freq_char()
      elif(ch ==3):
         str_pali()
      elif(ch == 4):
         index_substring()
      elif(ch ==5):
         freq_word()
      else:
          print("exit")                          


