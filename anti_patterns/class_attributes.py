class Rectangle:
    width = 0   # ❌ Class variable (shared by all instances)
    height = 0  # ❌ Class variable (shared by all instances)

# Create two rectangles
rect1 = Rectangle()
Rectangle.width = 5
Rectangle.height = 30

rect2 = Rectangle()

print(rect1.width, rect1.height)
print(rect2.width, rect2.height)
