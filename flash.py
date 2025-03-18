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


car_rental = {
    "Toyota Corolla": {"daily_rate": 30, "available": False, "category": "Standard"},
    "Honda Civic": {"daily_rate": 35, "available": True, "category": "Standard"},
    "BMW X5": {"daily_rate": 80, "available": True, "category": "Luxury"},
    "Mercedes C-Class": {"daily_rate": 90, "available": False, "category": "Luxury"},
    "Ford Focus": {"daily_rate": 28, "available": True, "category": "Standard"}
}
rental_request = {
    "model": "Toyota Corolla",
    "days": 8}

standard = []
luxury = []
for x in car_rental.values():
    if x['category'] == "Standard" and x['available'] == True:
        standard.append(x)
    elif 
print(standard)
print(luxury)
print(standard[0])
car = car_rental[rental_request['model']]
rental_cost = car['daily_rate'] * rental_request['days']

if car['available'] == True: 
    if car['category'] == standard:
        if car['days'] > 7:
            print("Applying 15% discount for renting for more than 7 days.")
            print(f"Total rental cost before discounts: ${rental_cost}")
            discounted = rental_cost * 0.85
            print(f"Total rental cost after discounts: ${discounted}")
    else:
        if car['days'] >= 5:
            print("Applying 10% discount for renting for more than 5 days.")
            print(f"Total rental cost before discounts: ${rental_cost}")
            luxdiscounted = rental_cost * 0.9
            print(f"Total rental cost after discounts: ${luxdiscounted}")
else: 
    print(f"{car} is unavailable. Suggesting {standard[0]} instead.")
