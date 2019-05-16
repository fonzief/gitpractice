
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return "{name}. \"{title}\". {year}, {medium}. {owner_name}, {owner_location}.".format(name=self.artist, title=self.title, year=self.year, medium=self.medium, owner_name=self.owner.name, owner_location=self.owner.location)





class Marketplace:

  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.new_listings = new_listing
    self.listings.append(self.new_listings)
  ###testa om vad som hander utan definera new listings

  def remove_listing(self, listing):
    self.listing = listing
    self.listings.pop(self.listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)




class Client:

  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum is True:
        self.location = location
    else:
        self.location = "private collection"

  def sell_artwork(self, artwork, price):
    self.price = price
    self.artwork = artwork
    if self.artwork.owner == self:
      #verifierar att agaren av verket ar samma namn som ersatter client, dvs saljer.
      new_listin = Listing(self.artwork, self.price, self.name)
      veneer.add_listing(new_listin)



  def buy_artwork(self, artwork):
    self.artwork = artwork
    if self.artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == self.artwork:
          self.artwork.owner = self
          veneer.listings.remove(listing)
          break
          #varför definerades inte self.artwork i video? han skrev (if listing.art == artwork:)
#om konsten inte ags av koparen, kolla om art finns i listings, om den finns, byt agaren till koparen.tar bort fran listings





class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "{art}, {price}".format(art=self.art.title, price=self.price)






#######################information_marketplace###

veneer = Marketplace()



###############client information###########

edytta = Client("Edytta Halpirt", None, False)

moma = Client("The MOMA", "New York", True)

###############information_Art###########

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)
print(girl_with_mandolin)
#print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, 6000000)
##edytta saljer sin konst, den satts i listings




moma.buy_artwork(girl_with_mandolin)

#moma koper konsten som edytta salde. tas bort fran listings
#print(girl_with_mandolin)


print(veneer.show_listings())
#listings nu tom
