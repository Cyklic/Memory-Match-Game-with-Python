MEMORY MATCH GAME

By Leonard Umoru on 28th November, 2024

Objective
The Memory Match Game’s main objectives include creating a fun, challenging, and interactive environment 
that enhances cognitive abilities, helps strengthen short-term memory, enhances concentration, and tracks progress. 
This exercise is important to train one’s brain, especially for infants and ageing adults, to be better at 
remembering things, for both educational and real-life purposes. Ultimately, it is also a good way to relieve stress 
and pass time while still being productive and having fun.

Proposed Solution/Methodology
This project encourages players to engage with a grid of hidden image pairs, requiring them 
to remember image locations and the images themselves and uncover matches in sequence. I believe this will help improve 
their cognitive skills and attention to detail. The libraries that will be used in the creation of this project are:
• Pygame: This is a core library for creating game elements such as the game window, 
buttons, and animations. I will be using this to create the game window and for creating 
the cards and loading them with images. It will also be used to create the grid layout and 
handle click events.
• Random: This is a python library used to generate random numbers and perform random operations.This library will be 
used to shuffle and randomize the position of the images anytime a new game is started.
• Os: Os stands for Operating System, and it is a library used to interact with the operating system, providing 
functions to perform tasks such as navigating the file system, managing files and directories, interacting with 
environment variables, and working with process-related information. This library will be used get images from the 
file directory they are stored in, to be used in this project.

Results and Insights
I tested the game thoroughly myself and I have found that the more rounds of the game I play, the better I am at keeping 
track of the pictures. Not only is it improving my ability to remember in the game, but it has also helped me remember 
daily tasks more than before, as I usually forget some in the past. In addition to everything I have mentioned, the game
is fun and engaging. It is essentially killing two birds with one stone.

Based on these results, I can see this game helping young children build their cognitive abilities and train their 
memory growing up, as it can positively impact their future. I can also see the game helping the older generation. As 
we get older, we tend to forget more. But with this game, the rate of loss of memory can be reduced and help the older 
generation retain their cognitive abilities.

Challenges
Some of the challenges I had during the process of building this project were:
• Keeping track of the loops and if statements.
• Knowing which block of code to put above others to run without errors or bugs.
• Creating the grid layout was tough to figure out, my images where going outside of the window at one point.
• Allowing the player to click two pictures and creating the matching logic was tricky to perform


Dependencies for running the code
• Make sure to create your virtual enviroment to store your libraries. Type the following in your terminal in the order:

    python3 -m venv .venv
    .\.venv\Scripts\activate

  If you get an error saying you dont have permissions, type this in your terminal:
    Set-ExecutionPolicy Unrestricted -Scope Process

• Install pygames. Type this in your terminal:

    pip install pygame
    
• Make sure to have an images folder with these images inside it. Note: The image folder is outside the virtual 
environment.
• Make sure to have the .ttf file for the font.
• Finally run the program and enjoy the game.