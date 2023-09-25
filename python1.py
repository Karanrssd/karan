# tup1=(23,34,32,23)
# # a=min(tup1)
# # print(a)
# tup1=(23,34,32,43)
# b=max(tup1)
# print(b)
# l=[1,"sparta",3.2,"True"]
# print(type(l))
# print(l[3])
# l.insert(2,4)
# print(l)
# l.append(23.43)
# print(l)
# l.reverse()
# print(l)
# l2=["mohan","aohan","karan"]
# l2.sort()
# print(l2)
# from audioop import reverse


# newlist = [x for x in range(10) if x<5]

# print(newlist)
# from audioop import reverse


# newlist=[23,43,54,23,674,1234,1231,34,12]
# # newlist.sort(reverse=True)
# newlist.sort()
# print(newlist)
# thislist=["banana","Apple","Mango","Fruits"]
# # thislist.sort(key=str.lower)
# print(thislist)
# mylist=thislist
# print(mylist)
# mylist=list(thislist)
# print(mylist)
# mylist=["asfca",'fw',"apple"]
# list3=thislist+mylist
# print(list3)
# list2=[1,2,3]
# for x in list2:
#     thislist.append(x)
# print(thislist)
# print(thislist[2])
# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)
# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)
# set1 = {"a", "b" , "c","4"}
# set2 = {1, 2, 3,4}

# set3 = set1.union(set2)
# print(set3)
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "Year":1833,
#     "Year":2354
# }
# mydict=thisdict.copy()
# mydict
# print(mydict)
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "Year":1833,
#     "Year":2354
# }
# y=thisdict.keys()
# z=thisdict.values()
# print(y)
# print(z)
# thisdict["color"]="white"
# y=thisdict.keys()
# print(y)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()      ---------------------------------IT WILL DELETE THE LAST ITEM OF THE DECTIONARY
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# x = 15
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# i = 0
# while i < 6:
#   i += 1
#   if i==3:
#     continue
#   print(i)

#  numpy library
import random
import numpy as np
# n1 = np.array([23, 24, 32, 43])
# n2 = np.array([23, 24, 64, 12])
# d=np.intersect1d(n1, n2)
# print(d)
# f=np.setdiff1d(n1,n2)
# print(f)
# n1=np.array([12,42])
# n2=np.array([12,34])
# d=np.sum([n1,n2])
# print(d)
# d=np.sum([n1,n2],axis=0)
# print(d)
# d=np.sum([n1,n2],axis=1)
# print(d)
# n3=n1+5
# print(n3)
# n4=n1*3
# print(n4)
# n5=n1/3
# print(n5)
# n6=np.mean(n1)
# n7=np.median(n2)
# print(n6)
# print(n7)
# n8=np.std(n1)
# print(n8)
# from matplotlib import pyplot as plt
# from cProfile import label
# from optparse import Values
# from re import X
# from turtle import color
# from matplotlib.lines import lineStyles
# import pandas as pd
# import numpy as np

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print('5th element on 2nd row: ', arr[1, 4])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])
# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:1])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[::2])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 1:4])
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=0)

# print(arr)
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))

# print(arr)
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)
# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 4)

# print(newarr)-----------------------------------------------------------------------------------
# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# x = np.where(arr%2 == 0)

# print(x)
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)
# arr = np.array([41, 42, 43, 44])
# import numpy as np
# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is completely divisble by 2, set the value to True, otherwise False
#   if element % 2 == 0:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)
# from numpy import random

# x=random.randint(100, size=(5))

# print(x)
# from numpy import random

# x = random.randint(100, size=(3, 5))

# print(x)
import pandas as pd
# s1=pd.Series([1,2,3,4,5])
# # print(s1)
# print(s1)
# d=pd.DataFrame({"date":["karan","subham","Sohan"],"marks":[32,43,55,54]})
# print(d)
# import pandas
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)
# import pandas as pd
# print(pd.__version__)

# import pandas as pd
# a=[12,34,543,54]
# my_var=pd.Series(a)
# print(my_var)

# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)
import pandas as pd
data={"name":"karan","course":"btech"}
new=pd.DataFrame(data)
print(new)

# arr=[1,2,3,4]
# # myvar=pd.DataFrame(arr)
# myvar=pd.Series(arr,index=["a","b","C","d"])
# print(myvar)
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df=pd.DataFrame(data)
# print(df)
# S1=pd.Series([1,3,4,5,6])
# print(S1)
# print(type(S1))
# S1=pd.Series([1,2,4,5,6],index=['a',"b","c","d","e"])
# print(S1)
# d = pd.Series({"a": 10, "b": 20, "c": 30})
# print(d)
# e=pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40},index=['c', 'b', 'a', 'd'])
# print(e)
# S1=pd.Series([1,2,34,53,54,36,45])
# print([S1[2]])
# print(S1[:4])
# print(S1[-4:6])--------------------------------------------------------------------------
# l1=[1,2,3,4,5,6,7,8,9,0]
# l1=pd.Series(l1)
# # print(l1)
# u=l1+2
# # print(u)
# u1=l1*3
# print(u1)
# u2=pd.DataFrame({"name":["karan","mohan","sohan"],"class":["bob","sob","tob"]})
# print(u2)
# u = pd.read_csv('karan.csv')
# l=u.head()
# l=u.tail()
# l=u.shape
# l=u.describe()
# print(l)
# l=u.iloc[0:3,0:2]
# print(l)
# l=u.loc[0:3,0:2]
# print(l)
# l=u.drop("id",axis=1)
# print(l)
# print(u.mean())
# print(u.median())
# print(u.max())
# print(u.min())
# def double_make(s):
#     return s*2
# u.["id", "salary"].apply(double_make)-----------------------------------
# l=u["SALARY"].value_count()
# print(l)


# x=np.arange(1,11)
# y=2*x
# plt.plot(x,y,color="g",linestyle=":",linewidth=3)
# plt.title("line plot")
# plt.xlabel("this is x axis")
# plt.ylabel("this is y axis")
# plt.show()
# x=np.arange(1,11)
# y1=2*x
# y2=3*x
# plt.plot(x,y1,color="g",linestyle=":",linewidth=3)
# plt.plot(x,y2,color="r",linestyle=":",linewidth=3)
# plt.title("line plot")
# plt.xlabel("this is x axis")
# plt.ylabel("this is y axis")
# plt.show()

# x=np.arange(1,11)
# y1=2*x
# y2=3*x
# plt.subplot(1,2,1)
# plt.grid(True)
# plt.plot(x,y1,color="g",linestyle=":",linewidth=3)
# plt.subplot(1,2,2)
# plt.plot(x,y2,color="r",linestyle=":",linewidth=3)
# plt.title("line plot")
# plt.xlabel("this is x axis")
# plt.ylabel("this is y axis")
# plt.grid(True)
# plt.show()

# student={
#     "bob":87,"julia":45,"anne":100}
# name=tuple(student.keys())
# value=tuple(student.values())
# plt.bar(name,value,color="r")
# plt.xlabel("this is name axis")
# plt.ylabel("this is marks axis")
# plt.grid(True)
# plt.show()
# student={
#     "bob":87,"julia":45,"anne":100}
# name=tuple(student.keys())
# value=tuple(student.values())
# plt.barh(name,value,color="r")
# plt.xlabel("this is name axis")
# plt.ylabel("this is marks axis")
# plt.grid(True)
# plt.show()
# x=[10,20,30,40,50,60]
# y=[8,1,3,4,5,6]
# plt.scatter(x,y,marker="*",color="r",s=100)
# plt.show()
# data=[1,2,3,2,2,2,4,5,4,2,4,5,4,2,1,3,3]
# plt.hist(data)
# plt.show()
# one=[1,2,3,4,5,6,7,8,9]
# two=[1,2,3,4,5,4,3,2,1]
# three=[6,7,8,9,8,7,6,5,4]
# data=list([one,two,three])
# plt.boxplot(data)
# plt.show()
# fruits=["Aple","mango","banana","guava"]
# quantity=[23,45,65,34]
# plt.pie(quantity,labels=fruits,autopct="%0.1f%%")
# plt.show()
# fruits=["Apple","mango","banana","guava"]
# quantity=[23,45,65,34]
# plt.pie(quantity,labels=fruits,autopct="%0.1f%%,radius=2")
# plt.pie([1],colors=["w"],radius=1)
# plt.show()
# n = int(input("ente the number"))
# for i in range(n):
#     print(i)
# n=int(input("enter the number"))
# for i in range(1,n):
#     for j in range(i):
#           print(i,end="")
# print(bin(5)&bin(4))
# x=10
# y=8
# print(bin(x))
# print(bin(y))
# # print(x&y, bin(x&y))
# # print(x&y)
# print(bin(x|y),x|y)
# a=10
# b=20
# a=eval(input("enter the firsr number"))
# b=eval(input("enter the second number"))
# print('sum is',a+b)
# if a>b:
#     print("yes ")
# if a!=b:
#     print("yes")
# -------------------------------------------------------------calculator
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=input("enter the type of operation what you want +,-,*,/ ")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print("invalid operation")
# -------------------------------------------------------------------------------------
# for n in range (10,0,-1):
#     print(n)
# for n in range (1,11,2):
#     print(n)
# for n in range (10,-1,-1):
#     print(n)
# i=1
# while i<=10:
#     print("welcome ")
#     i=i+1
# print(i)
# a=10
# while a>=1:
#     print(a,"hello")
#     a=a-1
# print(a)


# w="hello everyone"
# for i in w:
#     print(i,end="")
# w="welcome"
# print(w.find("c",1))
# print(w.isalpha())
# print(w.isalnum())
# print(w.isdigit())
# a=68
# print(chr(a))
# w="hello world"
# t=len(w)
# for a in range(t-1,-1,-1):
#     print(w[a])

# w=[1,2,3,34,3]
# l=[32,43]
# l.append(w)
# print(l)
# l.extend(w)
# print(l)
# w.pop(2)
# print(w.pop(2))
# l=[]
# for a in range(1,101):
#     l.append(a)
# print(l)
# n=[m for m in range(1,101)]
# print(n)
# l=[12,34,23,212]
# l1=[12,32,32,21,12]
# for a,b in zip(l,l1):
#     print(a,b)
# n=input("Enter the value")
# print(n)
# l=n.split()
# print(l)
# l=[]
# for a in range(1,4):
#     n=input("enter the value"+str(a)+":-")
#     l.append(n)
# print(l)
# --------------------------------------------------------------stack operation in lisr below
# l = []
# while True:
#     c = int(input('''
#     1 push Element
#     2 Pop Element
#     3 peek element
#     4 display element
#     5 Exit
#     '''))
#     if c == 1:
#         n = input("enter the value")
#         l.append(n)
#         print(l)

#     elif c == 2:
#         if len(l) == 0:
#             print("empty string")
#         else:
#             p = l.pop()
#             print(p)
#             print(l)
#     elif c == 3:
#         if len(l) == 0:
#             print("empty String")
#         else:
#             print("last stack value", l[-1])

#     elif c == 4:
#         print("display stack", l)
#     elif c == 5:
#         break
#     else:
#         print("inavalid operation ")
# --------------------------------------------------------------end of stack operation
# l = []
# while True:
#     c = int(input('''
#     1 push Element
#     2 Pop  first Element
#     3 display front element
#     4 last element
#     5 display element
#     6 Exit
#     '''))
#     if c == 1:
#         n = int(input("enter the value"))
#         l.append(n)
#         print(l)

#     elif c == 2:
#         if len(l) == 0:
#             print("empty queue")
#         else:
#             del l[0]
#             print(l)
#     elif c == 3:
#         if len(l) == 0:
#             print("empty queue")
#         else:
#             print("first queue value", l[0])

#     elif c == 4:
#         if len(l) == 0:
#             print("empty queue")
#         else:
#             print("last element in queue is", l[-1])
#     elif c == 5:
#         print("values in queue is",l)
#     elif c==6:
#           break
#     else:
#         print("inavalid operation ")
# -------------------------------------------------------------------------------queue operation

# course={
#         "name":"karan",
#         "sir name":"Singh",
#         "dob":13432
# }
# print(course)
# for k,v in course.items():
#     print(k,v)

# def sum(a,b):
#         c= a+b
#         return c

# d=sum(23,45)
# print(d)
# def showdata():
#         print("hello")
# showdata()
# def sum(a,b=2):
#         print(a+b)

# sum(23,20)
# sum(20)
# -------------------function with default argument
# def square(x):
#     return x*x
# s=square(5)
# print(s)
# import modul1 as md
# md.sum(23,34)
# md.multi(24,3)
# from modul1 import sum
# sum(23,45)
# import math

# from numpy import ceil
# print(math.factorial(4))
# print(math.sqrt(5))
# print(math.ceil(4.7))
# print(ceil(24.6))
# print(math.sqrt(9))
# import random
# a=random.randint(4,10)
# print(a)
# n1=random.randrange(3,10)
# print(n1)
# if a>n1:
#     print("a is winner")
# elif a==n1:
#     print("match is tie")
# else:
#     print("b is winner")
# r=random.random()                 #--------------------print any random value between 0 and 1
# print(r)
# l=[12,32,42,43]
# random.shuffle(l)
# print(l)
# u=random.uniform(3,9)     #write a float value between the given number
# print(u)
# ---------------------------------------------------------computer game
# import random
# rand=random.randrange(1,10)
# userinput=int(input("enter the number for playing a game -:"))
# if userinput>rand:
#     print("input of computer is-: ",rand)
#     print("you win the game your input is",userinput)
# elif userinput==rand:
#     print("match is tie")
# else:
#     print("input of computer is-: ",rand)
#     print("you loss the game your input is",userinput)
# -------------------------------------------------------------
# rock papeer seciser--------------------
# import random
# l = ["rock", "paper", "scissor"]
# while True:
#     ccount = 0
#     ucount = 0

#     uc = int(input('''
#     Game Start............
#     1 YES
#     2 NO |EXIT

#     '''))
#     if uc == 1:
#         for a in range(1, 6):
#             userinput = int(input('''
#             welcome choose any one value
#             1 Rock
#             2 SCissor
#             3 Paper
#             '''))
#             if userinput == 1:
#                 uchoice = "rock"
#             elif userinput == 2:
#                 uchoice = "scissor"
#             elif userinput == 3:
#                 uchoice = "paper"
#             Cchoice = random.choice(l)

#             if Cchoice == uchoice:
#                 print("computer value", Cchoice)
#                 print("your value", uchoice)
#                 print("game Draw")
#                 # ucount = ucount+1
#                 # ccount = ccount+1
#             elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
#                 print("you win")
#                 print("computer value", Cchoice)
#                 print("your value", uchoice)
#                 ucount = ucount+1
#             else:
#                 print("computer  win")
#                 print("computer value", Cchoice)
#                 print("your value", uchoice)
#                 ccount = ccount+1
#         if ucount == ccount:
#             print("game draw")
#             print("user score", ucount)
#             print(" Computer count", ccount)
#         elif ucount > ccount:
#             print("you win the game")
#             print("user count", ucount)
#             print("computer count", ccount)
#         else:
#             print("computer win")
#             print("user count", ucount)
#             print("computer count", ccount)
#     else:
#         break
# -------------------------------------------------------------------rock paper scissor
# l=[12,32,43,32]
# l[0]=32
# l[-1]=12
# print(l)

# def swapList(newList):
#     size = len(newList)

#     # Swapping
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp

#     return newList


# # Driver code
# newList = [12, 35, 9, 56, 24]

# print(swapList(newList))
# class Phone:


#     def make_call(self):
#         print("i am making a call")
#     def play_game(self):
#         print("i am playing a game ")
#     def set_cost(self,cost):
#         self.cost=cost
# p1=Phone()
# p1.make_call()
# p1.play_game()
# '''gsdfgsdg'''
# a="karan"
# print(a)
# a="hello"
# replace convert string into another string
# b=(a.replace("h","k"))
# print(b)
# print(a)
# ----------------------------------------split convert string to list with seperator
# a="Hello ! ,World"
# b=a.split(",")
# print(b)
# print(b[1])
# txt = "We are the so-called \"Vikings\" from the north."
# # txt = "We are the so-called "Vikings" from the north."
# print(txt)
# a="hello world"
# # print(a.rfind("o"))
# # print(a.rindex("o"))
# b=a.encode()
# print(b)
# thislist = ["apple", "banana", "cherry"]

# thislist[1:5] = ["watermelon","apple"]

# print(thislist)
# tup=("kiwi","apple")
# tup1=("banana","mango")
# tup3=tup+tup1
# print(tup3)
# d=tup3.append("afa")
# print(d)
# this={"hello",1}
# # this.add("sdgs")
# # print(this)
# this.add("sdgssdsfa")
# print(this)
# l=["apple","banana"]
# d=type(l)
# print()
# ----------------------------------------------------------------------------
# age = 36
# weight=26
# txt = "My name is John, and I am {} and my weight is {}"
# print(txt.format(age,weight))
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# a=0.0
# b=0
# print(type(a))
# print(type(b))
# ---------------------------------------------------------------
# The escape character allows you to use double quotes when you normally would not be allowed:

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
# thislist = ["apple", "banana", "cherry","cherrya"]
# thislist[1:4] = ["watermelon"]
# print(thislist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict["brand"])
# print(len(thisdict))
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# thisset=set(("apple","banana"))
# print(thisset)
# a=400
# b=40
# if b>a:
#     print("b is greater then a ")
# elif a==b:
#     print("a and b are equal")
# else:
#     print(" a is greter then b")
# i=1
# while i<5:
#     print(i)
#     if i==3:
#         break
#     i+=1
# i=0
# while i<10:
#       if i==2:
#         continue------------------------------------------------------------------------------
#       i=i+1
# print(i)
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)


# my_function(child1="Emil", child2="Tobias", child3="Linus")
# f=open('D:\sdfdas',"r")
# print(f.read())
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
# f = open("demofile2.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile2.txt", "r")
# print(f.read())
# f = open("myfile1.txt", "x")
# # Result: a new empty file is created!
# print(f.read())
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))
# class Vehicle:
#     def __init__(self,milage,cost):
#         self.milage=milage
#         self.cost=cost
#     def show_vehicle_details(self):
#         print("milage of vehicle is",self.milage)
#         print('cost of vehicle is',self.cost)
#         print("i am a vehicle")
# v1=Vehicle(300,500)
# v1.show_vehicle_details()

# ----------------------------inheratance
# class parent():
#     def get_name(self, name):
#         self.name = name

#     def show_name(self):
#         return self.name


# class child(parent):
#     def get_age(self, age):
#         self.age = age

#     def show_age(self):
#         return self.age


# class grandchild(child):
#     def get_gender(self, gender):
#         self.gender = gender

#     def show_gender(self, gender):
#         return self.gender


# gc = grandchild()
# # gc.get_name("karan")
# # gc.show_name()
# gc.get_age(17)
# # gc.get_gender("male")
# gc.show_age()
# gc.show_gender()
# -----------------------------------------------------------inheratence
# s1=pd.Series([1,2,3,4,5])
# print(s1)
# type(s1)
# s1=pd.Series([1,2,3,4,5,6,7,8,9])
# print(s1[-3:])
# s2=s1+5
# print(s2)
# s3=pd.Series([2,4,6,8,10,12,14,16,18])
# print(s1+s3)
# for i in range(1,11):
#     s1=pd.Series([i*2])
#     print(s1)
# p1=pd.DataFrame({"Name":["anne","bob","matt"],"Marks":[75,12,82]})
# print(p1)
# iris=pd.read_csv("age.csv")
# d=iris.head()
# print(d)
# print(iris.shape)
# print(iris.iloc[2:3,1:2])
# d=iris["age"].value_counts()

