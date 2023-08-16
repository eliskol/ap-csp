restaurants = ["Din Tai Fung", "Houston's", "Paulette's Pupusas", "Leah's Thai", "Taco Bell"]

new_restaurant = input("What restaurant would you like to add to the list?\n")

def ask_for_comparison(first_restaurant, second_restaurant):
    return input("Do you like A) " + first_restaurant +
          " or B) " + second_restaurant + " more?\n")

comparison = ask_for_comparison(new_restaurant, restaurants[2])

if comparison == "A":
    comparison = ask_for_comparison(new_restaurant, restaurants[1])
    if comparison == "B":
        restaurants.insert(2, new_restaurant)
    elif comparison == "A":
        comparison = ask_for_comparison(new_restaurant, restaurants[0])
        if comparison == "B":
            restaurants.insert(1, new_restaurant)
        elif comparison == "A":
            restaurants.insert(0, new_restaurant)

elif comparison == "B":
    comparison = ask_for_comparison(new_restaurant, restaurants[3])
    if comparison == "A":
        restaurants.insert(3, new_restaurant)
    elif comparison == "B":
        comparison = ask_for_comparison(new_restaurant, restaurants[4])
        if comparison == "A":
            restaurants.insert(4, new_restaurant)
        elif comparison == "B":
            restaurants.insert(5, new_restaurant)

print("Your current ranking of restaurants is " + str(restaurants))