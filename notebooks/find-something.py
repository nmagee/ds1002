# Look for an item and do something when you find it

fruit = ["apples","bananas","mangos","blueberries","kumquats","kiwis"]


def find_something(fruit):
  for f in fruit:
    if (f == "kumquats"):
      print("I found one!")
    else:
      print("Nothing here")

find_something(fruit)
