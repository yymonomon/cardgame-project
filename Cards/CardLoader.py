import json
from Cards import CardFunctions as cFuncs

class Card:
    def __init__(
        self,
        strName,
        strType,
        strText,
        intStrike,
        intBlock,
        lstCost,
        lstReturn,
        fncRulesText
    ):

        self.Name     = strName
        self.Type     = strType
        self.Text     = strText
        self.Strike   = intStrike
        self.Block    = intBlock
        self.Cost     = lstCost
        self.Return   = lstReturn
        self.Function = fncRulesText

def parseCardFunctionIntoStack(objCard):
    stack = []
    for i in range(len(objCard.Function)):
        match objCard.Function[i]:
            pass
            #TODO: Add cardFunctions -> stack.
            
def loadCard(strFileName):
    with open(strFileName, 'r') as f:
        data = json.load(f)
    card = Card(
        data['Name'],
        data['Type'],
        data['Text'],
        data['Cost'],
        data['Return'],
        data['Function']
    )
    return card
