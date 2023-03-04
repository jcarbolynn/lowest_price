# Refer to the README.md file in this project for a description 
# of the challenge and requirements. When viewing the README.md, 
# replit will show an option to Open Preview, which will open a 
# more readable view.

# The Python module math is imported and available to use but not required.
# Please do not import any additional modules (such as NumPy).
from vehicle import Vehicle

def ev_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices):
  cars_list = []

  # tuple = list(zip(vehicle_names, vehicle_ranges, vehicle_rental_prices))
  # print(tuple[0][1])
  # make sure you understand what you use lol

  # make vehicle objects
  # zip creates a new list with each list as a tuple, creates iterable object of bundles
  for vehicle, range, price in zip(vehicle_names, vehicle_ranges, vehicle_rental_prices):
    car = Vehicle(vehicle, range, price)
    cars_list.append(car)

  cheapest = cars_list[0]
  # cheapest.trip_price()
    
  for car in cars_list:
    if car.trip_price() < cheapest.trip_price():
      cheapest = car

  print(f"The least expensive vehicle is the {cheapest.name} which will cost ${cheapest.trip_price()}.00 to take on the trip.")

# You may call ev_roadtrip with your own arguments here.
# For example, if the following line is uncommented, and the Run button
# is clicked, it will call ev_roadtrip with the listed
# parameters. The supplied example uses the same arguments as the
# test Challenge01.
    
ev_roadtrip(vehicle_names=["Toyota Prius", "Leaf", "ID4"], vehicle_ranges=[100, 200, 75], vehicle_rental_prices=[50.00, 75.00, 100.00])
# ev_roadtrip(vehicle_names=["ID4"], vehicle_ranges=[75], vehicle_rental_prices=[100.00])

# The challenges are provided as a set of tests that can be run 
# from the Tests panel at the left (the icon looks like a check 
# mark). Clicking the Run tests button will run the Challenge 
# inputs against your code, displaying either a success message, 
# or a message about what was expected and what was observed.

# error if not enough info (in class) in main catch error
# good to write more tests
# how to make it more usable ex allow user to change trip mileage or 


# car_list = [
#   {
#     name: 'prius',
#     range: 100,
#     rent: 50,
#   },

#   {
#     name: 'leaf',
#     range: 200,
#     rent: 75,
#   },
#   {
#     name: 'ld4',
#     range: 75,
#     rent: 100,
#   }
# ]

# car_list[0]

# car_list_2 = {
# prius:
#   {
#     range: 100,
#     rent: 50,
#   }

# leaf:
#   {
#     range: 200,
#     rent: 75,
#   }

# id4:
#   {
#     range: 75,
#     rent: 100,
#   }
# }

