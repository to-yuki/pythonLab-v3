import sys
from Employees import empSearch

#-- Main-Satrt --#
def main():
    try:
        no = sys.argv[1]

        name,tell = empSearch(no)

        print("Employee Name: ",name)
        print("Employee Tell: ",tell)
    except:
        print("Input Error")

#-- Main-End --#

if __name__ == "__main__":
    main()
