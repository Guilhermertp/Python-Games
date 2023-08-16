import pygame,sys,random

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score #this will make this variables acessible outside of the function otherside we would get an error,
    #avoid creating this global variables it is bad practice, instead try to use return statments or create a whole  class for the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <=0:
        player_score += 1
        ball_start()

    if ball.right >= screen_width:#check if the ball hits the left wall
        opponent_score += 1
        ball_start()
# we remove this line if code ball_speed_x *= -1 and replace it a function to restart the ball movement instead of inverting the speed of the ball

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    """
    Ball hits left or right wall:
    Teleport it to the center
    Restart in a random direction
    """

def player_animation():
    player.y += player_speed
    # to avoid the player movement out of boundaries(screen)
    if player.top <= 0:
        player.top = 0  # puts the player at the position 0
    if player.bottom >= screen_height:
        player.bottom = screen_height  # puts the player at the position 0, it "teleports" by such small numbers that isn't noticeble the movement

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    # to avoid the opponent movement out of boundaries(screen)
    if opponent.top <= 0:
        opponent.top = 0  # puts the opponent at the position 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height  # puts the opponent at the position 0, it "teleports" by such small numbers that isn't noticeble the movement

def ball_start():
    global ball_speed_y,ball_speed_x
    ball.center = (screen_width/2,screen_height/2) #teleports the ball to the center after the ball its a wall in the ball function above and this fucntion is called
    ball_speed_y *= random.choice((1,-1))# random.choice chooses a random element from a list that is passed into it
    ball_speed_x *= random.choice((1,-1))#after the ball is teleported tot he center the speed is multiplyed by 1 or -1 that randomizes the direction


#General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong') #give the window a title


#the origin of the window is tip left by pygame convention, when drawing he should have that in account
#Game rectangle, this three rectagles are empty to draw them will be in the loop using pygame.draw(surface, color, rect)
ball = pygame.Rect(screen_width/2- 15,screen_height/2 -15,30,30)#the subraction and division is to center the ball, 15 is half of the ball lenght
player = pygame.Rect(screen_width - 20,screen_height/2 -70 ,10,140) #70 is half of the lenght 140
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))#for the ball start in a random direction in the beggining of the game
ball_speed_y = 7 * random.choice((1,-1))#for the ball start in a random direction in the beggining of the game
player_speed = 0
opponent_speed = 7 #the opponent speed will determine the difficulty of the game

"""
3 steps to text to pygame

1.Create a font(and font size)
2.Write text on a new surface
3.Put the text surface on the main surface
"""

#text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

while True:
    #Handling input
    for event in pygame.event.get(): # check for all the user actions like pressing a key
        if event.type == pygame.QUIT: #cheks if the user have clicked the "x" in the top of the screen
            pygame.quit() #method that closes is the opposite of pygame.init() that starts all the pygame methods (starts the game)
            sys.exit() #makes sure that the program is not still runing in the back
        if event.type == pygame.KEYDOWN: #checks for any key in the keyboard if have been pressed fo specific key we need to define a second condition
            if event.key == pygame.K_DOWN: #to check for a specific key in this case key down
               #code that is going to be executed if the down key is pressed
               #if by example we declared player.y += 7 it won't work because we had to press several times the key,
               #keeping it pushed down won't trigger the event we would nee to keep pushing the key and the increment will be small to fix that
               #we need to declare a variable called player speed!!!!
               player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP: #checks for any key in the keyboard if have been pressed fo specific key we need to define a second condition
            if event.key == pygame.K_DOWN: #to check for a specific key in this case key up
               player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    """
    PLAYER MOVEMENT LOGIC
    1.Declare player speed variable
    2.Add this speed to the player on every frame
    3.No button pressed: speed = 0
    4.Button pressed:player speed becomes positive or negative
    """




    ball_animation()
    player_animation()
    opponent_ai()



    #Visuals
    screen.fill(bg_color)#add the background color by filling the entire display surface
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))#line that separates both sides
#Atention to the order in the loop, because the elements will be drawn on top of each other, by example screen.fill(bg_color) in the end will give an output of only a background
    # try to remove the comment to check it his code runs in the end screen.fill(bg_color)

    player_text = game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text,(660,470)) #puts a surface on another
    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_text,(600,470))

    # Updating the window
    pygame.display.flip() # thakes everything that comes from the loop and draws in the screen
    clock.tick(60) #limits how fast the loop runs


#I'm at 11  minutes
#https://www.youtube.com/watch?v=E4Ih9mpn5tk&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k&index=2
