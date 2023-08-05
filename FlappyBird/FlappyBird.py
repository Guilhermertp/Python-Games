import pygame, sys, random

#funtion to add to surfaces on the screen so when the floor is makeing it doesn't disapperar from the screen
def draw_floor():
    #creates the ilusion that the fllor moves but doesn't disappear with the two surfaces
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos+576, 900))

#function that returns a new pipe with the dimensions of the surface
def create_pipe():
    random_pipe_pos = random.choice(pipe_height) #pick a random item from a list
    #new_pipe = pipe_surface.get_rect(midtop= (288,512))#half of the dimensions of the screen (288x2=576)
    bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe,top_pipe# this returns a tuple because there are two variables instead of one, we will need to use extend in the game loop to add it to the pipe list

#function tthat takes a list of pipes and moves each pipe a tiny bit to the left and returning a new list of pipes
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024: #since the screen lenght is 1024 to reach that means is passing the bottom frontier
           screen.blit(pipe_surface,pipe )
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True) #create new surface that is being flipped using pygame method
            screen.blit(flip_pipe,pipe)

def check_collision(pipes): #game function check_collision affect the game_active varible, if it returns false it will store the False in the game_active variable
    for pipe in pipes:
        if bird_rect.colliderect(pipe):#check if the bird rectangle collides with the pipe rectangle
            #print('collision')
            death_sound.play()#each time the bird hits a pipe or any surface it plays this sound
            return False
    #if the bird gets too high or too low activate colision,we should avoid to use collision function if not
    #necessary to make the game more efficient, in this case we just need to check the position of the bird to activate collision
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:#the floor is at the position 900 but we need an interval because in games the position is not exactly 900 is a good principle to take in consideration
        print('collision')
        return False
    return True #it returns True if neither of the conditions above get triggered, it means that if there is a colision game_active equal to false and the code in the while loop won't run, nothing will happen in the screen

def rotate_bird(bird):
    new_bird =pygame.transform.rotozoom(bird,-bird_movement*3,1)#rotozoom allows to rotate and zoom or just one of the options, the minus("-"= is to change the direction of the roration
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))# creates a new rectangle based on the centery of the previous rectangle, so we don't change the position of the bird when we are updating the bird
    return new_bird,new_bird_rect

def score_display(game_state): #shows the scroe for the main game
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255,255))  # this tupple are the RGB colors(red,green and blue) that we mix to obtain one color this is the max that gives white if everyone was zerp we would get black
        score_rect = score_surface.get_rect(center=(288, 100))  # creates a rectangle around it to make it easyier to put in the center of the screen
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255,255))  # this tupple are the RGB colors(red,green and blue) that we mix to obtain one color this is the max that gives white if everyone was zerp we would get black
        score_rect = score_surface.get_rect(center=(288, 100))  # creates a rectangle around it to make it easyier to put in the center of the screen
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255,255))  # this tupple are the RGB colors(red,green and blue) that we mix to obtain one color this is the max that gives white if everyone was zerp we would get black
        high_score_rect = high_score_surface.get_rect(center=(288, 850))  # creates a rectangle around it to make it easyier to put in the center of the screen
        screen.blit(high_score_surface,high_score_rect)

def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score #we have to return since the high_score is in the local scope of the function
"""
********** LOGIC FOR FUNCTION FOR THE GAME OVER SCREEN***************

 if game_active:
    logic of our game
     game_active = check_collision()
else:
   game over logic

"""
pygame.mixer.pre_init(frequency = 44100, size =16, channels = 1, buffer = 512) #this way the sound won't have the delay between the press of a key and hearing the sound

pygame.init() #initiates all imported pygame modules
screen = pygame.display.set_mode((576,1024)) #create a black canvas/screen width and height
clock = pygame.time.Clock() #can limit the frame rate between other things
game_font = pygame.font.Font('04B_19.ttf',40) # '04B_19' is a font type used in the flappyBird game,40 is the size of the text
"""
********************************************************************
                                   GAME VARIABLES
**********************************************************************
"""
gravity = 0.25
bird_movement = 0 #variable that is going to be applyied to the data, is going to be update to move the bird_rectangle
#and then moving the bird_surface in the while loop

