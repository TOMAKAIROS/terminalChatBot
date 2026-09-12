print("Hello")

botName = "Jarvis"
bot = "\n" + botName + ": "
answerCount = 0

while True:

    why = input(bot + "Why are you building this?\nYou: ")

    why = why.strip().lower()

    if why == "quit":
        print(bot + "Goodbye...")
        break
        
    if why != "":
        answerCount = answerCount + 1
    
    if why == "to learn" or why == "learn":
        print(bot + "You're on the right path.")
    elif why == "idk":
        print(bot + "Go figure it out!")
    elif why == "":
        print(bot + "say something...i'm giving up on you.") 
    else:
        print(bot + "awkward...")

    print(str(answerCount) + "\n")