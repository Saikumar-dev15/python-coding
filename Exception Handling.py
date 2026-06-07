# execption = An event that interupts the flow of a program 
#             (ZeroDivisionError, TypeError , ValueError)
#             1.try , 2. Except , 3.finally

#When you entered an wrong data type it will considered as Type Error.
# 1+"1"      #here int and str are implemented

#when we entered a wrong type cast is called Value Error
#x=int("pizza")

try:
    number = int(input("Enter a number: "))
    print(2/number)
    
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!..")
    
except ValueError:
    print("Enter only numbers please!..")
    
except Exception:
    print("Something went wrong!")

finally:
    print("Do some cleanup here")
    

    
