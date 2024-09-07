import random
import win32com.client

class inputError(Exception):
    pass

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def user_input():
    while True:
        try:
            return int(input())
        except ValueError:
            print("An Error Occured: Enter integer value")
            speaker.speak('n Error Occured: Enter integer value')
Game = 'Snake Water Gun'
print("#"*80)
print(Game.center(80))
print("#"*80)
speaker.speak('Welcome to snake water gun game')
print("Enter 0 for Snake\n 1 for Water\n 2 for Gun\n -1 to Stop or Exit the Game")
speaker.speak("Enter 0 for Snake\n 1 for Water\n 2 for Gun\n -1 to Stop or Exit the Game: ")

#user points
points = 0
choices = list(range(3))

choice = {0:'Snake', 1:'Water', 2:'Gun'}

#Game 
user_choice = None

while True:

    #bot
    bot_choice = random.choice(choices)
    
    try:
        print('Your Choice Here:', end='  ')
        user_choice = user_input()
        if user_choice not in [-1, 0, 1, 2]:
            raise inputError("WRONG INPUT VALUE") 
    except inputError as e:
        print(e)
        speaker.speak('Wrong input value')
    except Exception as e:
        print(e)
        speaker.speak(e)

    else:
        if user_choice==-1:
            print("Game Over")
            speaker.speak("Game Over")
            print(f"Your points: {points}")
            speaker.speak(f"Your points: {points}")
            break

        print("$"*20)
        print(f"Your Choice: {choice[user_choice]}")
        speaker.speak(f"Your Choice: {choice[user_choice]}")
        print(f"Bot's Choice: {choice[bot_choice]}")
        speaker.speak(f"Bot's Choice: {choice[bot_choice]}")

        if bot_choice == user_choice:
            print("Match Draw")
            speaker.speak("Match Draw")
            print("$"*20)
        elif bot_choice==0 and user_choice==1:
            print("You Lost")
            speaker.speak("You Lost")
            print("$"*20)
            points -= 1
        elif bot_choice==1 and user_choice==2:
            print("You Lost")
            speaker.speak("You Lost")
            print("$"*20)
            points -= 1
        elif bot_choice==2 and user_choice==0:
            print("You Lost")
            speaker.speak("You Lost")
            print("$"*20)
            points -= 1
        else:
            print("You Won")
            speaker.speak("You Won")
            print("$"*20)
            points += 1
        
        if points == -2:
            print('(*o*) Wasted (*o*)')
            speaker.speak('You have consistently lost 3 matches. You are the biggest looser I have ever met. I can\'t play with you more. Get Lot')
            break