#prog to print the given list one by one
L=list(map(int,input("Enter 10 elements:").split(",")))
for i in range(len(L)):
           print(L[i],end=" ")
           i=i+1

#prog to print the sum and avg of 5 floating numbers
L=list(map(float,input("Enter 5 floating point numbers:").split(",")))
sum=0
for i in range(len(L)):
           sum=sum+L[i]
           i=i+1
print("Sum=",sum)
print("Average=",(sum/len(L)))

#prog to print the even numbers in the list
L=list(map(int,input("Enter 6 elements:").split(",")))
for i in range(len(L)):
    if(L[i]%2==0):
        print(L[i],end=" ")
    else:
        pass

#prog to print the even numbers in the list taking n inputs 
L=list(map(int,input("Enter the elements:").split(",")))
for i in range(len(L)):
    if(L[i]%2==0):
        print(L[i],end=" ")
    else:
        pass


#prog to print the prod and sum based on the given condition
L=list(map(int,input("Enter the elements:").split(",")))
prod=1
sum=0
for i in range(len(L)):
    prod=prod*L[i]
    sum=sum+L[i]
if(prod<750):
     print("Product of the given numbers:",prod)
else:
     print("Sum of the given numbers:",sum)


    





                                                              
                                                              
           
