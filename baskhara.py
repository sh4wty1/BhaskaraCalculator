print("Bhaskara Calculator")
print("ax^2 + bx + c = 0")
a = float(input("Enter 'a' value: "))
b = float(input("Enter 'b' value: "))
c = float(input("Enter 'c' value: "))

delta = (b**2) - 4 * a * c

if a == 0:
    print("'a' value must be different from 0")
elif delta < 0:
    print("Complex number")
elif delta == 0:
    x = (-b) / (2 * a)
    print(f"x = {x}")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
