""" def teacher_mode(): 
    class flashcards:
        def _init_(card, phrase, answer):
            card.phrase = int("Word/Phrase: ")
            card.answer = int("Definition/Answer: ")
        def create  """

# car rental service
""" standard = []
for properties in car_rental:
    if properties["category"] ==
for properties in rental_request:
    if properties["model"[avaliable]] == False:
        print(f"Toyota Corolla is unavailable. Suggesting ") """


standard = []
luxury = []

for key, value in car_rental.items():

    if value["category"] == "Standard":
        standard.append(key)
    elif value["category"] == "Luxury":
        luxury.append(key)

    for x, y in rental_request.items():
        if key == y:
            cost = value["daily_rate"] * y
            if value["avaliable"] == False:
                print(f"The {key} is unavailable. Suggesting {standard[0]} instead.")

            elif value["category"] == "Luxury" and y >= 5:
                luxdisc = cost * 0.9
                print(f"pre-discount rental cost = {cost}, discounted rental cost = {luxdisc}")
            elif y > 7:
                discounted = cost * 0.85
                print(f"discounted daily rate = {discounted}")
