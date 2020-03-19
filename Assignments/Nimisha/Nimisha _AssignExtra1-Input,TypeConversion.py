#!/usr/bin/env python
# coding: utf-8

# 1. Write a program to Input temperature in Fahrenheit and print in Celsius

# In[12]:


fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = round((fahrenheit - 32) * 5/9,1)
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))


# 2.Write a program to input a number and print its square and cube. 

# In[19]:



number = float(input(" Please Enter any numeric Value : "))

square = number * number
cube   = number*number*number 
print("The Square of a Given Number{0}  = {1} ".format(number, square))
print("The cube of a Given Number {0}  = {1}".format(number, cube))


# In[21]:


#3.WAP to input a number n and a number m and print the result of following n2+m2
n=int(input("enter number :"))
m=int(input("enter number  "))
result=n ** 2 + m **2
print("result",result)


# In[26]:


#4.WAP to input a numbers M and N and print result of MN
m=int(input("enter number :"))
n=int(input("enter number  "))
result=pow(m,n)
print(result)


# In[31]:


m=int(input("enter number :"))
n=int(input("enter number  "))
result=(m)*(n)
print(result)


# In[32]:


#5.Write a simple interest calculator
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))

SI = (P * N * R)/100
print("Simple interest : {}".format(SI))


# In[33]:


#6.Input Principal, Rate, Time and print Compound Interest and Amount
p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))
# calculating compound interest
ci =  p * (pow((1 + r / 100), t)) 

# printing the values
print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("Time in years     : ", t)
print("compound Interest : ", ci)


# In[2]:


#7.WAP to print sum of first n natural numbers. (n needs to be taken as input)
n = input("Enter Number ")
n = int (n)
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )


# In[6]:


#8.WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and also the pythonic way). 
# Python program to swap two variables

#x = 5
#y = 10

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print("using temp variable",x,y)

x, y = y, x   #using pythonic way
print("using pythonic way", x, y)


# In[27]:


#9. WAP to print ascii value of all white-space characters present in python. 

print(ord('\n'))
print(ord('\t'))

 


# In[38]:


#10. Input a single character and print its ascii values. 
ch=input("enter any character:")
print("the ASCII vale of char"+ch+"is:",ord(ch))


# In[42]:


#11. WAP that takes area of a circle and gives back the radius and circumference.

PI =3.14
radius=float(input("input the radius of the circle: "))
area = PI * radius * radius
circumference = 2 * PI * radius

print("Area of a circle=%.2f" %area)
print("circumference of a circle=%.2f" %circumference)




# In[3]:


#12. We need to input marks in 5 subjects out of 100 and print percentage. 

sub1=float(input("enter marks of english:"))
sub2=float(input("enter marks of kannada"))
sub3=float(input("enter marks of hindi"))
sub4=float(input("enter marks of maths"))
sub5=float(input("enter marks of science"))
sum=sub1+sub2+sub3+sub4+sub5
percentage=(sum/500)*100
print("the percentage of all 5 subjects : ",percentage)


# In[ ]:





# In[ ]:




