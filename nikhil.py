'''This calculater devloped by Nikhil Sikarwar'''
'''First year python project'''
def operation(x,y):
    if z=="1":
        add(x,y)
    elif z== "2":
        sub(x,y)
    elif z == "3":
        mult(x,y)
    elif z == "4":
        div(x,y)
def add(x,y):
    c = x + y 
    print(c)
def sub(x,y):
    c = x-y
    print(c)
def mult(x,y):
    c = x*y
    print(c)
def  div(x,y):
    c = x/y
    print(c)
n = 0
while n <= 1:
   x = int(input("enter first number : "))
   y = int(input("enter second number : "))
   print(""" 
          1.enter 1 for addition
          2.enter 2 for sub.
          3.enter 3 for multi.       
          4.enter 4 for div. """)
   z = str(input("\nselect operation want to perform : "))
   operation(x,y)
   n = n
 
