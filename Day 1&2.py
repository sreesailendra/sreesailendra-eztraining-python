           #DAY1
#input and output the integer values
num1=int(input("enter first integer:"))
num2=int(input("enter second integer:"))
num3=int(input("enter third integer:"))

num4=float(input("enter first float:"))
num5=float(input("enter second float:"))
num6=float(input("enter third float:"))

num7=input("enter first string:")
num8=input("enter second string:")

num9=complex(input("enter complex number:"))
print("first integer:",num1)
print("second integer:",num2)
print("third integer:",num3)
print("first float:",num4)
print("second float:",num5)
print("third float:",num6)
print("first string:",num7)
print("second string:",num8)
print("complex number:",num9)

>>> a=36
>>> print("roll no:"+str(a))
roll no:36
>>> print("roll no:",a)
roll no: 36
>>> a=345

#swapping using temp
n1=input("enter n1:")
n2=input("enter n2:")
t=n1
n1=n2
n2=t
print("n1=",n1)
print("n2=",n2)

#swapping without using temp
n1=input("enter n1:")
n2=input("enter n2:")
n1,n2=n2,n1
print("n1=",n1)
print("n2=",n2)

#area of triangle
l=float(input("enter length:"))
b=float(input("enter breadth:"))
area=l*b
print("area=",area)

#perimetre of triangle
l=float(input("enter length:"))
b=float(input("enter breadth:"))
perimeter=2*(l+b)
print("perimeter=",perimeter)



            #DAY2

#  check number whether it is Even Positive,Even Negative,Odd Positive,Odd negative
num=int(input("enter a number:"))
if num%2==0:
    if num>=0:
        print('given number is even-positive')
    else:
        print('given number is even-negative')
else:
    if num>=0:
        print("given number is odd-positive")
    else:
        print('given number is odd-negative')

#input a number and check if it is 500 or not
num=int(input("enter a number:"))
if num==500:
   print("it is 500")
else:
    print("it is not 500")


#  check the given number is integer or float

n=87.544
if n==int(n):
    print('n is an integer')
elif n==float(n):
    print('n is a float number')

#second method

n=5.0
if isinstance(5,int)==True:
    print('n is integer')
else:
    print('n is float')
    
#third method
n=10.3
res=n-int(n)
if res==0 :
   print('n is integer')
else:
    print('n is float')


#  logical operators
n1,n2=int(input("enter first number")),int(input("enter second number"))
print("{}&{}={}".format(n1,n2,n1&n2))
print("{}|{}={}".format(n1,n2,n1|n2))
print("{}^{}={}".format(n1,n2,n1^n2))
print("~{}={}".format(n1,~n1))
print("~{}={}".format(n2,~n2))


#  Divisible by both 5 and 2
n=int(input("enter a number"))
if n%10==0:
    print('{} is divisible by both 2 and 5'.format(n))
else:
    print('{} is not divisible by both 2 and 5'.format(n))

#  find product of 10 integer numbers
a=list(map(int,input("numbers=").strip().split()))[:10]
i=0
while(1<10):
 print(a[i]*a[i+1])
 i+=1


#loops
 #while loop
 i=1
while i<=20:
      if i%2==0:
        print(i)
      i=i+1

  #for loop
   for i in range(1,10):
    print(i)

   for i in range(1,10,2):
     print(i)
     
#  input 3 numbers find greatest number
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1>n2:
    if n1>n3:
        print('{} is greatest number'.format(n1))
if n2>n1:
    if n2>n3:
        print('{} is greatest number'.format(n2))
if n3>n1:
    if n3>n2:
        print('{} is greatest number'.format(n3))

#  print patterns

''' pattern programs
     1.upside down filled triangle
     2.hollow heart
     3.frog '''
print('.','.','.','.','.',sep=' ')
print('','.','.','.','.','',sep=' ')
print('','','.','.','.','',sep=' ')
print('','','','.','.','',sep=' ')
print('','','','','.','',sep=' ')


print('','m','m','','m','m','',sep='  ')
print('m','','','m','','','m',sep='  ')
print('m','','','','','','m',sep='  ')
print('','m','','','','m','',sep='  ')
print('','','m','','m','','',sep='  ')
print('','','','m','','','',sep=' ')

#  switch case using if elif else
'''temp >45          hottest
        40-45       hot
        25-40       moderate
        10-25       cold
        below 10    chill '''

temp=int(input("temperature is :"))
if temp>45:
    print("hottest")
elif temp>=40:
    print("hot")
elif temp>=25:
    print("moderate")
elif temp>=10:
    print("cold")
else:
    print("chill")

# comparision between numbers
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1>n2:
    print('{}>{}'.format(n1,n2))
elif n1<n2:
    print('{}<{}'.format(n1,n2))
else:
    print('{}={}'.format(n1,n2))


#  output using sep and end
print("i","am","very",'hungry',sep='@',end='')
print('its','time','to','eat',sep='$',end='%%%%')
print('yo')

#multiple inputs and mapping them into a list
n=int(input("size="))
a=list(map(int,input("numbers=").strip().split()))[:n]
print(a)


#guess the number game
import random
n= random.randrange(1,50)
guess=int(input('enter any number:'))
while n!=guess:
    if guess<n:
        print('too low')
        guess=int(input('enter any number:'))
    elif guess>n:
        print('too high')
        guess=int(input('enter any number:'))
    else:
        break
print('you guessed it right')

              







    

    



    


