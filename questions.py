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


# def checkPallindromic(str):
#     reverse = ""
#     for i in range(len(str)-1,-1,-1):
#          reverse += str[i]
    

#     if str == reverse:
#          print(f"giver string : {str} is pallindromic")
#     else:
#          print(f"giver string : {str} is not pallindromic")
        

# checkPallindromic("naman")


#----- array -------
#1)accept the list elemt and print 
# num = int(input("Please enter your element count"))
# l = []

# for i in range(0, num,+1):
#     elem = int(input(f"please enter elmeent no {i+1}"))
#     l.append(elem)
    
# print(l)   

#2) reverse the list 
# l = [5,6,9,3,0,4,6]
# reverse = []

# for i in range(len(l)-1,-1,-1):
#     reverse.append(l[i])

# print(reverse)

#3) print positive and negative element of list seprately
# l = [-2,6,9,-8,7,-9,-8,7,2,-8,9]
# p = []
# n = []

# for i in range(len(l)):
#     if l[i] >= 0:
#         p.append(l[i])
#     else:
#         n.append(l[i])      

# print(p,n)        

#4) print gretest elemet of list with it's index
# l = [2,96,69,77,145,20]
# max = 0
# index = 0

# for i in range(len(l)):
#     if l[i] > max:
#         max = l[i]
#         index = i
#     else:
#         continue


# print(f"max number is {max} on index {index}")

#5) second gretest value of list with index
# l = [2,96,69,77,145,20]
# max1 = 0
# max2 = 0

# for i in range(len(l)):
#     if l[i] > max1:
#         max2 = max1
#         max1 = l[i]

# print(max1, max2)

#6) check if list is sorted or not 

# l = [1,2,3,4,5,6]

# for i in range(len(l)-1):
#     if l[i] <= l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:    
#     print("your list is sorted")        


#7) check if list is pallindromic or not 

l = [2,3,15,15,3,2]
r = []

for i in range(len(l)-1,-1,-1):
    r.append(l[i])

if l == r:
    print("list is pallindromic")
else:        
    print("list is not pallindromic")
