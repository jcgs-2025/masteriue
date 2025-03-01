from shapes import Triangle, Rectangle

def main():
    t = Triangle(10, 5)
    print(f"The area of triangle {t.description()} is {t.area()}")
    
    r = Rectangle(10, 5)
    print(f"The area of rectangle {r.description()} is {r.area()}")

    
if __name__ == '__main__':
    main()