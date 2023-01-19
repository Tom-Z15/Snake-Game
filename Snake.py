import pygame
import random
import sys
import os

win = pygame.display.set_mode((500, 500))

run = True
x = 240
y = 240
x_point = random.randint(0, 500)
y_point = random.randint(50, 500)
radius = 3
vel = 5
direction = "right"
points = 0
point_active = False
hitbox_snake = 0
hitbox_point = 0
hitbox_snake_2 = pygame.draw.rect(win, (0,0,0), pygame.Rect(10, 10, 6, 6))
index = 0

#Cords
cords_x = []
cords_y = []

#text
pygame.init()






#Window name
pygame.display.set_caption('Snake')

def draw ():
    global hitbox_snake
    global hitbox_snake_2
    global hitbox_point
    global index
    global cords
    
    
    hitbox_snake = pygame.draw.rect(win, (255,0,0), pygame.Rect(x - 3, y - 3, 6, 6))
    hitbox_point = pygame.draw.rect(win, (255,0,0), pygame.Rect(x_point - 3, y_point - 3, 6, 6))
    
        
    
    win.fill((0, 0, 0))
    
    pygame.draw.line(win, (255, 0, 0), (0, 50), (500, 50), 1)    
    
    pygame.draw.rect(win, (255,0,0), pygame.Rect(x - 3, y - 3, 6, 6))
    pygame.draw.rect(win, (255,0,0), pygame.Rect(x_point - 3, y_point - 3, 6, 6))  
    pygame.draw.circle(win, (255,255,255), (int(x), int(y)), radius)
    cords_x.append (x)
    cords_y.append(y)


    
    if point_active == True:
        pass
    else:
        pygame.draw.circle(win, (255,0,0), (int(x_point), int(y_point)), radius)
        

    for i in range(points):
        index = len(cords_x) - (i + 2)
        
        hitbox_snake_2 = pygame.draw.rect(win, (0,0,0), pygame.Rect(cords_x[index -1 ], cords_y[index -1], 3, 3))
        pygame.draw.circle(win, (255,0,0), ( cords_x[index], cords_y[index]), radius)
    


def logic():
    global points
    global point_active
    global x_point
    global y_point
    collide = hitbox_snake.colliderect(hitbox_point)
    collide_tail = hitbox_snake_2.colliderect(hitbox_snake)
    
    if collide:
        x_point = random.randint(0, 500)
        y_point = random.randint(50, 500)
        
        point_active = True
        points += 1
        pygame.draw.circle(win, (255,0,0), (int(x_point), int(y_point)), radius)

    if collide_tail:
        pygame.quit()
   
    
    
    if x >= 500: 
        pygame.quit()

    if x <= 0: 
        pygame.quit()
        

    if y <= 50:
        pygame.quit()
    
    if y >= 500:
        pygame.quit()
        

        
        


    
def move():

    global x
    global y
    global direction
    
    user_input = pygame.key.get_pressed()

    if user_input [pygame.K_LEFT]:
        if direction != "left":
            direction = "right"

    if user_input [pygame.K_RIGHT]:
        if direction != "right":
            direction = "left"
    
    if user_input [pygame.K_UP]:
        if direction != "down":
            direction = "up"

    if user_input [pygame.K_DOWN]:
        if direction != "up":
            direction = "down"


    match direction:
        case "right":
            x -= vel
        case "left":
            x += vel
        case "up":
            y -= vel
        case "down":
            y += vel





while run:
    font = pygame.font.SysFont("Arial", 50)

    text_score = font.render(str(points), True, (255,0,0))

    textRect = text_score.get_rect()
    textRect.center = (500 // 2, 25)
    
    move()
    draw()
    logic()

    win.blit(text_score, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.time.delay(100)

    pygame.display.update()






