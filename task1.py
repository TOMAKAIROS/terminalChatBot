print("Welcome to my text based program that records maintenance done on my Subaru.")

history = []
count = 0

def maintenance_question(myAnswer)
    if myAnswer == "history":
        return history
    elif myAnswer == "count":
        return count
    elif myAnswer == "quit":
        return "Goodbye..."