import sys
from Employees import empSearch

#-- Main-Satrt --#
def main():
    try:
        no = sys.argv[1]

        name,tel = empSearch(no)

        print("Employee Name: ",name)
        print("Employee Tel: ",tel)
    except:
        print("Input Error")

#-- Main-End --#

if __name__ == "__main__":
    main()
