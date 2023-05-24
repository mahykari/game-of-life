import random
import time
import curses
import shutil


TERM_W, TERM_H = shutil.get_terminal_size()
W, H = TERM_W // 2, TERM_H
ITER = 1000
DEAD, LIVE = '-+'

MOVES = [
  ( 0, 1), # E
  ( 1, 1), # SE
  ( 1, 0), # S
  ( 1,-1), # SW
  ( 0,-1), # W
  (-1,-1), # NW
  (-1, 0), # N
  (-1, 1), # NE
]


def freshgen():
  gen_ = [[' ' for _ in range(W)] for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if random.random() < 0.3:
        gen_[i][j] = LIVE
      else:
        gen_[i][j] = DEAD
  
  return gen_  


def nextgen(gen_):
  nextgen_ = freshgen()
  for i in range(H):
    for j in range(W):
      nextgen_[i][j] = update(gen_, i, j)
  return nextgen_


def update(gen_, r, c): # r, c = row, col
  neighbors = [move(r, c, dr, dc) for (dr, dc) in MOVES]
  live_neigbors = [
    (r, c) for (r, c) in neighbors if gen_[r][c] == LIVE]
  n = len(live_neigbors)
  
  if gen_[r][c] == DEAD and n == 3:
      return LIVE 
  if gen_[r][c] == LIVE and (n == 2 or n == 3):
    return LIVE
  return DEAD


def flip(n, N):
  return n % N


def move(x, y, dx, dy):
  xp, yp = x+dx, y+dy
  return flip(xp, H), flip(yp, W)


def printgen(stdscr, gen_):
  # Geometric y- and x-axis
  for y in range(H):
    for x in range(W):
      txtattr = -1
      if gen_[y][x] == DEAD:
        txtattr = curses.A_DIM
      if gen_[y][x] == LIVE:
        txtattr = curses.A_BOLD
      stdscr.addstr(y, 2*x, gen_[y][x], txtattr)
      if 2*x+1 < W: stdscr.addstr(y, 2*x+1, ' ')
  
  stdscr.refresh()


def curses_colors():
  curses.use_default_colors()
  for i in range(curses.COLORS):
    curses.init_pair(i+1, i, -1)


def main(stdscr):
  curses_colors()
  
  gen_ = freshgen()
  for _ in range(ITER):
    printgen(stdscr, gen_)
    gen_ = nextgen(gen_)
    time.sleep(0.1)


curses.wrapper(main)
