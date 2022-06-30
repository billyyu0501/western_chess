# This function holds the moving rule of different chess
# two arrays (dest and capture) will be returned as a result 
from asyncio.windows_events import NULL
from pickle import TRUE


def possible_move(board,chess_pos,chess_type,player):
    d_chess = ['kdt','qdt','rdt','bdt','kdt','pdt']
    l_chess = ['klt','qlt','rlt','blt','klt','plt']
    dest = []
    capture = []
    param = 20 if player ==1 else 10 
    match chess_type[0]:
        case "k": #King
            for x in range(-1,2):
                for y in range(-1,2):
                    # skip if the dest is out of range 
                    if not(-1<chess_pos[1]+y<8 and -1<chess_pos[0]+x<8):
                        continue
                    chess = board[chess_pos[1]+y][chess_pos[0]+x]
                    print(f"{chess} {chess//param}")
                    if chess == 0:
                        dest.append((chess_pos[0]+x,chess_pos[1]+y))
                    elif chess//param ==1: 
                        capture.append((chess_pos[0]+x,chess_pos[1]+y))
        case "q": #Queen
            direction = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
            for route in direction:
                dist = 1 
                while True:
                    x,y = route[0]*dist, route[1]*dist
                    if not(-1<chess_pos[1]+y <8 and -1<chess_pos[0]+x<8):
                        break
                    if board[chess_pos[1]+y][chess_pos[0]+x] ==0:
                        dest.append((chess_pos[0]+x,chess_pos[1]+y))
                        dist +=1
                        continue
                    if board[chess_pos[1]+y][chess_pos[0]+x]//param ==1:
                        capture.append((chess_pos[0]+x,chess_pos[1]+y))
                    break
        case "r": #Root
            direction = [(1,0),(0,1),(-1,0),(0,-1)]
            for route in direction:
                dist = 1 
                while True:
                    x,y = route[0]*dist, route[1]*dist
                    if not(-1<chess_pos[1]+y <8 and -1<chess_pos[0]+x<8):
                        break
                    if board[chess_pos[1]+y][chess_pos[0]+x] ==0:
                        dest.append((chess_pos[0]+x,chess_pos[1]+y))
                        dist +=1
                        continue
                    if board[chess_pos[1]+y][chess_pos[0]+x]//param ==1:
                        capture.append((chess_pos[0]+x,chess_pos[1]+y))
                    break
        case "b": #Bishop
            direction = [(-1,-1),(-1,1),(1,-1),(1,1)]
            for route in direction:
                dist = 1 
                while True:
                    x,y = route[0]*dist, route[1]*dist
                    if not(-1<chess_pos[1]+y <8 and -1<chess_pos[0]+x<8):
                        break
                    if board[chess_pos[1]+y][chess_pos[0]+x] ==0:
                        dest.append((chess_pos[0]+x,chess_pos[1]+y))
                        dist +=1
                        continue
                    if board[chess_pos[1]+y][chess_pos[0]+x]//param ==1:
                        capture.append((chess_pos[0]+x,chess_pos[1]+y))
                    break
        case "n": #Knight
            for x in range(-2,3):
                for y in range(-2,3):
                    # the movement pattern of knight 
                    if (abs(x)==abs(y) or x==0 or y==0):
                        continue
                    # take away those coordinate that is out of boundary
                    if not(-1<chess_pos[1]+y <8 and -1<chess_pos[0]+x<8):
                        continue
                    # distinguish the possible dest, chess that can be captured and append them into corresponding array 
                    if board[chess_pos[1]+y][chess_pos[0]+x] ==0:
                        dest.append((chess_pos[0]+x,chess_pos[1]+y))
                    if board[chess_pos[1]+y][chess_pos[0]+x]//param ==1:
                        capture.append((chess_pos[0]+x,chess_pos[1]+y))
        case "p": #pawn
            direction = -1 if player == 1 else 1
            init_pos = 6 if player ==1 else 1 
            if not -1<chess_pos[1]+direction<8:
                return dest,capture
            if board[chess_pos[1]+direction][chess_pos[0]] == 0:
                dest.append((chess_pos[0],chess_pos[1]+direction))
                if board[chess_pos[1]+direction*2][chess_pos[0]] ==0 and chess_pos[1]== init_pos:
                    dest.append((chess_pos[0],chess_pos[1]+direction*2))
            #detect capture chess move
            for y in range(-1,2,2):
                if not( -1<chess_pos[1]+direction<8 and -1<chess_pos[0]+y<8):
                    continue
                if board[chess_pos[1]+direction][chess_pos[0]+y]//param ==1:
                    capture.append((chess_pos[0]+y,chess_pos[1]+direction))
    return dest,capture

def move(origin,dest,board):
    chess = board[origin[1]][origin[0]]
    board[origin[1]][origin[0]] = 0
    board[dest[1]][dest[0]] = chess
    return board

def endgame(board):
    dp,lp = False, False
    for y in range(8):
        if 20 in board[y]: dp = True 
        if 10 in board[y]: lp = True 
    match dp, lp:
        case True,True:
            return 0
        case False, True:
            return 1 
        case True, False:
            return 2

            
    