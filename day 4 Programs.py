#Program 1
#create a list with 8 customer names ,display a dictionary which has customers names along with discounts for them fdirom a particular shop

import random
customers=['luffy','nami','robin','zoro','sanji','franky','trafalgar','chopper']
discount={name:random.randint(1,100) for name in customers}
print(discount)


#progarm 2
#create 2 lists ,list1 should have 5 students names and list2 should have their total marks
#create a dict ,names and percentage  

#method 1
names=['shanks','buggy','roger','releigh','trafalgar']
marks=[360,200,490,450,400]
d={n:p/500*100 for (n,p) in zip(names,marks)}
print(d)

#method 2
import random
name=list(map(str,input('enter names:').split()))
marks=[]
for i in range(len(name)):
    a=(random.randint(300,500)/500)*100
    marks.append(a)
dict={x:y for (x,y) in zip(name,marks)}
print(dict)


PROGRAMES

[1] input a string and a charcter and find out and display whether that particular character is present in the string or not
program:  

name=input("enter a string:")
letter=input("enter a letter:")
if letter in name:
    print("{} is not present in {}".format(letter,name))
else:
    print("{} is not present in {}".format(letter[0],name))
  .............................................................
#second method
name=input("enter a string:")
letter=input("enter a letter:")
for i in name:
    if i==letter:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("{} is present in {}".format(letter[0],name))
else:
    print("{} is  not present in {}".format(letter[0],name))
  ...............................................................
#third method
st=input('enter the string:')
char=input('enter a char:')
a='yes' if char in st else 'no'
print(a)


[2] check whether the given string is palandrome or not
program:
string = input("Enter string : ") 
revstr = ""
for i in string: 
    revstr = i + revstr   
print("Reversed string : ", revstr) 
 
if(string == revstr): 
   print("The string is a palindrome.") 
else: 
   print("The string is not a palindrome.")

[3] input a string and check string contains space or not , if yes return the number of space in string 
program:

s=input('enter a string:')
count=0
for i in s:
    if i==' ':
       count+=1
print(count)

[4] create a list with vowels get one string as input and count vowels in that string
program:

v=['a','e','i','o','u','A','E','I','O','U']
s=input("enter a string")
count=0
for i in range(len(s)):
    if s[i] in v:
        count += 1
print("Number of vowels in the given string is: ", count)

        