# d=iris.sort_values(by="name")
# print(d)
# import numpy as np
# from matplotlib import pyplot as plt
# x=np.arange(1,11)
# y1=3*x
# y2=4*x
# plt.plot(x,y1,color="g",linestyle=":",linewidth=5)
# plt.plot(x,y2,color="r",linestyle=":",linewidth=5)
# plt.title("plot")
# plt.xlabel("this is x axis")
# plt.ylabel("this is y axis")
# plt.grid=(True)
# plt.show()
# from matplotlib import pyplot as plt
# students={"bob":98,"matt":56,"sam":27}
# name=list(students.keys())
# values=list(students.values())
# plt.bar(name,values)
# plt.title("students marks distsribution")
# plt.xlabel("name of the student")
# plt.ylabel("marks of the students")
# plt.show()
# ------------------------for vertical bar chart
# students={"bob":98,"matt":56,"sam":27}
# name=list(students.keys())
# values=list(students.values())
# plt.barh(name,values,color="b")
# plt.show()
# plt.title("students marks distsribution")
# plt.xlabel("name of the student")
# plt.ylabel("marks of the students")
# plt.show()
# -----------------------------------------for horizantal bar chart
# x=[10,20,30,40,50,60,70,80,90]
# a=[1,2,3,4,5,6,7,8,9]
# plt.scatter(x,a)
# plt.show()
# -------------------------------scatter plot
# plt.scatter(x,a,marker="*",c="g",s=100)
# plt.show()
# ----------------histogoram chart
# data=[1,3,3,3,3,9,9,5,4,4,8,8,8,6,7]
# plt.hist(data)
# plt.show()
# -------------------pie plot
# fruits=["apple","oranges","mango","guava"]
# quantity=[12,24,45,12]
# plt.pie(quantity,labels=fruits,autopct="%0.1f%%")
# plt.show()
# plt.pie(fruits,quantity,autopct="%0.1f%%")
# plt.show()
# ----------------------------------donat chart
# fruits=["apple","oranges","mango","guava"]
# quantity=[12,24,45,12]
# plt.pie(quantity,labels=fruits,radius=2)
# plt.pie([1],colors=["w"],radius=1)
# plt.show()
# def myname():
#     print("karan singh")

# myname()
# import numpy as np
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# print(d[1,1,0])
# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)
# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])
# import numpy as np

# arr = np.array([1, 2, 3, 4], dtype='i')

# print(arr)
# print(arr.dtype)
# ---------------------------it will give error because a can not converted into string
# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i')
# -----------------------------------------------------change the data type of array
# import numpy as np
# arr=np.array([1.1,2.1,3.1])
# new_arr=arr.astype('i')
# print(new_arr)
# print(new_arr.dtype)
# Change data type from integer to boolean:
# import numpy as np
# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)
# -----------------------------copy and view concept
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)
# ------------------view and copy function
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)
# --------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 8,10])
# ypoints = np.array([3, 10,12])
# plt.plot(xpoints, ypoints, 'o')
# plt.show()
# from matplotlib import pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4])
# y=np.array([10,12,15,16])
# plt.plot(x,y,"o")
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()
# if you want to give the same color
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'b')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r', marker = 'o', ms = 20, mfc = 'b',mec="r",linestyle="--",linewidth=20.5)
# # plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()
# position of title -----------
# import numpy as np
# import matplotlib.pyplot as plt
# x= np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y= np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse",loc="right")
# plt.ylabel("Calorie Burnage")
# plt.plot(x,y)
# plt.grid()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# x= np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid(color = 'green', linestyle = '--', linewidth = 5.5)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()
# import numpy as np
# from matplotlib import pyplot as plt
# x=np.array(["a","b","c"])
# y=np.array([10,12,14])
# plt.bar(x,y,width=0.7,color="hotpink")
# plt.show()
# -----------------------------------------------------
# import numpy as np
# from matplotlib import pyplot as plt
# y=np.array([12,24,36])
# mylables=["a","b","c"]
# plt.pie(y,labels=mylables)
# plt.show()
# --------------------------------------------------for playing sound
# from playsound import playsound
# playsound("C:\\Users\karan\\OneDrive\\Desktop\\python\\play.mp3")
# ------------------------------------------------------

# a=input("enter the first number :")
# b=input("enter the second  number :")
# a=int(a)
# b=int(b)
# avg=(a+b)/2
# print( "the average of number is",avg)
# -------------------------------------------------------
# a=input("enter your name")
# print("good afternoon ",a)
# -------------------------------------------------------------------
# l='''hello MR Name I thing you doing well today how can I help you
# today is Date'''
# name=input(" Plese Enter your Name\n")
# date=(input("enter today date in dd/mm/yyyy formate\n"))
# l=l.replace("Name",name)
# l=l.replace("Date",date)
# print(l)
# def sum():
#     a=input("enter the first number\n")
#     b=input("enter the second number\n")
#     a=int(a)
#     b=int(b)
#     sum=a+b
#     print(sum)
# sum()
# --------------------------------------------------
# l1=[3,2,7,4,5]
# # l=l1.sort()
# # print(l)
# l1.sort()
# print(l1)
# l1.append(4)
# print(l1)
# ----------------------------------lenght is two-2
# l={20,20.0,"20"}
# print(len(l))
# print(l)
# l={}
# ----------------------------------------
# l=[]
# l=()
# l=set()
# print(type(l))
# l=[12,[1,2],(2,3),{1,2},{"karan":"good"}]
# g={1,(1,2)}
# g={1,(1,2),{"karan":"good"}}
# print(g)
# sub1=int(input("enter the first number\n"))
# sub2=int(input("enter the second  number\n"))
# sub3=int(input("enter the third number\n"))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail becaue you have less then 33 marks in 1 subject")
# elif(sub1+sub2+sub3)/3<40:
#     print("you fail because overall percentage is less then 40 ")
# else:
#     print("conguralation you are pass")
# leng=input("enter your name \n")
# if len(leng)<10:
#     print("lenght of name is less then 10")
# else:
#     print("length of name is greter then 10")
# l="karan is good boy"
# if "karan" in l:
#     print("karan is presnt")
# else:
#     print("karan is not preset")
# -----------------------------------------------------
# num=int(input("enter the number\n"))
# for i in range(1,11):
#     # print(str(num)+"x"+str(i)+"=",num*i)
#     print(f"{num}X{i}={num*i}")
# ----------------------------------------------------------------
# l1=["karan","mohan","sohan","rohan","sunil"]
# for name in l1:
#     if name.startswith("s"):
#         print(name)
#     if name.endswith("n"):
#         print("hello"+name)
# -----------------------------------------------------------------------for prime number
# num=int(input("enter the number\n"))
# for i in range (2,num):
#     if(num%i==0):
#         t=False
#     else:
#         t=True
# if t==True:
#     print("number is prime")
# elif t==False:
#     print("number is not prime")
# ----------------------------------------------------------------------
# ---------------------------------------------fraction of number by for loop

