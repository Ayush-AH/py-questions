# 1) reverse ths string
# str = "hello ayush how are you?"
# reverse = ""

# for i in range(len(str)-1,-1,-1):
#     reverse += str[i]

# print(reverse)	

#2) arrange string such that lower case comes first 
# str = "Hello Ayush hoW aRe You?"
# output = ""

# for i in str:
#     if i.islower():
#         output += i
    
# for i in str:
#     if i.isupper():
#         output += i
        	
# print(output)

#3)  count char , digits and symbols
# str = "phdk45#@6!ji55f"
# chars = 0
# digits = 0
# symbols = 0

# for i in str:
#     if i.isalpha():
#         chars += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         symbols += 1        
        
# print(f"Total counts of chars, digits and symbols: \nchars:{chars}\ndigits:{digits}\nsymbols:{symbols}")        

#4 count vowels fromgiven string
# str = "aihseoujbkwfisoiou"
# vowels = 0


# for i in str:
#     if i in "aeiouAEIOU":
#         vowels += 1
        

# print(vowels)

#5) check in the string is pallindromic


def checkPallindromic(str):
    reverse = ""
    for i in range(len(str)-1,-1,-1):
         reverse += str[i]
    

    if str == reverse:
         print(f"giver string : {str} is pallindromic")
    else:
         print(f"giver string : {str} is not pallindromic")
        

checkPallindromic("naman")
