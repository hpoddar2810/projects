import pygame
from random import randint
pygame.init()

def isboardfull(board):
    if board.count(' ') == 0:
        return True
    
    return False


def check(board,sign):
    bo = [0] + board
    return  ( (bo[1] == sign and bo[2] == sign and bo[3] == sign) or
            (bo[4] == sign and bo[5] == sign and bo[6] == sign) or
            (bo[7] == sign and bo[8] == sign and bo[9] == sign) or
            (bo[1] == sign and bo[4] == sign and bo[7] == sign) or
            (bo[2] == sign and bo[5] == sign and bo[8] == sign) or
            (bo[3] == sign and bo[6] == sign and bo[9] == sign) or
            (bo[1] == sign and bo[5] == sign and bo[9] == sign) or
            (bo[3] == sign and bo[5] == sign and bo[7] == sign) )


def pos_empty(board, pos):
    if board[pos] == ' ':
        return True
    return False


def machinemove(board):
    for i in range(9):
        if pos_empty(board, i):
            bo = board.copy()
            bo[i] = '0'
            if check(bo, '0'):
                return i
    
    for i in range(9):
        if pos_empty(board, i):
            bo = board.copy()
            bo[i] = 'X'
            if check(bo, 'X'):
                return i

    
    pos = 4
    while not pos_empty(board, pos):
        pos = randint(0,8)
    
    return pos
    
    
def game_wait():
    for i in range(300):
        pygame.time.delay(30)

def win_screen(sign):
    font1 = pygame.font.SysFont('Arial', 50)

    if sign == 'X':
        textwin = font1.render('You Won!!!', True, (0, 255, 0))
    else: 
        textwin = font1.render('computer Won!!!', True, (0, 255, 0))
    
    win.blit(textwin, (150 - textwin.get_width()//2, 150 - textwin.get_height()//2))
    pygame.display.update()

screen_width = 500
screen_height = 300
font = pygame.font.SysFont('Arial', 50)
white = (255, 255, 255)
textx = font.render("X", True, white)
text0 = font.render("0", True, white)
rects =[]
board = [' ']*9

win = pygame.display.set_mode((screen_width, screen_height))
win.fill(white)
pygame.display.set_caption("Tic Tac Toe")

for i in range(9):
    pygame.draw.rect(win, (0,0,0), ((i%3)*100, (i//3)*100, 99, 99))
    area = pygame.Rect((i%3)*100, (i//3)*100, 99, 99)
    rects.append(area)

rects.append(pygame.Rect(0, 0, 300, 300))
pygame.display.update()
pygame.event.clear()
while not isboardfull(board):
    print("1")
    pygame.time.delay(60)
    print("2")

    event = pygame.event.wait()
    #events = pygame.event.get()

    #for event in events:
    print(event.type)
    print('6')
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()



    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and rects[9].collidepoint(pygame.mouse.get_pos()):
        print("3")
        for i in range(9):
            if rects[i].collidepoint(event.pos):
                print('4')
                win.blit(textx, ((i%3)*100 + 35, (i//3)*100 + 25))
                board[i] = 'X'
                continue

        print('7')
        pygame.display.update()
        #game_wait()
        print('8')
        if check(board, 'X'):
            print('5')
            win_screen('X')
            game_wait()
            pygame.quit()
            exit()

        pos = machinemove(board)
        board[pos] = '0'
        win.blit(text0, ((pos%3)*100 + 35, (pos//3)*100 + 25))
        pygame.display.update()
        #game_wait()

        if check(board, '0'):
            win_screen('0')
            game_wait()
            pygame.quit()
            exit()
