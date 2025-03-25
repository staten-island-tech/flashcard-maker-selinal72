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
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def points(self):
        self.score =+ 1

selina = student("selina", 0)
switch = input("Switch to Student Mode? Y/N ")
while switch == "Y":
    phrases = cards_data['phrase']
    print(phrases)