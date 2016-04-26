__author__ = "Propupul"

# MAD LIBS BABY!
# Programm makes the user enter words (nouns, adjectives, verbs,place)
# After the user enters the words, it prints out a story using those words!


def main():
    da_story = madlibs()
    print(da_story)


def madlibs():
    list_words = []
    for words in range(1,15):
        print("Enter word#", words)
        ask_words = input()
        list_words.append(ask_words.upper())
        if len(list_words) == 14:
            print("you have", list_words)
    story_in = ["Welcome to Beginner Python Projects. If you're new to", list_words[0], "{verb},in python, check out some of the",list_words[1],"{noun} for basic",list_words[2],"{plural noun} on this subreddit."
                "Each",list_words[3],"{noun} idea has a basic ",list_words[4],"{noun} for you to ",list_words[5],"{verb}, as well as subgoals that ",list_words[6],"{verb} a bit more thought, but help make your",list_words[7],"{noun} more interesting."
                "Before beginning, you should know the basics to Python such as",list_words[8],"{plural noun}, loops, dictionaries, and how to define functions. ",list_words[9],"{verb}, if you don't know how to do something, ",list_words[10],"{proper noun} is your friend. The overall intent for these projects is to ",list_words[11],"{noun} you from a beginning level to an intermediate level."
                "It is alright to post your code for a project, but please put it inside",list_words[12],"{noun} tags like this or link to it on a",list_words[13],"{adjective} website."]
    return(story_in)

main()