game_active = True
score = 0
high_score = 0

#import background background image
bg_surface = pygame.image.load('sprites/background-day.png').convert()
"""
convert()
is not mandatory but it converts the image in a format that is easyer for pygame to use
what makes the game run better and faster when the game becomes heavier
"""

#scale the background image(double the size) to fill all the canvas, try to comment this line of code to see what happened before
bg_surface = pygame.transform.scale2x(bg_surface)

#load the floor image that will be moving during the game and scale it like it was done for the background
floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

#to move the floor we nee to update the x point in the while loop, moving by small increments it will look like a fluid motion
floor_x_pos = 0

#Creating the animation of the bird flap using three images in a list that will be picked in a certain time to give the ilusion of movement(animation)
bird_downflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-downflap.png').convert_alpha())
bird_midflap  = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-midflap.png').convert_alpha())
bird_upflap   = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512)) #create rectangle around the bird surface

BIRDFLAP = pygame.USEREVENT +1 #the plus one is to create a different user event since we already have one for the pipe
pygame.time.set_timer(BIRDFLAP,200) #the index in bird_index is changing every 200 miliseconds, it is going to cycle throught the 3 images of the bird flaps

#imports the picture of the bird and scales
#bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha()#to remove the black surface envoling the bird, this surface appears when we change the rotation of the original image
#bird_surface = pygame.transform.scale2x(bird_surface)
#takes the new surface and puts a rectangle around it
#bird_rect = bird_surface.get_rect(center= (100,512))#center is the point choosen for the rectangle and the tuple with the coordinates

#*************************PIPES PROCESS*****************************************
#1.IMPORT IMAGE ON SURFACE
#2.PUT RECT AROUND SURFACE
#3.BLIT(SURFCE,RECT)

