# -*- coding: utf-8 -*-
import pygame
import time
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED,WHITE
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax
FPS = 10

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')
pygame.init()
def get_row_col_from_mouse(pos):
    x,y =pos
    row=y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def gwinnerWhite():
    
        font1 = pygame.font.SysFont('consolas.ttf', 72)
        img1 = font1.render('WHITE  WINS!', True, (50,205,50))
        WIN.blit(img1,(250,350))
        pygame.display.flip()

def gwinnerRed():                
        font2 = pygame.font.SysFont('consolas.ttf', 72)
        img2 = font2.render('RED  WINS!', True, (50,205,50))
        WIN.blit(img2,(250,350))
        pygame.display.flip()
def Draw():
        font2 = pygame.font.SysFont('consolas.ttf', 72)
        img2 = font2.render('DRAW!', True, (50,205,50))
        WIN.blit(img2,(300,350))
        pygame.display.flip()

def main():
    run =True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    
    
    while run:
        clock.tick(FPS)
        if(game.get_board().red_left==0):
            gwinnerWhite()
            pygame.time.delay(5000)  
        
        if(game.get_board().white_left==0):
            gwinnerRed()
            pygame.time.delay(5000)  
            
        if game.turn==RED:
            value,new_board = minimax(game.get_board(),3,RED,game)
            if new_board==None:
                if game.get_board().white_left>0 and game.get_board().red_left>0:
                    Draw()
                pygame.time.delay(5000) 
                
                run==False
                break
            game.ai_move(new_board)
            
        
                
        
        if game.turn==WHITE :
            value,new_board = minimax(game.get_board(),3,WHITE,game) 
            if new_board==None:
                if game.get_board().white_left>0 and game.get_board().red_left>0:
                    Draw()
                pygame.time.delay(5000) 
                run==False
                break
            game.ai_move(new_board)
        
        
        if game.winner()!=None:
            
            pygame.time.delay(5000)                
            run=False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col=get_row_col_from_mouse(pos)
                game.select(row,col)
                
                
        game.update()
    pygame.quit()
    
  
main()

    