import math

def calculate_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def calculate_perimeter(side1, side2, side3):

    perimeter = side1 + side2 + side3
    return perimeter

def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

def main():
    print("Welcome to the Triangle Calculator!")
    print("Please enter the lengths of the triangle's sides.")

    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    area = calculate_area(side1, side2, side3)
    perimeter = calculate_perimeter(side1, side2, side3)
    triangle_type = classify_triangle(side1, side2, side3)

    print("Triangle Properties:")
    print(f"Area: {area:.2f} square units")
    print(f"Perimeter: {perimeter:.2f} units")
    print(f"Type: {triangle_type}")

if __name__ == "__main__":
    main()
