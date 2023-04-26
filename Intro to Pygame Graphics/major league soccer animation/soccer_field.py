import pygame
import math
from constants import *

def display_field(field_color, stripe_color):
    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)
    
    '''fence'''
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x+2, y], [x+2, y+15], [x, y+15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y+15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x+800, y], 1)


def display_goal_lines():
    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2*math.pi, 5)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

def display_goal_box():
    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    #net
    #the biggest part of the net is split into 3 sections. We know this beccause as we continue to inspect the code, there is a pattern in the x values.  
    #the patterns are visible with x increasing by 5, then 4, then 5 again. So, given that there are 3 patterns, we split the middle net into 3 parts. 

    #center net 1/3
    temp = 341
    for x in range(325, 365, 5):
        pygame.draw.line(screen, WHITE, [x, 140], [temp, 200], 1)
        temp = temp+3

    #center net 2/3 
    temp = 364
    for x in range(364, 439, 4):
        pygame.draw.line(screen, WHITE, [x, 140], [temp, 200], 1)
        temp = temp+4

    #center net 3/3
    temp = 438    
    for x in range(440, 480, 5):
        pygame.draw.line(screen, WHITE, [x, 140], [temp, 200], 1)
        temp = temp+3


    #net part 2
    #this takes care of the left side of the net. it follows the same arithmetics as the above code. 
    
    temp = 216
    for x in range (324, 340, 2):
        pygame.draw.line(screen, WHITE, [320, 140], [x, temp], 1)
        temp = temp-2

    #net part 3
    temp = 216
    for x in range(476, 461, -2):
        pygame.draw.line(screen, WHITE, [480, 140], [x, temp], 1)
        temp = temp-2

    #net part 4 1/2
    #we also split this portion of the net into patterns. we notice that the inital x's are different. 
    temp = 144
    for x in range(144, 178, 4):
        pygame.draw.line(screen, WHITE, [324, temp], [476, x], 1)
        temp = temp+4

    #net part 4 2/2
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    temp = 184
    for x in range(184, 198, 4):
        pygame.draw.line(screen, WHITE, [335, temp], [465, x], 1)
        temp = temp+4
        
    #net is finished! 