#1.IMPORT IMAGE ON SURFACE
pipe_surface = pygame.image.load('sprites/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
#2.PUT RECT AROUND SURFACE
pipe_list = []#it is going to conatin several rectangles where new rectangles will be assigned to each rectangle
#put new rectangles using a timer
SPAWNPIPE = pygame.USEREVENT #this event is going to be triggered by a timer and not a click in the mouse like some other events in the code
pygame.time.set_timer(SPAWNPIPE,1200)#event that is being triggered every 1.2 seconds
pipe_height = [400,600,800] #all the possible heights our pipe can have

#*************************SOUNDS*********************************************importing sound into pygame
flap_sound = pygame.mixer.Sound('audio/wing.wav')
death_sound = pygame.mixer.Sound('audio/hit.wav')
score_sound = pygame.mixer.Sound('audio/point.wav')

score_sound_countdown = 100 #new variable to make it easy to play score sound when score += 0.01  in the main loop gets to a full number(integer).


#*******************Game over surface****************************************
game_over_surface =  pygame.transform.scale2x(pygame.image.load('sprites/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(288,512))
"""
***********************************************************
                          GAME LOOP
***********************************************************
"""


#loop to keep the screen/canvas open unless we close it in the x button
while True:
    for event in pygame.event.get(): #pygames look for all the events are happening like closing window,clicking mouse etc...
        if event.type == pygame.QUIT: #condition for event QUIT that if true runs the following code to close the game
            pygame.quit()##close the game if pressed the X button on top of the screen
            sys.exit() #access the system module to make sure the game stops running, because without this the while loop will be still running and we want it to stop

        #check if any keys of the keyboard are pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active: #check for a specific key
                bird_movement = 0#to disable the effects of gravity variable or the jump wouldn't work proprely
                bird_movement -=12#to make the bird jump we need to make the bird_movement value negative
                flap_sound.play()#plays the sound in the wave file
            if event.key == pygame.K_SPACE and game_active == False: #only runs if I press space and the game is over
                game_active = True
                pipe_list.clear()#when we start the game again we want to avoid spawning multiple pipes from the previous game
                bird_rect.center = (100,512)#when the game re-starts puts the bird in the original position
                bird_movement = 0 #clear the bird number because it can be an high positive number afecting the re-start of the game
                score = 0# to avoid that when we press the keyboard key and the game restarts that the score restarts from zero

        if event.type == SPAWNPIPE:
            #pipe_list.append(create_pipe()) # we can't use append because in the function create pipe we are returning two variables instead of one, it it was just the bottom pipe it is ok
            #we have to use extend since the function create pipe returns a tupple
            pipe_list.extend(create_pipe())

            """
            extend()method is used to iterate over an iterable(string, tuple, list, set, or dictionary) and then add each
            element of the iterable to the end of the current list.append(
            """
        if event.type == BIRDFLAP:
            if bird_index <2: #to make sure is not out of range for the index (goes till 2)
                bird_index += 1
            else:
                bird_index = 0
            bird_surface,bird_rect = bird_animation()#takes an item from the list bird_surface = bird_frames[bird_index] and puts a new rectangle around it, it is important because the images/frames might have different dimensions
            #but the rectangle must have the same dimesnion as the surface surround them.


    # 'blit' method put one surface in another,in this case put the background image/surface in the screen surface
    screen.blit(bg_surface,(0,0)) #we need to define the xy coordinates for the background image
#in pygame the origin point is the top left of the screen, when we define 0,0 is the top left

    if game_active: #the following code only runs if game_active is equal to True
        # ********************************************** BIRD **********************************************
        bird_movement += gravity  # is going to increase from 0.25 to 0.5,0.75,1 etc
        rotated_bird = rotate_bird(bird_surface)#using a new function that returns a rotated bird based on the original bird surface after being rotated
        bird_rect.centery += bird_movement  # move the rectangle in the axis y
        screen.blit(rotated_bird, bird_rect)  # bird rect is in place where the coordinate tupple would be

        game_active = check_collision(pipe_list)

        # ********************************************** PIPES **********************************************
        pipe_list = move_pipes(
            pipe_list)  # take all the pipes and mpve them and overwrite the pipe list with the new pipes
        draw_pipes(pipe_list)  # show the new pipes
        # ********************************************** SCORE  ******************************************
        score += 0.01 #this is trigered at the same time as the next line score_sound_countdown = 100
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')
# ********************************************** FLOOR **********************************************
    #increments added to x coordinate to make the floor move to the left
    floor_x_pos -=1
    """
    The floor is going to disappear and to avoid that we need to have another floor image next the other
    """
    draw_floor()
    #to avoid to have the floor disapearing
    if floor_x_pos <= -576: # if left surface to far to the left it will do something
        floor_x_pos = 0#resets the position to where it started


    #screen.blit(floor_surface,(0,0)) I need to change the coordinate so the floor is in the bottom and not in the top
    #screen.blit(floor_surface, (floor_x_pos, 900))

    pygame.display.update() #takes everything in the while loop and updates it in the screen by example
    #if we add an image it will update the screen for the image to pop up
    clock.tick(120) #limits the game to not run faster than 120 frames per second, it can run slower

"""
FRAMES PER SECOND 
How many pictures(/frames) a game draws in a single second.
They influence how fast(and fluid) a game runs.

Display Surface and regular surface
Dsiplay surface can only be one and always be shown
while regular surface can be manny and only displayed when attached to the display surface

To check foor colisions we have to create a rectangle around our player/bird and the obstacles
to check for colisions. Creating rectangles - > pygame.Rect(width,height,x,y) or surface.get_rect(rect_position)
the second gets the rectangle around the surface

Rotation on pygame leds to losing quality

                    Text in pygame
                1.Create a font(style,size)
                2.Render the font(text, colour)
                3.Use the resulting text surface

"""

