try:
   num1,num2=eval(input("enter two numbers,separated:"))
   result=num1/num2
   print("result is",result)
except(ZeroDivisionError,syntaxerror) as e:
   print("Inside ZeroDivisionError,syntaxerror",e)
except:
   print("wrong input")
else:
   print("no exception")
finally:
   print("done")
