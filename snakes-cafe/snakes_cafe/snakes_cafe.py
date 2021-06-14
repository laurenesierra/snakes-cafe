def greeting():
  print("""
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **                                  **
  ** To quit at any time, type "quit" **
  **************************************

  """)

greeting()

def menu():
  print("""
  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears
  """)

menu()

def order_prompt():
  print("""
  ***********************************
  ** What would you like to order? **
  ***********************************
  """)
  
  food_order = []
  while True:
    customer_order = str(input("> ").lower())
    x_number = len(food_order) + 1
    if customer_order == "quit":
      break
    else:
      food_order.append(customer_order)

      print("** " + str(x_number) + " order of " + str(food_order) + " have been added to your meal **")

order_prompt()
