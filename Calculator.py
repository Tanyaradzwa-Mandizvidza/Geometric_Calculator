import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

# Input from the user
try:
    print("Choose a shape to calculate:")
    print("1. Rectangle")
    print("2. Circle")
    
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: ")
        
        # Calculate the area and perimeter of the rectangle
        area = calculate_rectangle_area(length, width)
        perimeter = calculate_rectangle_perimeter(length, width)
        
        print(f"The area of the rectangle is: {area}")
        print(f"The perimeter of the rectangle is: {perimeter}")
        
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        
        # Calculate the area and circumference of the circle
        area = calculate_circle_area(radius)
        circumference = calculate_circle_circumference(radius)
        
        print(f"The area of the circle is: {area}")
        print(f"The circumference of the circle is: {circumference}")
    
    else:
        print("Invalid choice. Please enter 1 for Rectangle or 2 for Circle.")
        
except ValueError:
    print("Please enter valid numerical values for calculations.")
