itemsb = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

itemse = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

itemsd = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

itemsk = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}



#############################################


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return str(self.name) + " menu is open beetwen " + str(self.start_time) + " and " + str(self.end_time)+ "."

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    bill = 0
    for n in purchased_items:
      bill += self.items.get(n)
    return bill
#self.items.get(n) retrieves the value of the items looping in the list from the brunch menu

################################################


class Franchise:
  def __init__(self, address, menus):
    self.adress = address
    self.menus = menus

  def __repr__(self):
    return "this is the restourant on " +str(self.adress)+"."

  def available_menus(self,time):
    available_menus = []
    for m in self.menus:
      if time <= m.end_time and time >= m.start_time:
        available_menus.append(m)
    return available_menus

################################################


#################menu info######################



brunch = Menu("brunch", itemsb, 1100, 1600)

early_bird = Menu("early_bird", itemse, 1500, 1800)

dinner = Menu("Dinner", itemsd, 1700, 2300)

kids = Menu("Kids", itemsk, 1100, 2100)

################bills info######################

brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
#printas blir 13.5

early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
#printas blir 21.5


all_menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", all_menus )

new_installment = Franchise("12 East Mulberry Street", all_menus )

print(new_installment.available_menus(1200))
################arepas#####################
itemsa = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a Arepa", itemsa, 1000, 2000)



arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu )
################################################


class Business:
  def __init__(self, name, franchises):
    pass






   ################busnisses#######################

Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

Business("Take a' Arepa", arepas_place)
