from Paddle import Paddle
from Ball import Ball


def setup():
    size(1200, 800)
    
    speed = 6
    
    global f, paddle_player1, paddle_player2, ball, player1_score, player2_score
    
    f = createFont("Arial", 16, True)
    ball = Ball(height / 2, width / 2, random(0, TWO_PI), speed)
    paddle_player2 = Paddle(height / 2, width - 50)
    paddle_player1 = Paddle(height / 2, 50)
    player1_score = 0
    player2_score = 0


def draw():
    background(0)
    
    global f, player1_score, player2_score
    
    paddle_len = 100
    ball_radius = 10
    

    if (ball.x >= width):
        player1_score += 1
        ball.reset()
        paddle_player1.reset()
    elif (ball.x <= 0):
        player2_score += 1
        ball.reset()
        paddle_player1.reset()
    
    
    textFont(f, 50)            
    fill(255)                       
    text(player1_score, width / 2 - 50, 60)
    text(player2_score, width / 2 + 50, 60)
    
    
    paddle_player1.show()
    paddle_player2.show()
    ball.show(ball_radius)
    ball.move() 
    ball.edges()
    ball.leftPaddle(paddle_player1)
    ball.rightPaddle(paddle_player2)
    
    
def keyPressed():
    speed = 30
    
    if (key == 'w'):
        paddle_player1.move(-speed)
        
    elif (key == 's'):
        paddle_player1.move(speed)
            
            
    if (key == 'o'):
        paddle_player2.move(-speed)
        
    elif (key == 'l'):
        paddle_player2.move(speed)
        
        
    if (key == 'r'):
        ball.reset()
        paddle_player1.reset()
        paddle_player2.reset()
