print("Welcome to the Space Travel Calculator")
distance = float(input("Please input the distance in light-years!"))
speed = float(input("How fast are you going? (in fraction of the speed of light)"))
time = distance / speed
print("It will take you " + str(time) + " years to reach your destination.")