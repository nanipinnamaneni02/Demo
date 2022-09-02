#!/usr/bin/env python
# coding: utf-8

# In[43]:


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


# In[46]:


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
#Join A and B
C = A.union(B)
print(C)
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
A.update(B) #A with B
print(A)
B.update(A)  #B with A
print(B)
#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
symmetry = A.symmetric_difference(B)
print('The symmetry between A and B is=', symmetry)
###Delete the sets completely
A.clear()
print(A)
B.clear()
print(B)


# In[25]:


#########Q5
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
print("_circum_of_circle_ = %.2f" %circumference)
print("_area_of_circle_= %.2f" %area)


# In[26]:


###########Q6
a = input("Please enter a sentence: ")
unique = set(a.split(' '))
b = len(unique)
print("the no of unique words used in this sentense: ",b)


# In[27]:


#############Q7
a = ('Name    \tAge\tCountry  \tCity')
b = ('Asabench\t250\tFinlnd   \tHelsink')
print(a) 
print(b)


# In[55]:


#############Q8
radius = 10
area = 3.14 * radius * radius
print(f'The area of the circle with radius 10 is {area:.0f} meters square')


# In[ ]:


##############Q9
# number of students
n = int(input("Enter number of students : "))
# this line read inputs from user using map() functio
a = list(map(int,input("\nEnter weights of students : ").strip().split()))[:n]
print("\nL1 : ", a)
b=[i/2.2048364154 for i in a]
b=['%.2f' % elem for elem in b]
print(b)


# In[56]:


import numpy as np  #importing important python libraries
import matplotlib.pyplot as plt  
import pandas as pd  
dataframe=pd.read_csv("dataset.csv")#reading the dataset
x= dataframe['Feature'].values  
y= dataframe['Class'].values 
#dividing data equally into training and testing data
from sklearn.model_selection import train_test_split  
features_tr, features_te, label_tr, label_te= train_test_split(x, y, random_state=0, train_size= 0.5 ) 
#reshaping the data feature and labes into 2D array
features_tr = np.array(features_tr).reshape(-1,1)
features_te = np.array(features_te).reshape(-1,1)
#Normalizing data
from sklearn.preprocessing import StandardScaler    
normalization= StandardScaler()    
features_tr= normalization.fit_transform(features_tr)    
features_te= normalization.transform(features_te)  
#fiting the training data into classifier model 
from sklearn.neighbors import KNeighborsClassifier  
model= KNeighborsClassifier(n_neighbors=3 )  
model.fit(features_tr, label_tr)
#Predicting the test set result  
predict_class= model.predict(features_te)  
print("Predicted Test Samples Output:",predict_class)

#creating a confusion matrix
from sklearn.metrics import confusion_matrix  
model_evaluation= confusion_matrix(label_te, predict_class) 
print("Confusion matrix:\n",model_evaluation)
#finding model accuracy
count=sum(sum(model_evaluation))
accuracy=(model_evaluation[0,0]+model_evaluation[1,1])/count
print ('Accuracy =: ', accuracy)
# finding model sensitivity
sense = model_evaluation[0,0]/(model_evaluation[0,0]+model_evaluation[0,1])
print('Sensitivity =: ', sense )
#finding model specificity
speci = model_evaluation[1,1]/(model_evaluation[1,0]+model_evaluation[1,1])
print('Specificity =: ', speci)


# In[ ]:




