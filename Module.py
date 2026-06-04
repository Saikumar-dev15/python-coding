#module = a file containing code you want to include i n your program
#          use 'import' to include a module (built-in or your own )
#          useful to break up large program reusable separate files

#print(help("modules"))

#import math
# import math as m
from math import e
a,b,c,d, e = 1,2,3,4,5
#print(e ** a)
#print(e ** b)
#print(e ** c)
#print(e ** d)
#print(e ** a)

#we can import our file from different py.file is called mudule

#variable scope = where a variables is visible and accesible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


a=100
b=200

def func1():
    a = 1
    #print(b)

def func2():
    b = 2
   # print(a)

func1()
func2()

#def func3():
    #x=2
    #print(x)
#def func4():
    #x=6                     #local
    #print(x)
    
#x=3                          #global
#func3()
#func4()




#if __name__ == __main__: (this script can be imported or run standalone)
#                          functions and classes in this module can be reused without the main block of code executing
#                          helps readability, leaves no global variables,  avoid unintended execution.

#ex.library = Import library for functionality
#             when running library directly, display a help page

#print(dir())



#def favourite_food(food):
#    print(f"your favourite is {food} ")

#def main():
#    print("this is script")
 #   favourite_food("Pizza")
#    print("GoodBye!....")
    
#if __name__ ==  '__main__':
#    main()
          

