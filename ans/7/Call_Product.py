from Product import Product
import sys

def main():
    p = Product()
    p.setValue(sys.argv[1], sys.argv[2], sys.argv[3])
    p.display()

if __name__ == "__main__":
    main()