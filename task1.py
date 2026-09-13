print("Welcome to my text based program that records maintenance done on my Subaru.\n")

history = []
count = 0

def maintenance_question(myAnswer):
    if myAnswer == "history":
        return history
    elif myAnswer == "count":
        return count
    elif myAnswer == "quit":
        return "Goodbye..."
    elif myAnswer != "":
        return "Let's try this again...\n"
    else:
        history.append(myAnswer)
        count += 1
        return "Maintenance Recorded"

while True:
    
    myAnswer = input("What maintenance did you complete? Type history, count, or quit\n\n")

    myAnswer = myAnswer.strip().lower()
    
    question = maintenance_question(myAnswer)

    if myAnswer == "quit":
        break
    
    print(history)
    print("\n" + count)