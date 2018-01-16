Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /home/cs2017a117/Joshua/myfirst.py ================
My name is Joshua
>>> print("CMR University")
CMR University
>>> print(Cmru)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(Cmru)
NameError: name 'Cmru' is not defined
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(float x)
SyntaxError: invalid syntax
>>> print("Python Programmming Language")
Python Programmming Language
>>> a=6
>>> b=10
>>> print(a+b)
16
>>> 5+6
11
>>> random(3,4,5,6,9)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    random(3,4,5,6,9)
NameError: name 'random' is not defined
>>> a=100
>>> b=300
>>> c=a+b
>>> print c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?
>>> print(c)
400
>>> a=2000
>>> b=999
>>> c=a*b
>>> print(c)
1998000
>>> a=90
>>> b=20
>>> c=a/b
>>> print(c)
4.5
>>> timeit.timeit(stmt=s, number=100000)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    timeit.timeit(stmt=s, number=100000)
NameError: name 'timeit' is not defined
>>> a=90
>>> b=20
>>> c=a+b
>>> print("Addition of" a "+" b "="c)
SyntaxError: invalid syntax
>>> print("Addition of" ,a "+" ,b "=" ,c)
SyntaxError: invalid syntax
>>> print("Addition of" ,a, "+" ,b, "=" ,c)
Addition of 90 + 20 = 110
>>> a=6
>>> b=90
>>> print("Multiplication of" ,a, "and" ,b, "=" ,a*b)
Multiplication of 6 and 90 = 540
>>> a=str(input("Enter a string"))
Enter a string
>>> dfh
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dfh
NameError: name 'dfh' is not defined
>>> a=str(input("Enter a string"))
Enter a string hf
>>> a=str(input("Enter a string"))
Enter a string hj
>>> b=str(input("Enter a string"))
Enter a string vg
>>> c=a+b
>>> print(c)
 hj vg
>>> d=a*b
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d=a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> e=a-b
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    e=a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