# -----------------------------------------------------------------factorial of a number
# num=int(input("enter the number\n"))
# fact=1
# for i in range (1,num+1):
#     fact=fact*i
#     print(fact)
# print(fact)
# n=5
# for i in range (n):
#     print("*"*(i+1))
# n=3
# for i in range(n):
#     print(" " *(n-i-1),end="")
#     print("*" *(2*i+1),end="")
#     print(" " *(n-i-1))

# -------------------------------------------------------functions
# print('''what you want frist enter
# for average write avg()
# for sum enter the sum()''')

# p=0
# x=int(input("enter the total number you want to insert\n"))
# for i in range (x):
#     a=int(input("enter the number"))
#     p=p+a
# print("sum of your all entered number is ",p)

# --------------------------------------------------------------------------
# def greet (name):
#     print("good day "+ name)

# greet("harry")
# ---------------------------------------------------------------
# def my_sum(num1,num2):
#     return num1+num2

# s=my_sum(2,5)
# print(s)
# ------------------------------------------------------------
# data=input('''what you want
# for sum press 1
# for substration press 2
# for multiplication press 3
# for substration press four\n''')

# def add_n():
#     l=[]
#     i=2
#     while i>1:
#         n=int(input("enter the number"))
#         wy=l.append(n)
#         wx=sum(l)
#         print("sum is ",wx)
#         print("l is now",l)
# if data==1:
#     add_n()
# if data==2:
#     subs()
# if data==3:
#     multi()
# if data==4:
#     div()
# add_n()
# n=int(input("Enter the total numbers you want to check\n"))
# for i in range(n):
#     l=[]
#     a=int(input("enter the numbers "))
#     l.append(a)
#     l.sort()
#     print(l)
# l.reverse()
# print(l)
# l=[12,11,15]
# l.append(16)
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# j=["apple","banana","mango"]
# for i in j:
#     l=[]
#     l.append(i)

# print(l)
# -----------------------------------------------------------gretest of three number
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# num3=int(input("enter the third number"))
# def great(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             print(f"{num1} is greates ")
#         else:
#             print(f"{num3} is greatest ")
#     else:
#         print(f"{num2} is greates ")

# great(num1,num2,num3)
# ---------------------------------------------------------------------------
# num=int(input("enter the celicuse value"))
# b=((num*9)/5)+32
# print(b)
# --------------------------------------------------------conversion of celicus to foraneheight
# n=3
# for i in range(n):
#     print("*"*(n-i))

# -----------------------------------------------------------------------------------game
# for i in range(3):
#         print("computers turn  he choose snake(s),gun(g),water(w)")
#         rand = random.randint(1, 3)
#         if rand == 1:
#             comp = "s"
#         elif rand == 2:
#             comp = "g"
#         elif rand == 3:
#             comp = "w"
#         man = input("your turn choose one snake(s),gun(g),water(w)\n")

#         def game_win(comp, man):
#             if comp == man:
#                 return 1
#             if comp == "s":
#                 if man == "w":
#                     return False
#                 elif man == "g":
#                     return True
#             if comp == "w":
#                 if man == "g":
#                     return False
#                 elif man == "s":
#                     return True
#             if comp == "g":
#                 if man == "s":
#                     return False
#                 elif man == "w":
#                     return True
#         print(f"computer choose {comp}")
#         print(f"you choose {man}")
#         a = game_win(comp, man)
#         if a == 1:
#             pass
#             # print("game is tie")
#         elif a == True:
#             j=a.count(True)
#             # print("you win")
#         else:
#             k=a.count(False)
#             # print("you loos")
# if j>k:
#      print(f"you win  by {j} and computer point {k}")
# elif k>j:
#      print(f"you loos the game your point{j} and computer point{k}")
# elif k==j:
#      print(f"game is tie both have equal point{j}")

# ------------------------------------------------------------------------------------------------
# f=open("karansingh.txt","w")
# f.write("karan is good boy")
# f.close()

# ----------------------------------------------------------------------
# def game():
#     return 59
# with open("highscore.txt") as f:
#     data=int(f.read())
# a=game()
# if a>data:
#     with open("highscore.txt","w") as f:
#         f.write(str(a))
# -------------------------------------------------------------------------------------read and write function in python
# def game():
#     return 558
# a=game()
# with open("highscore.txt") as f :
#     data=f.read()
# if data=="":
#     with open("highscore.txt","w") as f:
#         f.write(str(a))
# elif int(data)<a:
#     with open("highscore.txt","w") as f:
#         f.write(str(a))
# -------------------------------------------------------------------------------------------file handling
# words=["kaddu","pagle","kutte"]
# with open("sample.txt") as f:
#     l=f.read()
# for word in words:
#         l=l.replace(word,"@%###&%")
#         with open("sample.txt","w") as f:
#             f.write(l)
# -------------------------------------------------------------------------------------------------------
# content=True
# i=1
# with open("sample.txt") as f:
#     while content:
#         content=f.readline()
#         if "python" in content.lower():
#             print(content)
#             print(f"yes python is present in line number{i}")
#         i=i+1

