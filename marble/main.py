from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

w = (255,255,0)     #wall
f = (0,0,0)         #floor
m = (255,255,255)   #marble
g = (0,255,0)       #goal
t = (255,0,0)       #trap
l = (127,51,0)      #life
b = (0,100,0)       #border

x = 1               #strarting coordinates for the marble
y = 1               #vertical
life = 7

maze      = [[w,w,w,w,w,w,w,w,w,w],              #smaller maze
             [w,f,f,f,f,f,f,f,f,w],
             [w,w,w,f,w,t,f,w,f,w],
             [w,t,w,f,w,w,w,w,f,w],
             [w,f,f,f,f,f,f,w,f,w],
             [w,w,w,w,w,w,f,w,f,w],
             [w,f,g,w,t,w,f,w,f,w],
             [w,f,w,w,f,f,f,w,f,w],
             [w,f,f,w,w,w,w,w,f,w],
             [w,t,f,f,f,f,f,f,f,w],
             [w,w,w,w,w,w,w,w,w,w]]
             
maze_test = [[w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],    #bigger version of the maze
            [w,t,f,f,f,f,w,t,f,f,f,f,f,f,f,f,w],
            [w,f,f,f,f,f,f,f,f,f,w,t,f,f,f,f,w],
            [w,f,w,w,w,w,w,w,w,w,w,w,w,w,f,f,w],
            [w,f,f,f,t,w,f,f,f,f,f,f,t,w,w,f,w],
            [w,f,f,f,f,w,f,w,w,w,w,f,f,w,t,f,w],
            [w,w,w,w,f,w,f,w,g,f,w,f,f,w,f,f,w],
            [w,f,f,w,f,w,f,w,f,f,w,f,f,w,f,f,w],
            [w,f,f,w,f,w,f,f,f,f,w,w,f,w,f,w,w],
            [w,f,f,w,f,w,f,f,f,t,w,f,f,w,f,t,w],
            [w,f,f,w,f,w,w,w,w,w,w,f,f,w,f,f,w],
            [w,f,f,w,f,f,t,w,f,f,f,f,f,w,f,f,w],
            [w,f,f,w,f,f,f,f,f,f,f,f,t,w,w,f,w],
            [w,f,f,w,w,w,w,w,w,w,w,w,w,w,t,f,w],
            [w,f,f,f,w,f,f,f,f,f,f,t,w,t,f,f,w],
            [w,t,f,f,f,f,f,t,w,f,f,f,f,f,f,f,w],
            [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w]]

rows = len(maze)                            #getting the dimensions of the maze matrix for dynamic maze size handling
cols = len(maze[0])

display = [[f,f,f,f,f,f,f,b],               #display matrix filled with blank pixels and with a border to make an odd screen
        [f,f,f,f,f,f,f,b],
        [f,f,f,f,f,f,f,b],
        [f,f,f,f,f,f,f,b],
        [f,f,f,f,f,f,f,b],
        [f,f,f,f,f,f,f,b],
        [f,f,f,f,f,f,f,b],
        [b,b,b,b,b,b,b,b]]

game_over = False

def check_wall(x,y,new_x,new_y):            #function for checking collision with the wall
  if maze[new_y][new_x] != w:
    return new_x, new_y
  elif maze[new_y][x] != w:
    return x, new_y
  elif maze[y][new_x] != w:
    return new_x, y
  else:
    return x, y

def move_marble(pitch, roll, x, y):         #function for moving the marble
  new_x = x
  new_y = y
  if 2 < pitch < 178 and x != 0:
    new_x -= 1
  if 182 < pitch < 358 and x != cols:
    new_x += 1
  if 2 <roll < 178 and y != rows:
    new_y += 1
  if 182 < roll < 358 and y !=0:
    new_y -= 1
  new_x, new_y = check_wall(x,y,new_x,new_y)
  return new_x, new_y

def set_display(x,y):                       #function for setting the pixels of the display matrix
  for i in range(0, 7):
    for j in range(0, 7):
      if 0 <= (y-3+i) < rows and 0 <= (x-3+j) < cols:
        display[i][j] = maze[y-3+i][x-3+j]
      else:
        display[i][j] = w
  for i in range(0,7):                      #displaying the remaining lives in the bottom row
    display[7][i] = b
  for li in range(0, life):
    display[7][li] = l
  
while not game_over:                        #main program
  o = sense.get_orientation()               #getting the internal mesurement unit data from the sense hat
  pitch = o["pitch"]
  roll = o["roll"]
  x, y = move_marble(pitch, roll, x, y)
  if maze[y][x] == g:                       #checking if the win condition is fulfilled
    sense.show_message("WIN!")
    game_over = True
  if maze[y][x] == t:                       #checking if the marble collided with a trap
    if life > 1:
      life -= 1
      x = 1
      y = 1
      sense.show_message("LIFE LOST!")      #if there are still lives left remove one and display message
      sense.clear()
    else:
      sense.show_message("GAME OVER!")      #if none left set game over condition to true and display message
      game_over = True
  maze[y][x] = m 
  set_display(x,y)
  sense.set_pixels(sum(display,[]))
  sleep(0.2)
  maze[y][x] = f
  
sense.clear()
