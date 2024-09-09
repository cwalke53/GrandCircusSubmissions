import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
    def calculate_diameter(self):
        diameter = self.radius * 2
        return diameter

    def calculate_circumference(self):
        circumference = 2.0 * math.pi * self.radius
        return circumference

    def calculate_area(self):
        area = math.pi * float(self.radius ** 2)
        return area
    def grow(self):
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius

def user_Circle():
    circle = Circle(float(input("Enter a radius(number with decimals): ")))
    while True:
        # if user_input != float:
        #     print("Invalid data. try again")
        #     continue
        # elif user_input == float:
        #     break
        print(f"Diameter: {circle.calculate_diameter()}")
        print(f"Circumference: {circle.calculate_circumference()}")
        print(f"Area: {circle.calculate_area()}")

        grow_the_circle = input("Grow the circle? (y/n): ")

        if grow_the_circle == "y":
            circle.grow()
        else:
            print("Goodbye")
            break
user_Circle()

# print(full_circle.calculate_diameter())
# print(full_circle.calculate_circumference())

