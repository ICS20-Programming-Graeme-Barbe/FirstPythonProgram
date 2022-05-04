# This is a pythagorean theorem calculator

import math

side_selector = input("Select side: ")

side_selector = side_selector.upper()


if side_selector == "" and side_selector != "A" and side_selector != "B" and side_selector != "C":
	print("You need to select what side you are trying to find.")
	side_selector = input("Select side: ")
	side_selector = side_selector.upper
elif side_selector == "A":
	side_b = float(input("Enter side B length: "))
	side_c = float(input("Enter side C length: "))
	units = input("Choose units:" )
	calc = math.sqrt(side_c ** 2 - side_b ** 2)
	rounded = round(calc, 2)
	print("Side A is equal to ", rounded, units + "²")
elif side_selector == "B":
	side_a = float(input("Enter side A length: "))
	side_c = float(input("Enter side C length: "))
	calc = math.sqrt(side_c ** 2 - side_a ** 2)
	rounded = round(calc, 2)
	print("Side B is equal to ", rounded)
elif side_selector == "C":
	side_a = float(input("Enter side A length: "))
	side_b = float(input("Enter side B length: "))
	calc = math.sqrt(side_a ** 2 + side_b ** 2)
	rounded = round(calc, 2)
	print("Side C is equal to ", rounded)
else:
	print("Please choose between side A, B and C")
