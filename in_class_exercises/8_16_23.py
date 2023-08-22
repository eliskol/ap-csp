is_happy = False
if is_happy:
    print("\U0001F600")
elif not is_happy:\
    print("\U0001F616")

user_age = int(input("Input your age!\n"))
if user_age % 3 == 0 or user_age > 700:
    print("You can drink the concoction!")
else:
    print("No drinking!")