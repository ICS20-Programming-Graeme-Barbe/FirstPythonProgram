import math

side_a = float(input("Enter side A length: "))
side_b = float(input("Enter side B length: "))
calc = side_a ** 2 + side_b ** 2
square_root = math.sqrt(calc)
rounded = round(square_root, 2)

print("C side is equal to ", rounded)23