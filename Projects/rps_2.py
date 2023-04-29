import pygame
import os 
import random 
WIDTH , HEIGHT = 900 ,500
import sys
from pydub import AudioSegment
from pydub.playback import play
from pyvidplayer import Video

song = AudioSegment.from_mp3("C:/Users/ADMIN/Desktop/Project PC/Projects/Assets/Songs/Click.mp3")
WInn = AudioSegment.from_mp3("C:/Users/ADMIN/Desktop/Project PC/Projects/Assets/Songs/Winnner_.mp3")
score_user = 0
score_comp = 0
Computer = ""
user = ""
Winner = ""

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors ")

FPS = 60

pygame.init()
WHITE = (255,255,255)

Rock_i = pygame.image.load(os.path.join("Projects/Assets/images" , 'rock.png'))

Paper_i = pygame.image.load(os.path.join("Projects/Assets/images" , 'Paper.png'))

Scissor_i = pygame.image.load(os.path.join("Projects/Assets/images" , 'scissors.png'))

List = ["Rock", "Paper", "Scissor"]

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

Rock_w = 200
Rock_h = 200
Paper_w = 200
Paper_h = 200
Scissor_w = 200
Scissor_h = 200

Rock_i = pygame.transform.scale(Rock_i, (Rock_w, Rock_h))
Paper_i = pygame.transform.scale(Paper_i, (Paper_w, Paper_h))
Scissor_i = pygame.transform.scale(Scissor_i, (Scissor_w, Scissor_h))

def func(one, compu):
    global score_comp , score_user    
    if one == "Rock" and compu == "Scissor":
        score_user += 1
        
        # print("You Won a point")
        game(score_user, score_comp)
    elif one == "Paper" and compu == "Rock":
        score_user += 1
        # print("You Won a point")
        game(score_user, score_comp)
    elif one == "Scissor" and compu == "Paper":
        score_user += 1
        # print("You Won a point")
        game(score_user, score_comp)

    
    elif one == "Rock" and compu == "Paper":
        score_comp += 1
        # print("Computer Won a point")
        game(score_user, score_comp)

    elif one == "Paper" and compu == "Scissor":
        score_comp += 1
        # print("Computer Won a point")
        game(score_user, score_comp)
    elif one == "Scissor" and compu == "Rock":
        score_comp += 1
        # print("Computer Won a point")
        game(score_user, score_comp)
    else:
        print("You and Computer gotta same")
        game(score_user, score_comp)


vid = Video('C:/Users/ADMIN/Desktop/Project PC/Projects/Assets/images/outro.mp4')
vid.set_size((900,500))

def outro():
    while True:
        vid.draw(WIN,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()

def game(score_a,score_b):
    global score_user , score_comp , Winner
    if score_a == 10 :
        # print("You Have Won the match")
        Winner = "User"
        outro()
        play(WInn)
        
        score_user = 0
        score_comp = 0
    elif score_b == 10 :
        # print("Computer Have Won the match")
        Winner = "Computer"
        outro()
        play(WInn)
        
        score_user = 0
        score_comp = 0
    else:
        pass
    



black= (0,0,0)
def draw_window(roc,pap,sciss,user_point,comp_point,Winner):
    WIN.fill(WHITE)
    font = pygame.font.Font('freesansbold.ttf', 32)
    user_point_text = font.render("User: " + str(user_point), True, green, blue)
    comp_point_text = font.render("Computer: " + str(comp_point), True, green, blue)
    Winner_Text = font.render(Winner + " is the Winner", True , black)    
    WIN.blit(user_point_text, (10,10))
    WIN.blit(comp_point_text, (700,10))
    WIN.blit(Winner_Text,(350,10))
    WIN.blit(Rock_i,(roc.x,roc.y))
    WIN.blit(Paper_i,(pap.x,pap.y))
    WIN.blit(Scissor_i,(sciss.x,sciss.y))    

    
    pygame.display.update()

def main():    
    roc = pygame.Rect(50, 80, Rock_w, Rock_h)
    pap = pygame.Rect(320 , 80, Paper_w, Paper_h)
    sciss = pygame.Rect(580,80, Scissor_w, Scissor_h)
    clock = pygame.time.Clock()
    handled = False
    run = True
    while run:
    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:    
                play(song)
                
                comp = random.choice(List)
                # print(comp)
                
                if roc.collidepoint(pygame.mouse.get_pos()) and not handled :
                    # print ("You have clicked roc")
                    func("Rock",comp)
                    game(score_user, score_comp)
                elif pap.collidepoint(pygame.mouse.get_pos()) and not handled:
                    # print("You have clicked paper")
                    func("Paper",comp)
                    game(score_user, score_comp)

                elif sciss.collidepoint(pygame.mouse.get_pos()) and not handled:
                    
                    func("Scissor",comp)
                    game(score_user, score_comp)

                else:
                    print("Click at the right place")
            
            
    
        draw_window(roc , pap,sciss,score_user,score_comp,Winner)
    pygame.quit()

if __name__ == '__main__':
    main()
