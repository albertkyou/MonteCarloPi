# pypi is a Monte Carlo approximation of pi rendered in a pygame window
# the goal is to open a pygame window and plot a bunch of dots with various distributions
# Demo of how to approximate pi using a monte carlo simulation
# Albert You

# Concept:
# The area of a square with length 2 is 4
# The area of a unit circle is pi
# The probability of a point landing inside the circle is thus pi/4

import pygame
import numpy as np 
import time

pygame.init()

background_colour = (255,255,255) # white
(width, height) = (900, 1000)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Approximate Pi')
screen.fill(background_colour)

# Display the counter for dots inside the circle and outside the circle
font = pygame.font.Font("freesansbold.ttf", 32) 
insidetext = font.render('Dots inside circle: ', True, (255,0,0)) 
outsidetext = font.render('Dots outside circle: ', True, (0,0,255))
ratio = font.render('Ratio: ',True,(0,0,0))
screen.blit(insidetext,(200,50))
screen.blit(outsidetext,(200, 100))
screen.blit(ratio,(200,150))
# draw bounding square
pygame.draw.rect(screen,(0,0,0),(100,200,700,700),2)

# draw bounding rectangle
pygame.draw.circle(screen,(0,0,0),(450,550),350,1)

insidecounter = 0
outsidecounter = 0

# helper function to see if something is inside a circle
def incircle(x,y):
    # calculates if (x,y) is in the circle or not

    # x: [-1,1]
    # y: [-1,1]

    radius = np.sqrt(x**2+y**2)
    if radius <= 1:
        return True
    else:
        return False

# pygame.display.flip()
def drawDots():
    global insidecounter
    global outsidecounter
    # generate a bunch of dots that fit on a normal distribution

    x = 2*np.random.rand()-1
    y = 2*np.random.rand()-1

    if incircle(x,y):
        pygame.draw.circle(screen, (255,0,0), (450+int(350*x),550+int(350*y)), 2)
        insidecounter+=1
        pygame.draw.rect(screen, (255,255,255), (600,50,100,50))
        insidenumber = font.render(str(insidecounter),True,(255,0,0),(255,255,255))
        screen.blit(insidenumber,(600, 50))
    else:
        pygame.draw.circle(screen, (0,0,255), (450+int(350*x),550+int(350*y)), 2)
        outsidecounter+=1
        pygame.draw.rect(screen, (255,255,255), (600,100,100,50))

        outsidenumber = font.render(str(outsidecounter),True,(0,0,255),(255,255,255))
        screen.blit(outsidenumber,(600, 100))

    if outsidecounter > 0:
        pygame.draw.rect(screen, (255,255,255), (600,150,150,50))
        rationumber = font.render(str(4.0*(insidecounter/(insidecounter + outsidecounter))),True,(0,0,0),(255,255,255))
        screen.blit(rationumber,(350, 150))
    pygame.display.update()

# main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawDots()

main()
