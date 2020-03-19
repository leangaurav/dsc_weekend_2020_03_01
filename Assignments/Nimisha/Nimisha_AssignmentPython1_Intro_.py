#!/usr/bin/env python
# coding: utf-8

# 1. Predict output

# In[1]:


s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
print(len(s1), len(s2))


# 2. WAP to input a string and print its length

# In[7]:


n1 = 'NIMISHAMBA'
print('The length of the string: {} is {}'.format(n1,len(n1)))


# 3. WAP to input 2 numbers and print thier sum and difference

# In[9]:


n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number"))
sum=int(n1+n2)
sum1=int(n1-n2)
print('\n the sum of number {} and {} is {} '.format(n1,n2,sum))
print('\n the difference of number {} and {} is {}'.format(n1,n2,sum1))


# 4. predict output

# In[11]:


s1 = 'ab'
s2 = 'de'
s3 = s1+s2
print(s3)


# 5. predict output

# In[12]:


s1 = 'ab'
s2 = 'de'
s3 = s1+s2
print(s3)


# 6. predict output

# In[13]:


s1 = 'ab'*4
print(s1)


# 7. predict output
# 

# In[14]:


s1 = 'ab\n'*4
print(s1)


# 8. WAP to input a string s and a number n.print the string n times on the screen, each should appear in a
# seperate line (do not use any kind of loops, use the multiplication operator)

# In[16]:


s=input('Enter a string ')
n=int(input('Enter a number'))
s=s+'\n'
print(s*n)


# 9. predict output

# In[17]:


res = print('Gaurav')
print(res)


# 10. predict output

# In[18]:


res = len('tuteur.py@gmail.com')
print(type(res))


# 11. predict output
# 

# In[19]:


s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))


# 12.Find the name of function to find the square root. (see all the options available in dir() of math) 

# In[25]:


import math
print(dir(math))

#print(math.sqrt(25))


# 13. WAP to input a number and print its square root().

# In[32]:


n1 = int(input('Enter a number:'))
print('the square root of {} is {}'.format(n,math.sqrt(n)))


# 14. WAP to input 4 numbers from user and print their average

# In[35]:


n1 = int(input('Enter the number: '))
n2 = int(input('Enter the number: '))
n3 = int(input('Enter the number: '))
n4 = int(input('Enter the number: '))
sum = n1+n2+n3+n4
average = sum/4
print("The average of 4 numbers {}".format(average))


# 15. Use the help function to check what the abs function in python does.
# 
# 

# In[41]:


help(abs)


# 16. what is the output of this code when run from python interpreter

#     print(__main__)

# Answer: from interpreter got __main__ as output

# 17. What is the output of this code when run from a python script.

# In[44]:


print(__name__)
print(dir(__name__))


# 18. Does the dir of int class contain an attribute __name__(Y/N).

# In[46]:


dir(int)
print(dir(int))


# In[ ]:


Answer : No
    the dir(int) class does not conatain an attribute __name__
    


# 19. Predict the output of :

# In[50]:


print(__name__)
print(__builtins__.__name__)
print(int.__name__)


# In[ ]:




