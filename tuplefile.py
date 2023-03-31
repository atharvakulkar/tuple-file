#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().set_next_input('Ques 1 Q1. What are the characteristics of the tuples? Is tuple immutable');get_ipython().run_line_magic('pinfo', 'immutable')
ANS-- Tuple items are ordered, unchangeable, and allow duplicate values.
        Tuple items are indexed, the first item has index [0] , the second item has index [1] . tuple are immutable
    
    


# In[6]:


Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why
tuples have only two in-built methods as compared to Lists.

ans-
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
 Python Tuples is an immutable collection of that are more like lists. Python Provides a couple of methods to work with tuples
    


# In[7]:


get_ipython().set_next_input('Which collection datatypes in python do not allow duplicate items');get_ipython().run_line_magic('pinfo', 'items')


ans- 
Set is a collection which is unordered and unindexed. No duplicate members.


# In[9]:


l=  [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)


# In[ ]:


Q4. Explain the difference between the union() and update() methods for a set. Give an example of
each method.
They are very different. 
One set changes the set in place, while the other leaves the original set alone, and returns a copy instead.
update() adds all missing elements to the set on which it is called whereas set.
union() creates a new set. Consequently, the return value of set.
example-
s.union(t)  s | t   new set with elements from both s and t

s.update(t) s |= t  return set s with elements added from t


# In[11]:


What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.



A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
example-->>


# In[13]:



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[ ]:


Can we create a nested dictionary? If so, please give an example by creating a simple one-level
nested dictionary.
In Python, a nested dictionary is a dictionary inside a dictionary. 
It's a collection of dictionaries into one single dictionary.
Here, the nested_dict is a nested dictionary with the dictionary dictA and dictB.
They are two dictionary each having own key and value.
  
    
    example=


# In[14]:





people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)


# In[ ]:


Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of
the key as this list ['Python', 'Machine Learning’, 'Deep Learning']
dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
                      


# In[26]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
print("Dictionary before using setdefault():", dict1)
ret_value = dict1.setdefault('Deep Learning','Data Science Masters' )
ret_value = dict1.setdefault('Machine Learning','Data Scicence Masters')
print("Return value of setdefault():", ret_value)
  
print("Dictionary after using setdefault():", dict1)


# In[ ]:



What are the three view objects in dictionaries? Use the three in-built methods in python to display
these three view objects for the given dictionary.
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}



ans-
The main view objects of dictionary in python are keys, values and items.




# In[ ]:







# In[ ]:





# In[ ]:





# In[ ]:




