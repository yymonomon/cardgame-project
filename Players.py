class Player ():
    def __init__(self, intStartingLife, tupDeckList, tuptInventoryList):
        self.StartLife = intStartingLife
        self.DeckList = lstDeckList
        self.InventoryList = lstInventoryList
        self.Life = self.StartLife
        self.Deck = list(self.DeckList)
        self.Inventory = list(self.InventoryList)
        self.DrawSize = 6
        self.Hand = []
        self.Heat = 0
        self.Cold = 0

    def draw(self, intDrawSize):
        for i in range(intDrawSize):
            self.Hand.append(self.Deck[0])
            self.Deck.pop([0])
