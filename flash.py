class flashcards:
    input1 = input("Enter Word/Phrase: ")
    input2 = input("Enter Definition/Answer: ")
    def __init__(card, phrase, answer):
        card.phrase = phrase
        card.answer = answer
    def display(card):
        print(card.phrase, card.answer)
mansa_musa = flashcards(input1, "Mansa Musa")
mansa_musa.display()