#Exercise 1
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#Exercise 2
print("I could have code like this.")
# print("This won't run.")
print("This will run.")

#Exercise 3
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3+2<5-7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?",3 + 2)
print("What is 5 - 7?",5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?",5 > -2)
print("Is it greater or equal?",5 >= -2)
print("Is it less or equal?",5 <= -2)

#Exercise 4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers/cars_driven
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")

#Exercise 5
my_name = 'Hailing Xu'
my_age = 18
my_height = 1.80
my_weight = 70
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} metres tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
