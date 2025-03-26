import json
try:
    with open("cards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

class flashcards:
    def __init__(card, phrase, answer):
        card.phrase = phrase
        card.answer = answer
    def create_dict(card):
        print(card.phrase, card.answer)
        x = {card.phrase : card.answer}
        return x


ask = input("Create flashcard? Y/N ")
while ask == "Y":
    input1 = input("Enter Word/Phrase: ")
    input2 = input("Enter Definition/Answer: ")
    mansa_musa = flashcards(input1, input2)
    print(mansa_musa.create_dict())
    cards_data.append(mansa_musa.__dict__)
    print(cards_data)
    ask = input("Create flashcard? Y/N ")
    print(cards_data)

class student:
    def __init__(self, name, score, streak):
        self.name = name
        self.score = score
        self.streak = streak
    def show_score(self):
        print(self.score)
    def points(self):
        self.score =+ 1
    def streaks(self):
        self.streak =+1
    def reset_score(self):
        self.streak = 0

selina = student("selina", 0, 0)
switch = input("Switch to Student Mode? Y/N ")
while switch == "Y":
    for x in cards_data:
        phrases = x['phrase']
        print(phrases)
        attempt = input("Enter Answer: ")
        if attempt == phrases['answer']:
            print(f"Correct! Good job! Current Score: {print(selina.points())}. Current Streak: {print(selina.streaks())}")
        else:
            selina.reset_score()
            print(f"Incorrect. Streak broken. Current Score: {print(selina.show_score())}")
    again = input("Attempt another round? Y/N ")