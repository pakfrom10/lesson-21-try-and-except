try:
    a,b=eval(input("enter two numbers seperated by coma "))
    result=a/b 
    print("{} divided by {} equals to {}".format(a,b,result))
except ValueError as q:
    print("exception is",q)
except ZeroDivisionError as g:
    print(" exception is ",g)
except SyntaxError as s:
    print("excepton is ",s)