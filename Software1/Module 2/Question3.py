length_str = input("Enter the length of the rectangle: ")
length = float(length_str)
width_str = input("Enter the width of the rectangle: ")
width = float(width_str)
perimeter = width * 2 + length * 2
area = width * length
print(f'The perimeter of the rectangle is {perimeter:.1f}')
print(f'The area of the rectangle is {area}')