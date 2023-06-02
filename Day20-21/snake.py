from turtle import Turtle
# best score: 68

class Snake():
    def __init__(self):
        self.key = "d"
        self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in self.starting_positions:
            self.addSegment(position)
        self.head = self.segments[0]
    
    def createSnake(self):
        for position in self.starting_positions:
            self.addSegment(position)
        self.head = self.segments[0]
            
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def resetSnake(self):
        self.key = "d"
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    def addSegment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.addSegment(self.segments[-1].pos())
    
    def w(self):
        if self.key == "d":
            self.segments[0].left(90)
            self.key = "w"
        elif self.key == "a":
            self.segments[0].right(90)
            self.key = "w"
    def s(self):
        if self.key == "a":
            self.segments[0].left(90)
            self.key = "s"
        elif self.key == "d":
            self.segments[0].right(90)
            self.key = "s"
    def a(self):
        if self.key == "w":
            self.segments[0].left(90)
            self.key = "a"
        elif self.key == "s":
            self.segments[0].right(90)
            self.key = "a"
    def d(self):
        if self.key == "s":
            self.segments[0].left(90)
            self.key = "d"
        elif self.key == "w":
            self.segments[0].right(90)
            self.key = "d"