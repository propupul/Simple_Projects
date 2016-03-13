__author__ = "Propupul"


import time
from random import randint

def main():
    keep_going = 'y'
    while keep_going == 'y':
        ask_question = input("Ask a question ")
        print("Thinking....")
        time.sleep(1.9999)
        eightball_responses()
        keep_going = input("Would you like to ask anothe question? [y/n]: ")
        if keep_going == 'n':
            print("See ya later!")
    
    

def eightball_responses():
    

        question_list = ["It is certain", "It is decidedly so", "Without a doubt",
                         "You may rely on it","As I see it, yes", "Most likely", "Outlook good",
                         "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now",
                         "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
                         "Outlook not so good", "Very doubtful", "Yes, definitely"]
        random_question = randint(1,20)
        
        print(question_list[random_question])
        
      

    
main()
