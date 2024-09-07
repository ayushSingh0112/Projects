import random as r
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class GuessTheNumber:
    number = 0
    noOfGuesses = 0

    def __init__(self):
        self.number = r.randint(0, 100)
        self.noOfGuesses = 0

    def setNoOfGuesses(self, noOfGuesses):
        self.noOfGuesses = noOfGuesses

    def getNoOfGuesses(self): 
        return self.noOfGuesses
    
    def takeUserInput(self):
        try:
            self.userInput = int(input())
        except(ValueError):
            print('An Error Occured. Please enter a valid integer')
            speaker.Speak('An Error Occured. Please enter a valid integer')
    
    def isCorrectNumber(self):
        self.noOfGuesses+=1
        if self.userInput == self.number:
            print(f"Congratulations\nYou guess the number right in {self.noOfGuesses} attempts")
            speaker.Speak(f"Congratulations\nYou guess the number right in {self.noOfGuesses} attempts")
            return True
        
        elif(self.userInput < self.number):
            print("It's Low, Guess Again: ")
            speaker.Speak("It's Low, Guess Again: ")

        elif(self.userInput > self.number):
            print("It's High, Guess Again: ")
            speaker.Speak("It's High, Guess Again: ")
        
        return False
    
game = GuessTheNumber()
flag = False
speaker.Speak('Welcome to guess the number game')
print("Enter your number: ")
speaker.Speak("Enter your number: ")
while flag != True:
    game.takeUserInput()
    flag = game.isCorrectNumber()