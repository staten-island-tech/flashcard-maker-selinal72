car_rental = {
    "Toyota Corolla": {"daily_rate": 30, "available": False, "category": "Standard"},
    "Honda Civic": {"daily_rate": 35, "available": True, "category": "Standard"},
    "BMW X5": {"daily_rate": 80, "available": True, "category": "Luxury"},
    "Mercedes C-Class": {"daily_rate": 90, "available": False, "category": "Luxury"},
    "Ford Focus": {"daily_rate": 28, "available": True, "category": "Standard"}
}
rental_request = {
    "model": "Honda Civic",
    "days": 8}

standard = []
luxury = []
for x,y in car_rental.items():
    if y['category'] == "Standard" and y['available'] == True:
        standard.append(x)
    elif  y['category'] == "Luxury" and y['available'] == True:
        luxury.append(x)
print(standard)
print(luxury)
car = car_rental[rental_request['model']]
car_name = rental_request['model']
rental_cost = car['daily_rate'] * rental_request['days']

print(f"Renting {rental_request['model']}")
if car['available'] == True: 
    if car['category'] == standard:
        if rental_request['days'] > 7:
            print("Applying 15% discount for renting for more than 7 days.")
            print(f"Total rental cost before discounts: ${rental_cost}")
            discounted = rental_cost * 0.85
            print(f"Total rental cost after discounts: ${discounted}")
    else:
        if rental_request['days'] >= 5:
            print("Applying 10% discount for renting for more than 5 days.")
            print(f"Total rental cost before discounts: ${rental_cost}")
            luxdiscounted = rental_cost * 0.9
            print(f"Total rental cost after discounts: ${luxdiscounted}")
else: 
    print(f"{car_name} is unavailable. Suggesting {standard[0]} instead.")