import turtle
import random

# Khởi tạo Turtle
t = turtle.Turtle()
t.speed(0)  # Đặt tốc độ về mức tối đa

# Mảng màu sắc cho pháo hoa
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Hàm vẽ pháo hoa
def draw_firework(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))

    # Vẽ cảnh hoa pháo hoa
    for _ in range(36):
        t.forward(100)
        t.right(170)

    # Vẽ vòng tròn nhỏ giữa cảnh hoa
    t.right(10)
    t.circle(10)

# Hàm vẽ nhiều pháo hoa
def draw_fireworks(num_fireworks):
    for _ in range(num_fireworks):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        draw_firework(x, y)

# Tắt hiển thị đường vẽ của Turtle
turtle.hideturtle()

# Vẽ nhiều pháo hoa
draw_fireworks(5)

# Đóng cửa sổ khi nhấp chuột
turtle.exitonclick()
