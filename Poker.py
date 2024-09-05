

cards = {'S2': 2,'S3': 3,'S4': 4,'S5': 5,'S6': 6,'S7': 7,'S8': 8,'S9': 9,'S10': 10,'SJ': 11,'SQ': 12,'SK': 13,'SA': 14}
# S2 has numerical value 2. S3 has numerical value 3, and so on. SJ has numerical value 11, SQ has value 12, SK has value 13, and SA has value 14.

def check_straight(card1, card2, card3):
   values = [cards[card1], cards[card2], cards[card3]]
   values.sort()
   print(values)
   if (values[2] - values[1] == 1) and (values[1] - values[0] == 1):
      return max(values)
   else:
      return 0
print(check_straight('S9','SJ', 'S8'))

def check_3ofa_kind(card1, card2, card3):
   values = [cards[card1], cards[card2], cards[card3]]
   if (values[2] == values[1]== values[0]):
      return values[0]
   else:
      return 0


def check_royal_flush(card1, card2, card3):
   return 14 if (check_straight(card1, card2, card3)) == 14 else 0




# print(check_straight("S9", "S7", "S8"))



