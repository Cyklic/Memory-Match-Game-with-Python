import pygame #Import pygame module
import os  #Import Operating Systems module
import random #Import random module

pygame.init() #Initializing pygame

#Game variables
g_width = 1100 #width of the screen
g_height = 650 #height of the screen
pic_width = 140 #width of each picture
pic_height = 70 #height of each picture
g_columns = 5 #Number of columns for the game
g_rows = 6 #Number of rows for the game
padding = 20 #General padding for the distance between each picture
left_margin = (g_width - (g_columns * pic_width + (g_columns - 1) * padding)) // 2 #Custom left and right margin for distance from edge of screen   
right_margin = left_margin
top_margin = (g_height - (g_rows * pic_height + (g_rows - 1) * padding)) // 2 #Custom top and bottom margin
bot_margin = top_margin
white = (255, 255, 255) #Creating the color white
black = (0, 0, 0) #Creating the color black
pick1 = None #Variable for first pick
pick2 = None #variable for second pick
head_font = pygame.font.Font('Freedom-10eM.ttf', 50) #Creating font for header text

#Loading pygame screen
screen = pygame.display.set_mode((g_width, g_height)) #Displaying the screen using width and height diemsions
pygame.display.set_caption('Memory Match Game') #Creating Game Name/Caption

#Load background image
bg_image = pygame.image.load('background.jpg') #For background image
bg_image = pygame.transform.scale(bg_image, (g_width, g_height)) #Making dimesions for the background image
bg_image_rect = bg_image.get_rect() #Creating rectangle for the bg image to display

#Create list of every pictures
game_pics = [] #List for storing the pictures that would be used for the game
for item in os.listdir('images/'): #Using the os module to loop the image directory to get the images in it
    game_pics.append(item.split('.')[0]) #This is to remove everything from the '.' to the right
game_pics_copy = game_pics.copy() #Creating a copy for each picture to make them doubled for the point of the game
game_pics.extend(game_pics_copy) #Extending not append so it doesnt add it to the gamepic list as a nested list   
game_pics_copy.clear() #Clear after extending
random.shuffle(game_pics) #Using the random module to randomize the gamepics list

#Load each image into python memory
mem_pics = [] #List for memory pictures
mem_pic_rect = [] #Creating rectangle list for the pictures in the mempic list
revealed_imgs = [] #List of revealed pictures
for item in game_pics: #For loop to put back the pictures names to their full names for loading
    pic = pygame.image.load(f'images/{item}.png') #adding the rest of the picture files name to load them
    pic = pygame.transform.scale(pic, (pic_width, pic_height)) #Scaling the pictures to the same size
    mem_pics.append(pic) #Adding the scaled pictures to the mempic list
    pic_rect = pic.get_rect() #Creating rectangles for each picture 
    mem_pic_rect.append(pic_rect)#Appending these rectangles to the mempicrect list
    
for i in range(len(mem_pic_rect)): #For loop for custom grid creation using index of pictures in mempicrect list
    mem_pic_rect[i].x = left_margin + (i % g_columns) * (pic_width + padding) #Creating x(horizontal) placement for the grid which is 0, 1, 2, 3, 4 because of column number is 5
    mem_pic_rect[i].y = top_margin + (i // g_columns) * (pic_height + padding) #Creating y(vertical) placement for the grid which is 00000, 11111, 22222, ..., 55555
    revealed_imgs.append(False) #False so that when we click on the picture it will ture True and it will be revealed

def create_bg(): #Function for creating the game background
    top_area = pygame.draw.rect(screen, black, [0, 0, g_width, 57], 0) #Creating top area for the title 
    head_text = head_font.render('MEMORY MATCH GAME', True, white) #Defining the title 
    screen.blit(head_text, (217,3)) #Displaying the title
    botm_area = pygame.draw.rect(screen, black, [0, g_height - 55, g_width, 100], 0) #Creating a bottom area

game_loop = True #Create game loop
while game_loop:
    screen.blit(bg_image, bg_image_rect) #Load backgroud image while the game loop is active
    create_bg()
     
    #Input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # For quitting by pressing the x 
            game_loop = False #After quitting turn of game loop
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Handle button event
            for item in mem_pic_rect:
                if item.collidepoint(event.pos): #If I click it should get the index point of where I clicked
                    if revealed_imgs[mem_pic_rect.index(item)] != True:
                        if pick1 != None: #If pick1 one has been done
                            pick2 = mem_pic_rect.index(item) #Allow for second picking (pick2)
                            revealed_imgs[pick2] = True #Change revealed picture for pick2 to true to reveal the picture
                        else: #If pick1 hasnt been done
                            pick1 = mem_pic_rect.index(item) #Allow for first picking (pick2)
                            revealed_imgs[pick1] = True #Change revealed picture for pick1 to true to reveal the picture    

    for i in range(len(game_pics)): #Uploading pictures to game screen
        if revealed_imgs[i] == True: #If picture is revealed 
            screen.blit(mem_pics[i], mem_pic_rect[i]) #Putting the pictures on the screen
        else:
            pygame.draw.rect(screen, white, (mem_pic_rect[i][0], (mem_pic_rect[i][1]), pic_width, pic_height)) #If not revealed cover images with wite rectangle
    pygame.display.update() #Update game display 
     
    if pick1 != None and pick2 != None: #If pick1 and pick2 have been made
        if game_pics[pick1] == game_pics[pick2]: #If  pick1 equals pick2 
            pick1, pick2 = None, None #Set the picks back to none for further picks for more pairings
        else: #If pick1 and pick2 dont equal
            pygame.time.wait(700) #Wait time in between checking pairing
            revealed_imgs[pick1] = False #Change back to false to hide the picture again
            revealed_imgs[pick2] = False #Change back to false to hide the picture again
            pick1, pick2 = None, None #Set the picks back to none for further picks for more pairings
           
    complete = 1 #Intializing complete to 1
    for num in range(len(revealed_imgs)): #If there is a false in the revealedimg list then its a 0 
        complete *= revealed_imgs[num] # 0 * 1 is 0 so complete = 0 therefore game keeps going and if all are True then its 1 and 1*1 is 1
        
    if complete == 1: #If complete = 1 meaning all the pictures have been uncovered
        game_loop = False #Terminate the game after win

    pygame.display.update() #Updating the display

pygame.quit() #For quitting the game