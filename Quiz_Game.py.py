import pygame
from pygame.locals import *
import sys

# quiz data
questions =  ("1.What is the purpose of function in programming?",
             "2.Which of the following principles is essential for creating a user-friendly interface?",
             "3.What is an algorithm in the context of computational thinking?",
             "4.What is the purpose of a for loop in programming?",
             "5.Which of the following elements is commonly used to gather user input in a graphical user interface (GUI)?",
             "6.What does the term debugging refer to in programming and computational thinking?",
             "7.Which of the following is NOT a fundamental data type in most programming languages?",
             "8.What does the term UX stand for in the context of user interface design?",
             "9.What is an if statement used for in programming?",
             "10.What does the term variable scope refer to in programming?",
             "11.What is wireframing in the context of user interface design?",
             "12.What is the purpose of a flowchart in computational thinking?",
             "13.What is a comment in programming?",
             "14.What is the golden ratio often used for in design, including user interfaces?",
             "15.What is a pseudocode used for in problem-solving and programming?",
             "16.In programming, what is the purpose of a function parameter?",
             "17.What is the term responsive design referring to in web development and user interfaces?",
             "18.What is the term responsive design referring to in web development and user interfaces?",
             "19.What does the term debugging refer to in programming?",
             "20.What is the Fitts's Law used to describe in the context of user interface design?")

options =  (("A.To define a variable. ","B.To group a set of instructions into a reusable block. ","C.To perform mathematical calculations. ","D.To display text on the screen. "),
           ("A.Overload the screen with information to give users more options. ","B.Use inconsistent fonts and colors for visual variety. ","C.Maintain consistency in layout,fonts,and colors. ","D.Make buttons and links difficult to click for a challenge. "),
           ("A.A tupe of computer virus. ","B.A step-by-step set of instructions to solve a problem. ","C.A type of computer hardware. ","D.A computer programming langauge. "),
           ("A.To define a new data type. ","B.To create an object-oriented class. ","C.To repeat a set of instructions a speccified number of times. ","D.To handle user input. "),
           ("A.Text lable. ","B.Check box. ","C.Image. ","D.Header. "),
           ("A.A process for making code run slower. ","B.A steb-by step guide for writing code. ","C.The process of identifying and fixing errors or bugs in code ","D.A type of computer virus. "),
           ("A.Integer. ","B.String. ","C.Array. ","D.Email. "),
           ("A.Universal XML. ","B.User Experience ","C.Uniform XAML. ","D.User Extension. "),
           ("A.To declare a variable. ","B.To compare two values and execute code based on a condition. ","C.To define a function. ","D.To print a message to the console. "),
           ("A.The size of a variable in memory. ","B.The visibility and accessibility of a variable with a program. ","C.The data type of a variable. ","D.The lifetime of a variable. "),
           ("A.A technique for connecting wires to the user interface. ","B.A visual representation of the layout and structure of a user interface. ","C.A type of coding language. ","D.A method for designing 3D graphics. "),
           ("A.To represent the flow of data within a computer's hardware. ","B.To visualize and document the steps of an algorithm or process. ","C.To create colorful graphics for a user interface. ","D.To execute code on a web server. "),
           ("A.A note to yourself to remember your grocery list. ","B.A section of code that is ignored by the computer.  ","C.A type of error in your code. ","D.A communication channel between programs. "),
           ("A.To calculate complex mathematical functions. ","B.To create visually pleasing porportions and layouts. ","C.To measure time intervals in a user interface. ","D.To design games and animations. "),
           ("A.A fake code code that is not used in real programs. ","B.A programming langauge for beginners. ","C.A simplified and human-readable description of an algorithm.  ","D.A type of programming errror. "),
           ("A.To specify the name of a function. ","B.To provide additional information about the program. ","C.To pass data to a function when it is called. ","D.To define the return type of a function. "),
           ("A.Designing interfaces with bright and contrasting colors. ","B.Creating interfaces that responds to voice commands. ","C.Designing interfaces that adapt to different screen sizes and devices. ","D.Designing interface that requires user registration. "),
           ("A.To make algorithms that never fail. ","B.To find algorithms that never fail. ","C.To improve the efficiency and performance of algorithms.","D.To create algoritms for artistic expression. "),
           ("A.A process for making code run slower. ","B.A step-by step guide for writing code. ","C.A process of identifying and fixing errors or bugs in code. ","D.A type of computer virus. "),
           ("A.The study of gravitational forces in space. ","B.The relationship between input time,distance,and target size in user interface elements. ","C.A law of thermodynamics ","D.A law of robotics. "),) 
       
