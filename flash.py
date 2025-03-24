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
    def display(card):
        print(card.phrase, card.answer)

ask = input("Create flashcard? Y/N ")
while ask == "Y":
    input1 = input("Enter Word/Phrase: ")
    input2 = input("Enter Definition/Answer: ")
    mansa_musa = flashcards(input1, input2)
    mansa_musa.display()
    cards_data.append(mansa_musa.__dict__)
    print(cards_data)
    ask = input("Create flashcard? Y/N ")

switch = input("Switch to Student Mode? Y/N ")
while switch == "Y":
    for phrase in cards_data:
        print(cards_data['phrase'])