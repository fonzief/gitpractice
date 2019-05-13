letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points.update({" ": 0})

#print(letter_to_points)

def score_words(word):
  point_total = 0
  for l in word:
    point_total += letter_to_points.get(l, 0)
  return point_total

brownie_points = score_words("BROWNIE")
#print(brownie_points)


################vilda ord spelarna har###########
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES" , "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

## hur mycket poang varje spelare har

player_to_points = {}


#orden spelarna spelat kollas och poang samlas

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for l in words:
      player_points += score_words(l)
    player_to_points[player] = player_points

update_point_totals()



#nar man skriver ord laggs ord till i dic.. och poang uppdateras

def play_word(word, player):
  player_to_words[player].append(word.upper())
  update_point_totals()



play_word("dans", "player1")

#print(player_to_words)
print(player_to_points)




#https://www.youtube.com/watch?v=WjVJcCBazNI&feature=youtu.be&t=337
