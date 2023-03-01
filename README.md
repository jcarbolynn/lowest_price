# Ada's EV Roadtrip 

Click the Open Preview button above for a more readable view of these instructions.

>Candidates receiving this challenge may elect to work through live coding a solution during their interview time, or may choose to solve the challenge ahead of time and walk through their solution during the interview. Candidates who prefer to live code are strongly encouraged to review the challenge ahead of time, and are free to use any prepared notes during the interview. Candidates who prefer to fully develop a solution ahead of time should be ready to discuss and potentially make changes to their solution with their interviewer.

## Getting Started

Begin the challenge by opening the `main.py` file in the Files view on the left. If the Files view is not already visible, click the top icon in the column of icons on the left, which resembles a sheet of paper with a bent corner.

Do not modify any file other than `main.py`.

## Requirements
- You will write a function with the input and outputs specified below.
- Your function must use at least one loop or iterator.
- Your function must use at least one conditional statement.
- Your function must use at least one Dictionary or List to store data. You should be familiar with the features of _**both**_ data types, even if you only use one in your function.
- The Python module math is imported and available to use but not required. Please do not import any additional modules (such as NumPy). 

## Problem Statement
Ada is planning a roadtrip from Helena, Montana to Adiecon in Seattle, Washington (1000km). You will create a program that will help Ada determine how expensive each available electric vehicle is for a road trip.

- Each Vehicle has a `range` (an integer in km), a `name` (a string), and a rental price.
- The function accepts a list of 
  - `vehicle_names`, a list of strings 
  - `vehicle_ranges`, a list of integers where each integer represents the range of the corresponding fully charge vehicle from vehicle_names
  - `vehicle_rental_prices`, a list of floats where each float represents the daily rental fee for a vehicle
- A Vehicle on the route must charge before exceeding its range.
- Fully Charging any vehicle is $5.00
- Print the name of the least expensive vehicle (cost/km) and the total amount it would cost to take it on a 1000 mile trip assuming a 3 day rental.

## Examples

These examples are also provided as a set of tests that can be run from the Tests panel at the left (the icon looks like a check mark). Clicking the Run tests button will run the Challenge inputs against your code, displaying either a success message, or a message about what was expected and what was observed.

### Example 1
#### Input (arguments of the function)
```
vehicle_names = ["Toyota Prius", "Leaf", "ID4"]
vehicle_ranges = [100, 200, 75]
vehicle_rental_prices = [50.00, 75.00, 100.00]
```
#### Output (printed by the function)
```
The least expensive vehicle is the Toyota Prius which will cost $200.00 to take on the trip.
```

### Example 2
#### Input (arguments of the function)
```
vehicle_names = ["Leaf"]
vehicle_ranges = [200]
vehicle_rental_prices = [75.00]
```
#### Output (printed by the function)
```
The least expensive vehicle is the Leaf which will cost $250.00 to take on the trip.
```
