#!/usr/bin/env python
# coding: utf-8

# In[69]:


##############################################question1
# sorting the list
ages = [19,22,19,24,20,25,26,25,24]
ages.sort()
print("sorted list is : ",end="") #sorting the list
print(ages)
print("Max age is : ",end="") #finding the max age
print(max(ages))
print("Min age  is : ",end="") #finding the min age
print(min(ages))
ages.extend([min(ages)]) # adding min age in list 
print("after the adding of the min age again to the list : ",end="")
print(ages)
ages.extend([max(ages)])  # adding max age in list
print("after the adding of the max age again to the list : ",end="")
print(ages)
import statistics  # Find the median age (one middle item or two middle items divided by two)
print("Median of 19,22,19,24,25,26,25,24  is : ",end="")
print(statistics.median([19,22,19,24,20,25,26,25,24]))
# Find the average age (sum of all items divided by their number)
def Average(ages):
    return sum(ages) / len(ages)
ages = [19,22,19,24,20,25,26,25,24]
average = Average(ages)
print("Average  age =", round(average, 2))
#Find the range of the ages (max minus min)
ages = [19,22,19,24,20,25,26,25,24]
max_val = max(ages)
min_val = min(ages)
range_ = max_val - min_val
print("range of ages   : ",end="")
print(range_)


# In[61]:


#question 2
dog = {}
dog["name"] = "triksy"
dog["colour"] = "brown"
dog["breed"] = "golden retriever"
dog["legs"] = "four"
dog["age"]= "seven year"
print(dog)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


student = {"first_name":"nani",
           "last_name":"pinnamaneni",
           "gender":"male",
           "age":"23",
           "marital status":"single",
           "skills":["AutoCAD"],
           "country":"india",
           "city":"vijayawada",
           "adress":"#321 st"}
print(student)
p=len(student)
print(p)
print(student["skills"])
print("student skills",student["skills"],type(student["skills"]))
student["skills"]="AutoCad,python"
print(student)
keyslist =(student.keys())
print(keyslist)
keyslist = (student.values())
print(keyslist)


# In[45]:


############ Q3
##Create a tuple containing names of your sisters and your brothers
brothers_tuple = ('nithin','manoj')
sisters_tuple  = ('priyanka','chinni')
siblings = brothers_tuple + sisters_tuple
print(siblings)
x = len(siblings)
print( "no. of siblings  =", x )
family_members = siblings + ('ram','chandrasena')
print(family_members)


# In[70]:


######Q4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'Oracle','Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("The length of set is:", len(it_companies))
company = ('twitter')
it_companies.add(company)
print(it_companies)
multiple_companies = {'TCS','DELOITTE'}
it_companies.update(multiple_companies)
print(it_companies)
it_companies.remove('Amazon') 
print(it_companies)
#   remove() method will raise an error if the specified item does not exist, and the discard() method will not.
C = A.union(B)#Join A and B
print(C)
print(A.intersection(B))#Find A intersection B
print(A.issubset(B))#Is A subset of B
print(A.isdisjoint(B))#Are A and B disjoint sets
#Join A with B and B with A
A.update(B) #A with B
print(A)
B.update(A)  #B with A
print(B)
#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
symmetry = A.symmetric_difference(B)
print('The symmetry between A and B is=', symmetry)# the symmetric difference between A and B
###Delete the sets completely
A.clear()
print(A)
B.clear()
print(B)


# In[76]:


#########Q5
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))#input allows user to pass the dynamic input
diameter = 2 * radius  #formula for diameter of circle
circumference = 2 * PI * radius  #formula for circumference of circle
area = PI * radius * radius #formula for area of circle
print("_circum_of_circle_ = %.2f" %circumference)
print("_area_of_circle_= %.2f" %area)


# In[79]:


###########Q6
a = input("Please enter a sentence: ")
unique = set(a.split(' '))
b = len(unique)
print("the no of unique words used in this sentense: ",b)


# In[68]:


#############Q7
a = ('Name    \tAge\tCountry   \tCity\nAsabench\t250\tFinlnd   \tHelsink')

print(a) 


# In[81]:


#############Q8
radius = 10
area = 3.14 * radius * radius
print(f'The area of the circle with radius 10 is {area:.0f} meters square')


# In[80]:


##############Q9
# number of students
n = int(input("Enter number of students : "))
# this line read inputs from user using map() function
a = list(map(int,input("\nEnter weights of students : ").strip().split()))[:n]
print("\nL1 : ", a)
b=[i/2.2048364154 for i in a]
b=['%.2f' % elem for elem in b]
print(b)


# In[85]:


print("training: 1o,2o,3x,6x\nTesting: 6x,7o,10o,11o")
print("TN : 1\tFP: 0\nFN: 0\tFP: 5\nAccuracy: 1\nSensitivity: 1\nSpecificity: 1")


# In[ ]:




