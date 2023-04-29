import random

Set = ["Rock","Paper","Scissor"]
score_comp = 0
score_user = 0
while score_user<=9 and score_comp <= 9:
    print("**"*10)
    print("Rock, paper, Scissor Game")
    print("**"*10)
    print("""It's a Rock Paper Scissor Game 
        Enter Your Choice
        1.Rock == 1 
        2.Paper == 2
        3.Scissor == 3""")
    get = int(input("Choice: "))

    comp = random.choice(Set)
    if get == 1 and comp == "Scissor":
        print("You gotta point")
        score_user += 1
        print("Your Point = " + str(score_user))
        print("Computer Point = " + str(score_comp))
    elif get == 2 and comp == "Rock":
        print("You gotta point")
        score_user += 1
        print("Your Point = " + str(score_user))
        print("Computer Point = " + str(score_comp))
    elif get == 3 and comp == "Paper":
        print("You gotta point")
        score_user += 1
        print("Your Point = " + str(score_user))
        print("Computer Point = " + str(score_comp))
    elif get == 1 and comp == "Paper":
        print("Computer Got a point")
        score_comp +=1
        print("Your score = " + str(score_user) )
        print("Computer point = " + str(score_comp))
    elif get == 2 and comp == "Scissor":
        print("Computer Got a point")
        score_comp +=1
        print("Your score = " + str(score_user) )
        print("Computer point = " + str(score_comp))
    elif get == 3 and comp == "Rock":
        print("Computer Got a point")
        score_comp +=1
        print("Your score = " + str(score_user) )
        print("Computer point = " + str(score_comp))
    # elif get != [1,2,3]:
    #     print("Make the right choice")
    else:
        print("You and computer gotta same ")
        print("Or You Have entered a Wrong one")
        print("\n")

if score_user == 10:
    print("You Won The Match and the computer lost by ")
    print("Just " + str(10-score_comp) + " Points" )
elif score_comp == 10:
    print("Computer Won the Match and you lost by ")
    print("Just " + str(10-score_user) + " Points")
