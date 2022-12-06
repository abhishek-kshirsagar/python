#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Area of triangle
b=int(input("Input the base:"))
h=int(input("Input the height"))
area=b*h/2
print("area=",area)


# In[4]:


#swap two variable
a=int(input("Enter No:"))
b=int(input("Enter No:"))
a,b=b,a
print("a=",a)
print("b=",b)


# In[6]:


#Generate a random number
import random
print(random.randint(0,9))


# In[14]:


#possitive or negative of zero
num=float(input("Enter Number="))
if(num>0):
    print("Number is possitive")
elif (num<0):
    print("Number is negative")
else:
    print("number is 0")


# In[18]:


#number is odd or even
A=int(input("Enter Number:"))
if(A%2==0):
    print("Number is Even")
else:
    print("Number is odd")


# In[31]:


#check prime number
num=int(input("Enter Number="))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"Number is not prime")
            break
        else:
                print(num,"Is prime")
                break


# In[6]:


#check Armstrong number
n=int(input("Enter no"))
s=0
t=n
while t>0:
    d=t%10
    s+=d**3
    t//=10
if n==s:
    print(n,"no is arm")
else:
    print(n,"no is not arm")


# In[8]:


#find the factorial of a number 
num=int(input("Enter Number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print("Factorial is",num,fact)


# In[61]:


# string is symmetrical or palindrome
def palin(string): 
    st = 0
    end = len(string)-1
    f = 0
while(st<end): 
    if(string[st]== string[end]): 
        st+= 1
        end-= 1
else: 
    f= 1
    break;
    if f==0: 
    print("The entered string is palindrome") 
else: 
    print("The entered string is not palindrome") 
def symm(string): 
    l = len(string) 
    flag=0
if l%2 == 0: 
    mid = l//2 
else: 
    mid = l//2 + 1 
    
    s1 = 0  
    s2 = mid 
while(s1 < mid and s2 < l): 
    
    if (string[s1] == string[s2]): 
        s1 = s1 + 1
        s2 = s2 + 1
else: 
        flag = 1
        break
if flag==-0: 
    print("The entered string is symmetrical") 
else: 
    print("The entered string is not symmetrical") 
string = input("Enter the string: ")
palin(string) 
symm(string)


# In[63]:


# reverse the string in python
a=input("Enter the string")
A=""
for i in a:
    A=i+A
print("string in reverse order",A)


# In[68]:


#remove ith character from string
A=input("Enter the string")
B=int(input("Enter the ith value"))
D=B+1
C=A[:B]+A[D:]
print("The required string is:",C)


# In[4]:


#max of three numbers
def maximum(a,b,c):
    list=[a,b,c]
    return max(list)
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
print("Maximum number is ::>",maximum(x,y,z))


# In[5]:


#sum of all no list
num=[1,2,3,4,5]
total=0
for x in num:
    total+=x
    
print(total)


# In[6]:


def sum():
    a=[5,6,9,88,22,55,66,83,2]
    b=0
    for m in a:
        b=b+m
    print("sum of all numbers in a:",b)


# In[18]:


#function to rev string
A=input("Enter the string reverse")
def reverse(A):
    str=""
for i in A:
    str =i+str
return str


# In[13]:


#print even lenght words in a string
n=input("Enter the string")
s = n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)
    


# In[25]:


#string which contains all vowels
A=input("Enter the string")
B=A.split(" ")
for K in B:
    for j in k:
        if(j==a and j==e and j==i and j==o and j==u):
            print("string contain vowels",j)
    else:
            print(" string dose not contain any vowels:")
        


# In[27]:


#number of matching character in a pair of string
A=input("Enter string 1:")
B=input("Enter string 2:")
C=set(A).intersection(B)
print("the number matching character",len(C))


# In[41]:


#function to perfect no
def num_perfect(num):
    sum_n=0
    for i in range(1, num):
        if num%i==0:
            sum_n=sum_n+i
    return sum_n == num
print(num_perfect(26))


# In[1]:


#,sum of elements inn list
A=[5,3,8,9,5,6,8]
B=sum(A)
print("sum of elements in A :",B)


# In[37]:


#multiple elements in list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((1,2,3,4)))


# In[4]:


#sort list
my_numbers = [10,4,6,3,7,9,]

my_numbers.sort()

print(my_numbers)


# In[5]:


#create touple 
A=("Rbnb","Dvp","Cdj","98")
print(A)


# In[7]:


#touple with different data types
A=(2,5,6,8,1,9,2,71,2)
print(A)
#float touple
B=(2,2,22,5,22,6,88,6,22.01,33.05)
print(B)
#character touple
C=("A","B","C","E","F")
print(C)
#string touple
D=("rbnb","cdj","dvp")
print(D)
#mixed touple
E=("rbnb",10,10.3,"10aaa","A")
print(E)


# In[15]:


#check whether an elements exists within touple
touple=("w",3,"r","e","s","o","u","r","c","e")
print("r" in touple)
print(5 in touple)


# In[17]:


#create set
A={2,3,5,6,8,9,6,6,7,44}
print(A)
B={"a","b","c","d","e","f","g","h"}
print(B)
C={"ram","RRR"}
print(C)
#Empty set
D={}
print(D)
#mix value set
mix={1,"cdj",5,5,"dd",(1,2,3,4)}
print(mix)


# In[1]:


A={1,2,"rbnb",(1,5,6,9),"CDJ"}
print(A)
A.add(55)
A.update([5,6,9,8])
print(A)
A.discard("rbnb")
print(A)
A.remove(2)
print(A)
B={99,88,66,55,5,"rbnb",2}
C=A.union(B)
print(C)


# In[2]:


#create set difference
A={1,32,5,6,2,4,586,85}
B={2,5,32,5,1,8,15,2,82,85}
print("set A",A)
print("set B",B)
C=A.difference(B)
print("set difference between A and B",C)


# In[26]:


#sort a dictionary by value
dict1={82:2 ,99:3 ,2:5 ,9:7}
sorted_values = sorted(dict1.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[K] == i:
            sorted_dict[K] = dict1[K]
    print(sorted_dict)


# In[20]:


#add key to dictionary
A={82:"name",99:"RBNB",2:"dictionary",9:"CDJ"}
A[5]:"DVP college shrirampur"
print("Updated A:",A)
A[1]:2589631479630.11346
print("Updated after adding :",A)


# In[27]:


#iterate over dictionary
d1={'name': 'sham', 'age' : 43, 'marks' : 96}
for k,v in d1.items():
    print(k,v)


# In[29]:


#remove dublicate from a list
A=[2,3,5,4,4,4,4,5,5,6,9,8,7,3,2]
B=[]
for i in A:
    if i not in B:
        B.append(i)
        print(B)


# In[31]:


#check empty list
A=[]
B=len(A)
if(B==0):
    print("list is empty")
else:
        print("list contain elements")


# In[33]:


#covert list to a touple
def convert(list):
    return tuple(list)
list = [1,2,3,4]
print(convert(list))


# In[34]:


#remove item from tuple
""" we cannot change the element s in a tuple. it means that we cannot 
delete or remove from a tuple.
deleting a tuple entirely, however, is possible using the keyword del"""
a = (1,2,3,4,5)
b = a[:2] + a[3:]
print(b)


# In[35]:


#slice tuple
#tuple[start : stop : stride]
A= ('a','b','c','d','e','f','g','h','i','j')
print(A[0:6])
print(A[1:9:2])
print(A[-1:-5:-2])


# In[37]:


#find the lenght of a tuple
# use lenght fuction(len(tuple))
A=(1,2,3,4,5,6,7,8,9,0)
print("lenght of tuple is:",len(A))


# In[46]:


#check set is subset
A={1,2,3,4,5,6,7,8,9,0}
B={1,2,3,4,5}
if(A.issubset(B)):
    print("A is subset of B")



# In[47]:


#find max&min in set
A={1,88,66,51,95,42,82,69,36,58}
B=max(A)
C=min(A)
print("Maximum value in set is:",B)
print("Minimum value is set is:",C)
