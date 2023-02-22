import os
import pygame
import time
import random

_screen_width = 800
_screen_height = 700
_play_width = 300  #10 blocks of 30 width
_play_height = 600 #20 blocks of 30 height
_block_size = 30

_top_left_x = (_screen_width - _play_width) // 2
_top_left_y = _screen_height - _play_height

#shapes

#I
I = [['00100',
      '00100',
      '00100',
      '00100',
      '00100'],
     
     ['00000',
      '00000',
      '11111',
      '00000',
      '00000']]



#L

L = [['00100',
      '00100',
      '00100',
      '00100',
      '00111'],
     
     ['00001',
      '00001',
      '11111',
      '00000',
      '00000']]

#O

O = [['00000',
      '01110',
      '01110',
      '01110',
      '00000'],
     
     ['00000',
      '01110',
      '01110',
      '01110',
      '00000']]

#S
S = [['00010',
      '00010',
      '01110',
      '01000',
      '01000'],
     
     ['01000',
      '01000',
      '01110',
      '00010',
      '00010']]

#random lists

shapes =[I,L,O,S]
colors = ['green','orange','red','blue','yellow','pink']


accepted_pos =  [[(x,y) for x in range(10)] for y in range(20)]

class Piece(object):
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(colors)
        self.rotation = 0

def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for y in range (len(grid)):
        for x in range(len(grid[y])):
            if(x,y) in locked_pos:
                c = locked_pos[(x,y)]
                grid[y][x] = c

    return grid

def get_shape():
    return Piece(5,0,random.choice(shapes))

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '1':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions


def valid_space(shape,grid):
    
    accepted_pos =  [[(x,y) for x in range(10) if grid[y][x] == (0,0,0)] for y in range(20)]
    accepted_pos =  [x for sub in accepted_pos for x in sub]
    formatted = convert_shape_format(shape)

    for position in formatted:
        if position not in accepted_pos:
            if position[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x,y = pos
        if y < 1:
            return True
    return False

def draw_grid(surface,row, col):
    sx = _top_left_x
    sy = _top_left_y

    for y in range (row):
        pygame.draw.line(surface, 'grey', (sx, sy+y*_block_size), (sx+_play_width,sy+y*_block_size))
        for x in range(col):
                pygame.draw.line(surface, 'grey', (sx+x*_block_size, sy), (sx+x*_block_size,sy+_play_height))

        
def draw_window(surface,grid):
    surface.fill((0,0,0))
    pygame.font.init()
    font = pygame.font.SysFont('comicsans',60)
    label = font.render('Tetris JK :D',1,'green')

    surface.blit(label, (_top_left_x + _play_width/2 - (label.get_width()/2), 30))

    font = pygame.font.SysFont('comicsans',20)

    text = font.render('This is easy mode!',1,'yellow')
    surface.blit(text, (_top_left_x + _play_width*1.1, _top_left_y*1.5))

    for y in range (len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (_top_left_x+x*_block_size,_top_left_y+y*_block_size, _block_size,_block_size),0)

    draw_grid(surface,20,10)
    pygame.draw.rect(surface, 'green', (_top_left_x,_top_left_y,_play_width,_play_height), 3)

    pygame.display.update()

def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5
    counter = 0
    

    while run:

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        counter+=1
   
        if counter > 10000:
            fall_speed -= 0.05
            counter = 0
            font = pygame.font.SysFont('comicsans',20)
            text = font.render('Faster!',1,'red')
            print(fall_speed)
                    

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    #current_piece.y -= 1
                    #if not(valid_space(current_piece,grid)):
                        #current_piece.y += 1
                    current_piece.rotation += 1
                    if not(valid_space(current_piece,grid)):
                        current_piece -= 1

    
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0],pos[1])
                locked_positions[p] = current_piece.color

            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(win,grid)

        if check_lost(locked_positions):
            run =  False

    
        

def main_menu(win):
    main(win)


win = pygame.display.set_mode((_screen_width,_screen_height))
pygame.display.set_caption('Tetris')
                        
main_menu(win)

                        
        

##if __name__ == "__main__":
##    tetris()
