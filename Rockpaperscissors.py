import random
exit=False
user_point=0
bot_point=0

while exit==False:
    options=["rock","paper","scissors"]

    user_input =input("Choose rock,paper,scissors or exit:")

    bot_input=random.choice(options)

    if user_input=="exit":
        print("your score is" +str(user_point)+"and the bot score is"+str(bot_point))
        print("Game Ended")
        
        exit=True
    if user_input =="rock":
        if bot_input=="rock":
            print("Your input is rock")
            print("Bot input is rock")
            print("Its a tie")    
        elif bot_input=="paper":
            print("Your input is rock")
            print("Bot input is paper")
            print("Bot Wins")   
            bot_point+=1
        elif bot_input=="scissors":
            print("Your input is rock")
            print("Bot input is scissors")
            print("You Win")   
            user_point+=1    
    elif user_input =="paper":
        if bot_input=="rock":
            print("Your input is paper")
            print("Bot input is rock")
            print("You Win")
            user_point+=1    
        elif bot_input=="paper":
            print("Your input is paper")
            print("Bot input is paper")
            print("Its a tie!")   
        elif bot_input=="scissors":
            print("Your input is paper")
            print("Bot input is scissors")
            print("Bot Win")   
            bot_point+=1    
    elif user_input =="scissors":
        if bot_input=="rock":
            print("Your input is scissors")
            print("Bot input is rock")
            print("Bot Win")
            bot_input+=1    
        elif bot_input=="paper":
            print("Your input is scissors")
            print("Bot input is paper")
            print("You Win")  
            user_point+=1 

        elif bot_input=="scissors":
            print("Your input is scissors")
            print("Bot input is scissors")
            print("Its a tie!")   

    elif user_input!="rock" or user_input!="paper" or user_input!="scissors" or user_input!="exit":
        print("Invalid Input")    
                              



