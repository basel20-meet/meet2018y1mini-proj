
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:basel
Date:30,10,2003
"""
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 100
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
screen=turtle.Screen()
snake = turtle.clone()
turtle.register_shape("moshiko.gif")
snake.shape("moshiko.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


for i in range(START_LENGTH):
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

    x_pos=x_pos+20
    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    var= snake.stamp()
    stamp_list.append(var)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN=1
LEFT=2
RIGHT=3
direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP#Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the DOWN key!")
def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the LEFT key!")
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    move_snake() 
    print("You pressed the RIGHT key!")
turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if my_pos in pos_list[:-1]:
        quit()
        
        
    
    if direction== DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,  SQUARE_SIZE + y_pos)
        print("You moved left!")    
    elif direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved left!")
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("take it easy")
       # quit()
    if new_x_pos <= LEFT_EDGE:
        print("moshiko dont crash") 
    
    if new_y_pos >= UP_EDGE:
        print("take it easy")
        #quit()
    if new_y_pos <= DOWN_EDGE:
        print("moshiko dont crash")
        #quit()
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_ind])                
                                               
        food_pos.pop(food_ind) 
        food_stamps.pop(food_ind) 
        print("You have eaten the food!")

     
    if len(food_stamps) <= 6 :
        make_food()
    elif snake.pos() not in food_pos:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    if len(food_stamps) <= 6 :
        make_food()
turtle.register_shape("coffe.gif") 
food = turtle.clone()
food.shape("coffe.gif") 
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for mytuple in food_pos :
    x = mytuple[0]
    y = mytuple[1]
    food.goto(x,y)
    var= food.stamp()
    food_stamps.append(var)
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)  
    food_pos.append(food.pos())
    var= food.stamp()
    food_stamps.append(var)


    
 







    





