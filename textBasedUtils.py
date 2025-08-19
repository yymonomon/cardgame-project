import Players
from Cards import CardLoader as cload

Character = ''

def gameStart():
    print("Game started... ")
    print("Loading Cards...")
    card = cload.loadCard("Cards/card.json")
    print(card.Name)
    arr = [card, card]
    for i in arr:
        print(i.Name)
