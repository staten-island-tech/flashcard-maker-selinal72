import json
try:
    with open("flashcards.json", "r") as file:
        flashcards_data = json.load(file)
except FileNotFoundError:
    flashcards_data = []
except json.JSONDecodeError:
    flashcards_data = []

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

    """ new_flashcard = {"phrase": input1, "answer": input2}
    flashcards_data.append(new_flashcard) """

    mansa_musa = flashcards(input1, input2)
    print(mansa_musa.create_dict())
    flashcards_data.append(mansa_musa.__dict__)

    print(flashcards_data)
    ask = input("Create flashcard? Y/N ")
else:
    with open("flashcards_data.json", "w") as file:
        json.dump(flashcards, file)

class student:
    def __init__(self, name, score, streak):
        self.name = name
        self.score = score
        self.streak = streak
    def points(self):
        self.score = self.score + 1
        return self.score
    def streaks(self):
        self.streak = self.streak + 1
        return self.streak
    def reset_streak(self):
        self.streak = 0
    def show_score(self):
        return self.score

selina = student("selina", 0, 0)
switch = input("Switch to Student Mode? Y/N ")
while switch == "Y":
    for flashcard in flashcards_data:
        print(flashcard["phrase"])
        attempt = input("Enter Answer: ")
        if attempt == flashcard["answer"]:
            print(f"Correct! Good job! Current Score: {selina.points()}. Current Streak: {selina.streaks()}")
        else:
            selina.reset_streak()
            print(f"Incorrect. Streak broken. Current Score: {selina.show_score()}")
    switch = input("Attempt another round? Y/N ")