class Card:
    def __init__(self, strDisplayName, intCost, intReturn, strType, fncRulesText, strTextBox): #intCost will be change to arrCost after resource system is finished
        if strDisplayName == "":
            self.FrontName = self
        else:
            self.FrontName = strDisplayName
        self.Cost = intCost
        self.Return = intReturn
        self.Type = strType
        self.Exe = fncRulesText
        self.Text = strTextBox

def loadCard(card):
    import card
    card = Card("", )