# n=5
# for i in range(5):
#     with open("sample.txt") as f:
#         b=f.readline()
#         print(b)
# i=1
# d= True
# while d:
#     with open("sample.txt") as f:
#         d=f.readline()
#         print(d)
#     i=i+1
# ----------------------------------------------------------------------copy the content and open in new file

# with open("sample.txt") as f:
#     d=f.read()
# with open("sis.txt","w") as f:
#     f.write(d)
# ---------------------------------------------------------------
# g="karan singh"
# with open("check.txt","w") as f:
#     f.write(g)
# ------------------------------------------------------------------identical file
# f1="sample.txt"
# f2="sis.txt"
# with open(f1) as f:
#     f1=f.read()
# with open(f2) as f:
#     f2=f.read()

# if f1==f2:
#     print("file are identical")
# if f1!=f2:
#     print("file are not identical")
# --------------------------------------------------------------------------delete cotent of file
# with open("sample.txt","w") as f:
#     f.write("")
# _______________________________________________________________________________________________
# ---------------------------------------------------------------------rename of file
# import os
# f1="sample.txt"
# f2="new file.txt"
# with open(f1) as f :
#     f1=f.read()
# with open(f2,"w") as f:
#     f2=f.write(f1)
# os.remove(f1)
# ---------------------------------------------------------------------------------------------------------
# l=[]
# data1=int(input('''enter the total number\n'''))
# for i in range(data1):
#     num=int(input("enter the number\n"))
#     l.append(num)
# data2=int(input(''' what you want
# 1.for sum press one
# 2.for average press 2
# 3.for multiplaction press 3
# 4.for sort press 4
# 5.for maximum press 5
# 6.for minimum press 6\n'''))
# if data2==1:
#     print("sum of numbers is ",sum(l))
# elif data2==2:
#     d=(sum(l))/data1
#     print("average of number is ",d)
# elif data2==3:
#     mul=1
#     for i in range(data1):
#         mul=mul*l[i]
#     print("multiplication of number is ",mul)
# elif data2==4:
#     l.sort()
#     print(l)
# elif data2==5:
#     d=max(l)
#     print(d)
# elif data2==6:
#     d=min(l)
#     print(d)

# ------------------------------------------------------------------------------
# l=[2,3,4,5]
# multiple=1
# for i in range(4):
#     multiple=multiple*l[i]
# print(multiple)
# l=[]
# while True:
#     d=int(input("enter the number\n"))
#     l.append(d)
#     if d==0:
#         break
# print("sum of numbers is",sum(l))
# x = ['ab', 'cd']
# for i in x:
#     x.append(i.upper())
# print(x)
# i = 1
# while True:
#     if i%0O7 == 0:
#         break
#     print(i)
#     i += 1
# i = 5
# while True:
#     if i%0O05 == 0:
#         break
#     print(i)
#     i += 1
# i = 5
# while True:
#     if i%0111 == 0:
#         break
#     print(i)
#     i += 1
# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)
    # i += 2
# --------------------------------GIV3E AN ERROR
# True = False
# while True:
#     print(True)
#     break
# D=float("12+25")
# D=float("INF")
# print(D)
# d=float("23"+"12")
# print(d)
# def kar():
#     print("karan")
# kar
# kar()
# --------------------------------------for printing the skyvalue of the alphabed
# print(ord("b")-ord("a"))
# import pandas as pd
# chlorie={"karan":"happy","singh":"sir name"}
# myvar=pd.Series(chlorie)
# print(myvar)
# import pandas as pd
# ko={"name":["karan","mohan","sohan"],"marks":[25,25,26]}
# myvar=pd.DataFrame(ko)
# print(myvar)
# import pandas as pd
# calories={"karan":"name","day":"monday"}
# myvar=pd.Series(calories)
# print(myvar)
# with open("new file.txt") as f:
#     while True:
#         content=f.readline()
#         print(content)
# i=1
# while True:
#     with open("sample.txt") as f:
#         d=f.readline()
#         print(d)
#         i=i+1
# l=[]
# d=int(input("how much number you want to enter \n"))
# for i in range (d):
#     c=int(input('enter the number \n'))
#     l.append(c)
# x=int(input('''for sum press 1
# for multiplaction press 2
# for maximum press 3
# for minimum press 4
# for average press 5\n'''))
# mul=1
# if x==1:
#     d=sum(l)
#     print(d)
# elif x==2:
#     for i in range(d):
#         mul=mul*l[i]
#     print("multpipaction  of mumer is",mul)
# elif x==3:
#     d=max(l)
#     print(d)
# elif x==4:
#     print(min(l))
# elif x==5:
#     avg=sum(l)/d
#     print(avg)
# -----------------------------------------------------multiplaction of numbers
# l=[]
# mul=1
# while True:
#     x=int(input("enter the number\n"))
#     l.append(x)
#     if x==1:
#         break
# for i in range(len(l)):
#     mul=mul*l[i]
# print("multiplication of number is ",mul)
# --------------------------------------------------------------------------------cut paste method

