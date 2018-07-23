import sys
try:
    year = int(sys.argv[1])
    if year % 400 == 0:
        print(year, end = "") 
        print(" is leap year!")
    else:
        if year % 100 == 0:
            print(year, end = "")
            print(" is not leap year.")
        else:
            if year % 4 ==0:
                print(year, end = "") 
                print(" is leap year!")
            else:
                print(year, end = "") 
                print(" is not leap year.")
except:
    print("This argument can not be converted to integer.")
    