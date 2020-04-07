ex1  
print("Hello World!")  
print("Hello Again!")  
print("I don't like typing English!")  
print("This is torturing!")  
print("'test'")  
---  
ex2  
#print("comments testing") 
print("This is not a comment")
---  
ex3  
print("math test:")
print("5 add 2 equals",5+2)
print("5 minus 2 equals",5-2)
print("5 mutiplys 2 equals",5*2)
print("5 divided by 2 equals",5/2)
print("what's left when 5 is divided by 2 equals",5%2)
print("5 is larger than 2 is",5>2)
print("5 is smaller than 2 is ",5<2)
print("5 is not larger than 2 is",5<=2)
print("5 is not smaller than 2 is",5>=2)
--- 
ex4&5  
cars = 40
car_holds = 4
car_color = 'white'
vans = 20
van_holds = 6
van_color = 'grey'
drivers = 80
drivers_left = drivers - cars - vans
maximum_passenger = car_holds*cars + van_holds*vans - (drivers - drivers_left)
print("we have",cars,car_color,"cars")
print(f"we have {vans} {van_color} vans")
print(f"{drivers_left} drivers are not needed")
print(f"we can hold {maximum_passenger} passengers at most")
