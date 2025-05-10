try:
    a=int(input("enter your number "))
    if a>10:
        print("{} is greater then ten".format(a))
except ValueError as q:
    print("exception is",q)