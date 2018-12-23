class Paddle (object):
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.vel = 0
        self.w = 25
        self.h = 100
    
    
    def move(self, vel):
        self.y += vel
    
    
    def show(self):
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)
    
    
    def reset(self):
        self.y = height / 2
