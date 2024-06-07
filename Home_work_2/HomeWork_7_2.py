#You are given four real numbers - the coordinates of two points on a
#plane. The first two numbers are the x and y coordinates of the first point,
#and the last two numbers are the x and y coordinates of the second point.
#Output the length of the line segment bounded by the two points.


x_1 = float(input("input x1 coordinates "))
y_1 = float(input("input y1 coordinates "))
x_2 = float(input("input x2 coordinates "))
y_2 = float(input("input y2 coordinates "))

z_1 = complex(x_1, y_1)
z_2 = complex(x_2, y_2)

z_modul = abs(z_1 - z_2)

print(z_modul)