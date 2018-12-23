class Ball (object):
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.xspeed = self.speed * cos(self.angle)
        self.yspeed = self.speed * sin(self.angle)
        
        
    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        
        
    def edges(self):
        if (self.y < 0 or self.y > height):
            self.yspeed *= -1

        
    def leftPaddle(self, paddle):
        if (self.x <= paddle.x + paddle.w and self.y >= paddle.y - 0.5 * paddle.h and self.y <= paddle.y + 0.5 * paddle.h):
            self.xspeed *= -1
            self.yspeed += random(-3, 3)
    
    
    def rightPaddle(self, paddle):
        if (self.x >= paddle.x - paddle.w and self.y >= paddle.y - 0.5 * paddle.h and self.y <= paddle.y + 0.5 * paddle.h):
            self.xspeed *= -1
            self.yspeed += random(-3, 3)
    
    def show(self, r):
        fill(255, 255, 255)
        ellipseMode(CENTER)
        ellipse(self.x, self.y, 2 * r, 2 * r)
        
        
    def reset(self):
        self.x = width / 2
        self.y = height / 2
        self.xspeed = self.speed * cos(random(0, TWO_PI))
        self.yspeed = self.speed * sin(random(0, TWO_PI))
