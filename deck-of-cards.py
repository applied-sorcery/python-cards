 # a single card model:
 # {
 #   "value": <1 - 13>,
 #   "suit": <h, c, s, d>,
 #   "description": "${value} of ${suit}"  | ex: "ten of hearts",
 # }


import random

def main():

    # this started as a deck of cards, now it's texas hold 'em poker:
PLAYERS = 2;
ROUNDS = ["pre-flop", "flop", "turn", "river"]

# ignoring blinds and betting amounts for simplicity
# pre-flop - this is after all the hole cards have been dealt (2 to each player) and the blinds have been put out

  deck_of_cards = []
  suits = ["hearts","spades","diamonds","clubs"]
  values = list(range(13))
  vals = []
  for v in values:
    vals.append(v+2)

  for s in suits
      for v in vals:
          deck_of_cards.append({'value':v,'suit':s, 'description':get_card_description(v,s)})

  #print(deck_of_cards)
  shuffle_cards(deck_of_cards)
  random.shuffle(deck_of_cards)
  quick_print(deck_of_cards)

def get_card_description(val, suit):

  valueLookup = { '11':'jack', '12':'queen', '13':'king', '14':'ace'}
  if val > 10:
      result_v = valueLookup[str(val)]
  else:
      result_v = val

  description_str = "%s of %s" % (result_v, suit)

  return description_str

def shuffle_cards(deck):
  deck = ""

def quick_print(deck):
    for card in deck:
        print("(%s,  %s)" % (card['value'], card['suit']))

 # # # #
if __name__ == "__main__":
    main()
