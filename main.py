#!/usr/bin/env python
import pygame, math, sys
from pygame.locals import *
import COLOR
from time import sleep

SCREEN_WIDTH      = 480
SCREEN_HEIGHT     = 320
FRAMES_PER_SECOND = 30

RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
GRAY   = (128, 128, 128)

BUTTON_COLOR = (25,25,25)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

button_space  = SCREEN_WIDTH/6/5
button_width  = SCREEN_WIDTH/6
button_height = SCREEN_HEIGHT/3
button_align  = SCREEN_HEIGHT - button_height - button_space/2

button1 = Rect([button_space/2,button_align],[SCREEN_WIDTH/6,SCREEN_HEIGHT/3])
button2 = Rect([button1.right+button_space, button_align],[button_width,button_height])
button3 = Rect([button2.right+button_space, button_align],[button_width,button_height])
button4 = Rect([button3.right+button_space, button_align],[button_width,button_height])
button5 = Rect([button4.right+button_space, button_align],[button_width,button_height])

def print_scr( string, x, y, fontsize=30, fontname=None, color=GRAY ):
	font   = pygame.font.SysFont(None,fontsize)
	text   = font.render(string,True,color)
	screen.blit(text, (x, y))
	pygame.display.flip()

def display_buttons():
	pygame.draw.rect(screen,BUTTON_COLOR,button1,0)
	pygame.draw.rect(screen,BUTTON_COLOR,button2,0)
	pygame.draw.rect(screen,BUTTON_COLOR,button3,0)
	pygame.draw.rect(screen,BUTTON_COLOR,button4,0)
	pygame.draw.rect(screen,BUTTON_COLOR,button5,0)
	pygame.display.flip()

while True:
	for i in pygame.event.get():
		if i.type == QUIT:
			exit()
	screen.fill((0,0,0))
	print_scr(str(pygame.mouse.get_pos()), 10, 10)
	display_buttons()
	mousepress=pygame.mouse.get_pressed()			
	pygame.display.update()
	sleep(.10)
