import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.right(45)
    
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    
    t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
 
    level = int(screen.textinput("Pythagoras Tree", "Enter the level of recursion:"))
    
    draw_pythagoras_tree(t, 100, level)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