answers = ("B","C","B","C","B","C","D","B","B","B","B","B","B","B","C","C","C","C","C","B")
guesses = []


# Initialize Pygame
pygame.init()

#Initialize pygame mixer
pygame.init()

#Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

#Load your music file
pygame.mixer.music.load('C:\swe\pygame\pygame.sound.mp3')

#play the music when game starts
pygame.mixer.music.play(-1)# The -1 argument loops the music indefinitely


# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Quiz Game")

# Define fonts and colors
font = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# Initialize variables
question_num = 0
score = 0

# Flag to track whether the game is over
game_over = False

# Function to check if the mouse is hovering over an option
def is_option_hovered(option_index):
    if question_num < len(questions):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        option_bounds = (50, 200 + option_index * 50, 500, 50)
        return option_bounds[0] <= mouse_x <= option_bounds[0] + option_bounds[2] and option_bounds[1] <= mouse_y <= option_bounds[1] + option_bounds[3]
    else:
        return False  # If there are no more questions, no options can be hovered.

# Function to display a countdown timer
def display_countdown():
    countdown_surface = font.render(f"Time Left: {remaining_time} seconds", True, WHITE)
    screen.blit(countdown_surface, (500, 30))

# Define the countdown duration in seconds for each question
COUNTDOWN_DURATION = 10
current_time = 0
remaining_time = COUNTDOWN_DURATION # Initialize remaining_time

# Create a pygame clock object to control the frame rate
clock = pygame.time.Clock()



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# Load button images (update file paths to the correct location)
start_img = pygame.image.load('C:\swe/start_btn.jpg.png').convert_alpha() 
exit_img = pygame.image.load('C:\swe/exit_btn.jpg.png').convert_alpha()


# Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw the button on the screen
        Screen.blit(self.image, self.rect.topleft)

        return action

# Creating button instances
start_button = Button(100, 100, start_img, 0.5)
exit_button = Button(400, 100, exit_img, 0.5)

# Game loop
run = True

def game_logic():
    print("The game has started!")

in_menu = True

# Main game loop
while in_menu:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Screen.fill(BLACK)

    if start_button.draw():
        in_menu = False  # Start the game
    if exit_button.draw():
        pygame.quit()
        sys.exit()

    # Render and display the menu elements
    welcome_text = font.render("WELCOME TO QUIZ GAME", True, (255, 255, 255))
    welcome_rect = welcome_text.get_rect()
    welcome_rect.center = (SCREEN_WIDTH // 2, 450)
    Screen.blit(welcome_text, welcome_rect)

    pygame.display.update()

# Game logic and quiz loop start here
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if not game_over:
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if question_num < len(questions) and 200 <= mouse_y <= 200 + 4 * 50:
                    option_index = (mouse_y - 200) // 50
                    guess = chr(ord('A') + option_index)
                    guesses.append(guess)
                    if guess == answers[question_num]:
                        score += 1
                    question_num += 1
                    current_time = 0

                    if question_num == len(questions):
                        game_over = True

        screen.fill(BLACK)

        if not game_over:
            if question_num < len(questions):
                question_surface = font.render(questions[question_num], True, WHITE)
                screen.blit(question_surface, (50, 100))

                option_y = 200
                for i, option in enumerate(options[question_num]):
                    option_color = YELLOW if is_option_hovered(i) else WHITE
                    option_surface = font.render(option, True, option_color)
                    screen.blit(option_surface, (50, option_y))
                    option_y += 50

            remaining_time = COUNTDOWN_DURATION - (current_time // 60)

            if remaining_time <= 0:
             # Time's up, handle this case as needed 
                    question_num += 1
                    current_time = 0  # Reset the timer                       
                         
        else:
            result_surface = font.render("RESULTS", True, BLACK)
            score_surface = font.render(f"Your score: {score}/{len(questions)}", True, WHITE)
            screen.blit(result_surface, (50, 100))
            screen.blit(score_surface, (50, 150))
            exit_message = font.render("Click anywhere to exit", True, GRAY)
            screen.blit(exit_message, (50, 400))

       
        # Display the countdown timer
        display_countdown()
        pygame.display.flip()
        current_time += 1
         # Controlling the frame rate to keep the game running at a consistent speed
        clock.tick(60)  # Limit the frame rate to 60 frames per second



thank_you_surface = font.render("Thank you!", True, WHITE)
screen.blit(thank_you_surface, (50, 500))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
