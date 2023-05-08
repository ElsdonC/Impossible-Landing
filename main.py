import turtle, random, math

class Game:
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 500, 500)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.delay(0)
        self.player = SpaceCraft(random.uniform(100,400), random.uniform(250,450), random.uniform(-4,4), random.uniform(-2,0))
        self.obstacles = []
        for i in range(10):
            self.obstacles.append(Obstacles(random.uniform(0,500), random.uniform(0,250)))
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')
        turtle.listen()
        turtle.mainloop()

    def explosion(self):
        explosion = turtle.Turtle()
        explosion.hideturtle()
        explosion.penup()
        explosion.speed(0)
        explosion.goto(self.player.xpos, self.player.ypos)
        explosion.dot(40, 'orange')
        explosion.dot(25, 'red')
        explosion.getscreen().delay(50)
        explosion.dot(60, 'orange')
        explosion.getscreen().delay(0)
        explosion.dot(50, 'red')
        explosion.getscreen().delay(50)
        explosion.dot(85, 'orange')
        explosion.getscreen().delay(0)
        explosion.dot(75, 'red')
        explosion.getscreen().delay(50)
        explosion.dot(120, 'orange')
        explosion.getscreen().delay(0)
        explosion.dot(100, 'red')

    def gameloop(self):
        playing = True
        self.player.move()
        for obstacle in self.obstacles:
            obstacle.move()
            if obstacle.ypos-30 <= self.player.ypos <= obstacle.ypos+30 and obstacle.xpos-30 <= self.player.xpos <= obstacle.xpos+30:
                self.explosion()
                turtle.goto(0,0)
                turtle.write("You crashed!", move=False, align='left', font=('Arial', 32, 'normal'))
                playing = False
        if (self.player.ypos >= 20 and playing):
            turtle.ontimer(self.gameloop, 0)
        else:
            if (playing):
                if (self.player.xvel > -3 and self.player.xvel < 3 and self.player.yvel > -3 and self.player.yvel < 3):
                    turtle.goto(0,0)
                    turtle.write("Successful Landing!", move=False, align='left', font=('Arial', 32, 'normal')) 
                else:
                    self.explosion()
                    turtle.goto(0,0)
                    turtle.write("You crashed!", move=False, align='left', font=('Arial', 32, 'normal')) 


class SpaceCraft(turtle.Turtle):
    def __init__(self, xpos, ypos, xvel, yvel):
        turtle.Turtle.__init__(self)
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.fuel = 40
        self.shapesize(5,5)
        self.left(40)
        self.penup()
        self.speed(0)
        self.goto(self.xpos, self.ypos)
        self.shape("turtle")
    def move(self):
        self.yvel = self.yvel-0.0486
        self.xpos = self.xcor() + self.xvel
        self.ypos = self.ycor() + self.yvel
        self.goto(self.xpos, self.ypos)
    def thrust(self):
        if (self.fuel > 0):
            self.fuel -= 1
            angle = math.radians(self.heading())
            cosine = math.cos(angle)
            sine = math.sin(angle)
            self.xvel += cosine
            self.yvel += sine
            if (self.fuel <= 0):
                print("Out of fuel")
            else:
                print(f"{self.fuel} fuel units remaining!")
        else:
            print("Out of fuel")
        print("Up button pressed")
    def left_turn(self):
        if (self.fuel <= 0):
            print("No fuel left!")
        else:
            self.left(15)
            self.fuel -= 1
            print(f"{self.fuel} fuel units remaining!")
        
    def right_turn(self):
        if (self.fuel <= 0):
            print("No fuel left!")
        else:   
            self.right(15)
            self.fuel -= 1
            print(f"{self.fuel} fuel units remaining!")

class Obstacles(turtle.Turtle):
    def __init__(self, xpos, ypos):
        turtle.Turtle.__init__(self)
        self.xpos = xpos
        self.ypos = ypos
        self.penup()
        self.goto(self.xpos, self.ypos)
    def move(self):
        self.speed(1)
        self.forward(20)
        self.xpos = self.xcor()
        self.ypos = self.ycor()
        self.right(45)

if __name__ == '__main__':
    Game()
