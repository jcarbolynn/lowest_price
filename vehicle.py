FULL_CHARGE = 5
TRIP_MILES = 1000
TRIP_DAYS = 3



class Vehicle:
 
  """Models each vehicle"""
  def __init__(self, car, range, price):
    self.name = car
    self.costs = {
      "range": range,
      "price": price,
    }
    # self.trip_price = trip_price(costs)


  def trip_price(self):

    cost_for_miles = (TRIP_MILES / self.costs['range']) * FULL_CHARGE
    cost_for_days = TRIP_DAYS * self.costs['price']
    total_cost = cost_for_miles + cost_for_days

    return round(total_cost)
    
    # print(f"{self.name}: \nrange: {self.costs['range']} \ntotal cost: {total_cost}")
    

  # def compare_costs(self, costs):
    

