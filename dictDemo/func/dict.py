def mergeName(firstname,lastname):
    full_name = firstname + ' '+lastname
    return  full_name
while True:
    print("please input your name!")
    first = input("firstname:")
    last = input("lastname:")
    full = mergeName(first,last)
    print(full)