# with open("sample.txt") as f:
#     d=f.read()
# with open ("karan.txt","w") as f:
#     f.write(d)
# with open("sample.txt","w") as f:
#     f.write("")
# --------------------------------------------------------------------------------------------------
# import random
# l=[]
# d=int(input("enter total number of round you want to play\n"))
# for i in range(d):
#         print("computers turn  he choose snake(s),gun(g),water(w)")
#         rand = random.randint(1, 3)
#         if rand == 1:
#             comp = "s"
#         elif rand == 2:
#             comp = "g"
#         elif rand == 3:
#             comp = "w"
#         man = input("your turn choose one snake(s),gun(g),water(w)\n")

#         def game_win(comp,man):
#             if comp == man:
#                 return None
#             elif comp == "s":
#                 if man == "w":
#                     return False
#                 elif man == "g":
#                     return True
#             elif comp == "w":
#                 if man == "g":
#                     return False
#                 elif man == "s":
#                     return True
#             elif comp == "g":
#                 if man == "s":
#                     return False
#                 elif man == "w":
#                     return True
#         print(f"computer choose {comp}")
#         print(f"you choose {man}")
#         a = game_win(comp,man)
#         if a==True:
#             l.append("man")
#         elif a==False:
#             l.append("comp")
#         elif a == None:
#             l.append("tie")
# d=l.count("man")
# # print(d)
# e=l.count("comp")
# g=l.count("tie")
# # print(e)
# if d>e:
#     print(f"you win and your point {d} computer point {e} and tie {g}")
# elif e>d:
#     print(f"you loos your point {d} computer point {e} and tie {g}")
# else:
#     print(f"game is tie number of time its tie {g}")
# print(l)
# ---------------------------------------------------------------------------------------------------sorting algorithm
# l=[]
# while True:
#     q=int(input('''
#     1.for data entery press one 
#     2. for sort press two 
#     3.for get first element press 3
#     4. for get last element press 4 
#     5.for pop operation press 5
#     6. for removing dublicate\n'''))
#     if q==1:
       
#         while True:
#             d = input("enter your data\n")
#             l.append(d)
#             if d == "f":
#                 l.pop()
#                 break
#             print(l)
#     elif q==2:
#         l.sort()
#         print(l)
#     elif q==3:
#         print(l[0])
#     elif q==4:
#         print(l[-1])
#     elif q==5:
#         print(l)
#         p=int(input("enter total element you want to pop\n"))
#         for i in range(p):
#             l.pop()
#         print(l)
#     elif q==6:
#         d=set(l)
#         f=list(d)
#         print(f)
# ------------------------------------------------------------------------------------------------------------
# arr=np.arry([1.1,2.1,3.1])
# new_arr=arr.astype('i')
# print(new_arr)
# l=[]
# mul=1
# while True:
#     p=int(input("enter the number you want to multiply\n"))
#     l.append(p)
#     print(l)
#     if p==1:
#         d=l.pop()
#         break
# c=len(l)

# for i in range(c):
#     mul=mul*l[i]
# print("multlpiaction of number is \n",mul)
        # -------------------------------------------------unpacking of variable
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# ------------------------------------------global variable
# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()

# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# myfunc()
# print("Python is " + x)

# in case of function after defining function inside the fuctinon we can not use it outside untile we not make this golbal
# in this case we can not use value of a,b outside the function for use this first make the variable golbal then use it 
# def add():
#     a=3
#     b=4
# print(a+b)


# in this case we can use the value of x outside the fuction after making global them inside the fuction
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)

# Check if "free" is present in the following text:
# txt = "The best things in life are free!"
# print("free" in txt)
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# The strip() method removes any whitespace from the beginning or the end:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
# a = "Hello, World!"
# print(a.replace("H", "J"))
# The split() method splits the string into substrings if it finds instances of the separator:
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# x=("apple","cherry")
# y=list(x)
# y[1]="mango"
# x=tuple(y)
# print(x)
# d=int(input("enter the number\n"))
# e=int(input("enter the number\n"))
# if d==e:
#     print("both are equal")
# if d>e:
#     print("d is gerater the e ")
# else:
#     print("d is less then e") 

# ---------------------------------------------------------------/
# One line if else statement:
# a = 2
# b = 330
# print("A") if a > b else print("B")
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")
# ---------------------in case of contiune statement if continue command is implement then afer continue what ever written is scape and command goes to while loop again
# i=0
# while i<6:
#     i=i+1
#     if i==3:
#         continue
#     print(i)
#     print("hello")
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# print(f"{i} is no loner then 6")
# in case of for loop if we use the for loop with break statement then else block code is not execute
# The else block will NOT be executed if the loop is stopped by a break statement.
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")
# when we dont known how many argument have to pass then we use the * symbol 
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")
# if you not want to follow the sequence then you can use this
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# default case in python function cheapter
# def myfunction(country="agra"):
#     print("my country is ",country)

# myfunction("allahabad")
# myfunction()

# def fruits(food):
#     for i in food:
#         print(i)
# fruit=["apple","banana","mango"]
# fruits(fruit)
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.